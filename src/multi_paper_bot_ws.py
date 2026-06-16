"""Paper trading bot skeleton.

This demo version does not connect to a real exchange.
It shows the intended control flow: config -> market data -> strategy -> risk -> paper order -> log.
"""

from __future__ import annotations

import csv
import datetime as dt
from pathlib import Path
from typing import Dict, Any

from config_loader import get_env_config, load_json_config
from risk_manager import RiskManager
from strategy import generate_demo_signal


DEMO_PRICES = {
    "BTCUSDT": 42000.0,
    "ETHUSDT": 2300.0,
    "SOLUSDT": 100.0,
}


def ensure_trade_log(path: str) -> Path:
    log_path = Path(path)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    if not log_path.exists():
        with log_path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                "timestamp",
                "symbol",
                "side",
                "mode",
                "entry_price",
                "exit_price",
                "quantity",
                "order_size_usdt",
                "pnl_usdt",
                "reason",
            ])

    return log_path


def append_paper_trade(log_path: Path, trade: Dict[str, Any]) -> None:
    with log_path.open("a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(trade.keys()))
        writer.writerow(trade)


def run_paper_bot() -> None:
    env = get_env_config()
    config = load_json_config()

    trade_log_path = ensure_trade_log(env["trade_log_path"])
    global_risk = config.get("global_risk", {})

    risk_manager = RiskManager(
        max_daily_loss_usdt=float(global_risk.get("max_daily_loss_usdt", 25)),
        max_open_positions=int(global_risk.get("max_open_positions", 3)),
        allow_live_trading=False,
    )

    print("[INFO] Starting Bybit Trading Bot")
    print("[INFO] Mode: paper")
    print(f"[INFO] Trade log: {trade_log_path}")

    for symbol_config in config["symbols"]:
        if not symbol_config.get("enabled", False):
            continue

        symbol = symbol_config["symbol"]
        last_price = DEMO_PRICES.get(symbol, 1.0)
        order_size = float(symbol_config.get("order_size_usdt", 10))

        signal = generate_demo_signal(symbol, last_price, order_size)
        if signal is None:
            continue

        decision = risk_manager.check_signal(signal, symbol_config, trading_mode="paper")
        print(f"[INFO] {symbol} signal={signal.side} confidence={signal.confidence} risk={decision.reason}")

        if not decision.allowed:
            continue

        quantity = order_size / last_price
        exit_price = last_price * 1.001 if signal.side == "Buy" else last_price * 0.999
        pnl = (exit_price - last_price) * quantity if signal.side == "Buy" else (last_price - exit_price) * quantity

        trade = {
            "timestamp": dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
            "symbol": symbol,
            "side": signal.side,
            "mode": "paper",
            "entry_price": round(last_price, 4),
            "exit_price": round(exit_price, 4),
            "quantity": round(quantity, 8),
            "order_size_usdt": round(order_size, 2),
            "pnl_usdt": round(pnl, 4),
            "reason": signal.reason,
        }

        append_paper_trade(trade_log_path, trade)
        risk_manager.register_close_position(symbol, pnl)
        print(f"[INFO] Paper trade saved: {trade}")


if __name__ == "__main__":
    run_paper_bot()
