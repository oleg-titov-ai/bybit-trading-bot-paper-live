"""Live trading bot skeleton.

This file is intentionally safe by default.
It does not place real orders unless live trading is explicitly enabled locally.

Never commit real API keys, secrets, balances, account IDs, or order IDs.
"""

from __future__ import annotations

import os

from config_loader import get_env_config, load_json_config


class LiveTradingDisabledError(RuntimeError):
    """Raised when live trading is not explicitly enabled."""


def require_live_trading_confirmation() -> None:
    """Block live mode unless multiple local safety flags are enabled."""
    trading_mode = os.getenv("TRADING_MODE", "paper")
    allow_live = os.getenv("ALLOW_LIVE_TRADING", "false").lower()
    confirm_live = os.getenv("CONFIRM_LIVE_TRADING", "false").lower()

    if trading_mode != "live":
        raise LiveTradingDisabledError("TRADING_MODE is not 'live'. Live trading is blocked.")

    if allow_live != "true" or confirm_live != "true":
        raise LiveTradingDisabledError(
            "Live trading requires ALLOW_LIVE_TRADING=true and CONFIRM_LIVE_TRADING=true."
        )

    if not os.getenv("BYBIT_API_KEY") or not os.getenv("BYBIT_API_SECRET"):
        raise LiveTradingDisabledError("BYBIT_API_KEY and BYBIT_API_SECRET must be set locally.")


def run_live_bot() -> None:
    """Safe live bot entry point.

    Real order placement should be implemented and tested locally only.
    """
    env = get_env_config()
    config = load_json_config()

    require_live_trading_confirmation()

    print("[WARNING] Live trading mode enabled locally.")
    print("[WARNING] This demo repository does not include real order execution code.")
    print(f"[INFO] Runtime config: mode={env['trading_mode']} symbols={len(config['symbols'])}")
    print("[INFO] Add exchange-specific order code locally after full paper/testnet testing.")


if __name__ == "__main__":
    run_live_bot()
