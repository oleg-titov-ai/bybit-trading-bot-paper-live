"""Demo strategy module.

The strategy returns sample signals from market data.
Replace this with your own tested logic locally.
"""

from __future__ import annotations

from typing import Optional

from risk_manager import TradeSignal


def generate_demo_signal(symbol: str, last_price: float, order_size_usdt: float) -> Optional[TradeSignal]:
    """Generate a deterministic demo signal.

    This is not a profitable strategy. It exists only to demonstrate the bot
    architecture and data flow.
    """
    if last_price <= 0:
        return None

    # Demo rule only: alternate direction based on integer price parity.
    side = "Buy" if int(last_price) % 2 == 0 else "Sell"

    return TradeSignal(
        symbol=symbol,
        side=side,
        confidence=0.75,
        order_size_usdt=order_size_usdt,
        reason="demo_signal",
    )
