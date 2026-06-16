# ✅ Setup Checklist

Use this checklist to configure the bot safely.

---

## 1. Local Environment

- [ ] Create a local `.env` file from `.env.example`.
- [ ] Keep `.env` outside GitHub.
- [ ] Set `TRADING_MODE=paper` first.
- [ ] Use `BYBIT_TESTNET=true` during testing.

---

## 2. Bybit API

- [ ] Create API credentials locally.
- [ ] Use least-privilege permissions.
- [ ] Avoid withdrawal permissions.
- [ ] Store API key and secret only in local `.env`.
- [ ] Rotate keys if they are exposed.

---

## 3. Symbol Configuration

- [ ] Copy `config/symbol_config.example.json`.
- [ ] Choose symbols.
- [ ] Set position size.
- [ ] Set risk limits.
- [ ] Disable symbols that are not being tested.

---

## 4. Paper Trading Test

- [ ] Run paper bot.
- [ ] Confirm WebSocket connection.
- [ ] Confirm signal generation.
- [ ] Confirm risk checks.
- [ ] Confirm demo trade logging.
- [ ] Review `data/paper_trades_demo.csv`.

---

## 5. Live Mode Safety

- [ ] Test on Bybit testnet first.
- [ ] Use tiny order size.
- [ ] Confirm order placement manually.
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
