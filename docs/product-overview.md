# Product Overview

## Purpose

This project demonstrates how to design a cryptocurrency trading bot with a strong emphasis on safety, observability, and controlled execution rather than on profit claims.

The system is structured around separate layers for market data, strategy logic, risk management, order execution, and trade logging.

## Main Use Cases

### 1. Paper Trading

```text
Bybit market data
        ↓
strategy signal
        ↓
risk validation
        ↓
simulated order
        ↓
trade log and monitoring alert
```

Paper mode allows strategy behavior and risk limits to be tested without sending real orders.

### 2. Optional Live Trading

```text
validated strategy signal
        ↓
risk manager approval
        ↓
live executor
        ↓
exchange response
        ↓
logging and alerting
```

Live mode should only be enabled after local testing, configuration review, and verification of all safety limits.

## Core Modules

- WebSocket market data consumer;
- multi-symbol configuration;
- strategy engine;
- risk manager;
- paper executor;
- optional live executor;
- CSV trade logging;
- terminal monitoring;
- Telegram-style alert flow;
- environment-based secret management.

## Risk Controls

Recommended controls include:

- maximum position size;
- maximum number of simultaneous positions;
- stop-loss rules;
- daily loss limit;
- symbol allowlist;
- cooldown after repeated errors;
- paper mode as the default;
- explicit live-mode confirmation.

## Portfolio Value

The repository demonstrates:

- Python project architecture;
- asynchronous market-data handling;
- configuration-driven automation;
- separation of strategy and execution;
- risk-aware system design;
- logging and monitoring;
- secure handling of API credentials.

## Next Development Steps

1. add automated unit tests for risk rules;
2. add backtesting with reproducible datasets;
3. add structured event logging;
4. add idempotent order handling;
5. add metrics for latency, errors, and strategy activity;
6. add a safer release checklist for live mode.

## Disclaimer

This repository is for educational and portfolio purposes only. It does not provide financial advice and does not guarantee profit.
