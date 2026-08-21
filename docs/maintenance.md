# Maintenance

- 2026-08-19: Treat live-session readiness as short-lived: recheck exchange position/order state and invalidate readiness whenever symbols, leverage, or risk settings change.
- 2026-08-20: Record the last successful paper-mode smoke check in release notes before enabling a new live configuration, without storing balances, keys, or account identifiers.
- 2026-08-20: Keep public configuration examples restricted to non-secret placeholders and testnet-safe values; never include API key fragments, account IDs, or real wallet data.
- 2026-08-20: Keep the documented paper-to-live checklist explicit about confirming symbol, side, quantity, and risk limits immediately before live submission.
- 2026-08-20: Revalidate documented quantity and price precision against current exchange instrument filters after API or dependency updates before relying on live order sizing.
- 2026-08-21: Verify order-validation errors redact request signatures and account-specific fields before they are written to logs or screenshots.
