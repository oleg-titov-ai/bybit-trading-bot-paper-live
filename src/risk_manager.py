"""Risk management layer for the demo trading bot."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class TradeSignal:
    symbol: str
    side: str
    confidence: float
    order_size_usdt: float
    reason: str


@dataclass
class RiskDecision:
    allowed: bool
    reason: str


class RiskManager:
    """Simple demo risk manager.

    This class is intentionally conservative and designed for paper trading.
    """

    def __init__(
        self,
        max_daily_loss_usdt: float,
        max_open_positions: int,
        allow_live_trading: bool = False,
    ) -> None:
        self.max_daily_loss_usdt = max_daily_loss_usdt
        self.max_open_positions = max_open_positions
        self.allow_live_trading = allow_live_trading
        self.daily_pnl_usdt = 0.0
        self.open_positions: Dict[str, float] = {}

    def check_signal(
        self,
        signal: TradeSignal,
        symbol_config: dict,
        trading_mode: str = "paper",
    ) -> RiskDecision:
        if trading_mode == "live" and not self.allow_live_trading:
            return RiskDecision(False, "Live trading is disabled")

        if not symbol_config.get("enabled", False):
            return RiskDecision(False, "Symbol is disabled")

        min_confidence = float(symbol_config.get("min_signal_confidence", 1.0))
        if signal.confidence < min_confidence:
            return RiskDecision(False, "Signal confidence is too low")

        max_position = float(symbol_config.get("max_position_usdt", 0))
        if signal.order_size_usdt > max_position:
            return RiskDecision(False, "Order size exceeds max position limit")

        if self.daily_pnl_usdt <= -abs(self.max_daily_loss_usdt):
            return RiskDecision(False, "Daily loss limit reached")

        if len(self.open_positions) >= self.max_open_positions:
            return RiskDecision(False, "Max open positions reached")

        return RiskDecision(True, "Risk check passed")

    def register_open_position(self, symbol: str, position_usdt: float) -> None:
        self.open_positions[symbol] = position_usdt

    def register_close_position(self, symbol: str, pnl_usdt: float) -> None:
        self.open_positions.pop(symbol, None)
        self.daily_pnl_usdt += pnl_usdt
