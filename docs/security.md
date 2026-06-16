# 🔐 Security Notes

This repository is a public-safe demo / portfolio version of a trading bot.

It must never contain real exchange credentials, account data, balances, private trading logs, or wallet information.

---

## 🚫 Never Commit

Do not commit:

- Bybit API key
- Bybit API secret
- real `.env` files
- real account IDs
- real balances
- real wallet data
- real order IDs
- real position IDs
- real trade logs
- private strategy parameters that should not be public
- production server IPs
- private webhook URLs

---

## ✅ Safe Public Placeholders

Use placeholders like:

```text
DEMO_BYBIT_API_KEY
DEMO_BYBIT_API_SECRET
BYBIT_TESTNET=true
TRADING_MODE=paper
CHANGE_ME_LOCALLY
```

---

## ✅ Safe Public Data

Safe to publish:

- paper trading demo logs;
- fake trade examples;
- example symbol config;
- risk management documentation;
- screenshots with balances hidden;
- screenshots from testnet or demo mode.

---

## 🧪 Before Making Repository Public

Search for:

```text
api_key
api_secret
secret
password
token
bybit
balance
wallet
account
order_id
position_id
private
.env
```

Also manually inspect all screenshots before uploading them.

---

## 🧯 If a Secret Was Committed

If a real API key or secret was committed:

1. Revoke it immediately in Bybit.
2. Create a new API key locally.
3. Remove the secret from repository files.
4. Treat the old key as compromised.

Deleting the file from GitHub is not enough if the key was already committed.
