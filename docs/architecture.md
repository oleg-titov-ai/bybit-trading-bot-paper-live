# 🧩 Architecture

The bot is structured around a clear separation of market data, strategy, risk management, execution, and logging.

---

## Main Flow

```text
Bybit WebSocket Market Data
        ↓
Market Data Handler
        ↓
Strategy Logic
        ↓
Risk Manager
        ↓
Order Executor
        ↓
Paper Trading / Live Trading
        ↓
Trade Logger
```

---

## Components

### Market Data Handler

Receives live market updates from Bybit WebSocket streams.

Typical data:

- symbol;
- price;
- timestamp;
- candle / ticker updates;
- volume;
- bid / ask data if needed.

---

### Strategy Logic

Generates potential trade signals from market data.

The strategy layer should not place orders directly. It only returns a structured signal such as:

```json
{
  "symbol": "BTCUSDT",
  "side": "Buy",
  "confidence": 0.75,
  "reason": "demo_signal"
}
```

---

### Risk Manager

Checks whether a signal is allowed.

Example checks:

- maximum position size;
- maximum daily loss;
- maximum number of open positions;
- symbol enabled / disabled;
- paper trading vs live mode;
- minimum signal confidence.

---

### Order Executor

Executes approved signals.

In paper mode, it simulates an order.

In live mode, it can send an order to Bybit using locally configured API credentials.

---

### Trade Logger

Saves trade events to CSV or another local storage format.

Public demo logs must contain fake or paper trading data only.
