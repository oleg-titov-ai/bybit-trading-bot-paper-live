# Maintenance

- 2026-08-19: Treat live-session readiness as short-lived: recheck exchange position/order state and invalidate readiness whenever symbols, leverage, or risk settings change.
- 2026-08-20: Record the last successful paper-mode smoke check in release notes before enabling a new live configuration, without storing balances, keys, or account identifiers.
- 2026-08-20: Keep public configuration examples restricted to non-secret placeholders and testnet-safe values; never include API key fragments, account IDs, or real wallet data.
- 2026-08-20: Keep the documented paper-to-live checklist explicit about confirming symbol, side, quantity, and risk limits immediately before live submission.
