# ✅ Setup Checklist

Use this checklist to configure the bot safely.

---

## 1. Local Environment

- [ ] Create a local `.env` file from `.env.example`.
- [ ] Keep `.env` outside GitHub.
- [ ] Set `TRADING_MODE=paper` first.
- [ ] Use `BYBIT_TESTNET=true` during testing.
- [ ] Confirm the host clock is synchronized before connecting to the exchange.
- [ ] Verify exchange timestamp errors are handled without retrying orders blindly.

---

## 2. Bybit API

- [ ] Create API credentials locally.
- [ ] Use least-privilege permissions.
- [ ] Avoid withdrawal permissions.
- [ ] Store API key and secret only in local `.env`.
- [ ] Rotate keys if they are exposed.
- [ ] Revoke unused API keys after testing.
- [ ] Recheck API permissions before every live-mode test.
- [ ] Review exchange maintenance notices before scheduling an unattended test run.

---

## 3. Symbol Configuration

- [ ] Copy `config/symbol_config.example.json`.
- [ ] Choose symbols.
- [ ] Set position size.
- [ ] Set risk limits.
- [ ] Disable symbols that are not being tested.
- [ ] Validate the JSON configuration before starting the bot.
- [ ] Record a non-sensitive startup snapshot of enabled symbols and risk limits for troubleshooting.
- [ ] Confirm every configured symbol is currently tradable on the selected Bybit environment.

---

## 4. Paper Trading Test

- [ ] Run paper bot.
- [ ] Confirm WebSocket connection.
- [ ] Confirm signal generation.
- [ ] Confirm risk checks.
- [ ] Confirm demo trade logging.
- [ ] Review `data/paper_trades_demo.csv`.
- [ ] Restart the bot and verify that duplicate demo orders are not created.
- [ ] Stop the bot gracefully and confirm the final state is written before exit.
- [ ] Confirm a second startup reads the previous shutdown state without corruption.
- [ ] Confirm long-running paper logs have a documented rotation or cleanup plan.
- [ ] Confirm log growth cannot exhaust available disk space during an extended paper run.
- [ ] Simulate a brief network interruption and verify safe reconnection behavior.
- [ ] Verify stale market data cannot trigger a new paper or live order.
- [ ] Verify paper mode never calls an authenticated order-submission endpoint.
- [ ] Confirm repeated processing of the same signal cannot create duplicate client order IDs.
- [ ] Confirm logged order timestamps are monotonic and use one documented timezone.
- [ ] Confirm a clean paper run exits with no unresolved local orders.

---

## 5. Live Mode Safety

- [ ] Test on Bybit testnet first.
- [ ] Use tiny order size.
- [ ] Confirm order placement manually.
- [ ] Reconcile each testnet order with the exchange order history before enabling live mode.
- [ ] Require an explicit startup confirmation before enabling live order submission.
- [ ] Verify exit orders are reduce-only and cannot accidentally increase an open position.
- [ ] Confirm an order is treated as accepted only after an exchange acknowledgement is received.
- [ ] Confirm rejected orders are logged clearly and never recorded as open positions.
- [ ] Confirm local open-order state matches the exchange after reconnecting.
- [ ] Confirm terminal order states are not overwritten by delayed WebSocket updates.
- [ ] Reconcile local position state with the exchange before resuming order submission after any restart.
- [ ] Verify partial fills update local quantity and remaining-order state before another order is submitted.
- [ ] Confirm the exchange system status is healthy before switching from paper to live mode.
- [ ] Confirm stop conditions.
- [ ] Confirm daily loss limit.
- [ ] Monitor bot while running.

---

## 6. Before Publishing Publicly

- [ ] Search for API keys.
- [ ] Search for API secrets.
- [ ] Search for real balances.
- [ ] Search for real account IDs.
- [ ] Search for real order IDs.
- [ ] Search for `.env` files.
- [ ] Inspect screenshots manually.
