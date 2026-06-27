# Security Policy

## Scope

This repository is a public portfolio and educational project. It must never contain real exchange credentials, private trading logs, wallet data, or production account information.

## Sensitive Data That Must Not Be Committed

- Bybit API keys;
- API secrets;
- `.env` files with real values;
- real account IDs;
- real wallet addresses;
- real balances;
- real order IDs;
- private trading logs;
- screenshots exposing account information.

## Safe Configuration

Use `.env.example` for placeholders only. Keep real credentials in a local `.env` file that is excluded from Git.

## Reporting a Security Issue

If you find a security problem in this repository, open a GitHub issue with a safe description only. Do not include secrets, private logs, screenshots with balances, or real account data.

## Trading Safety

This project does not provide financial advice. Paper trading should remain the default mode. Live mode should require explicit local configuration and careful review.
