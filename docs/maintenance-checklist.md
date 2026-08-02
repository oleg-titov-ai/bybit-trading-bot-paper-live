# Maintenance checklist

Before any live-mode session, verify paper mode is the default, symbol configuration is intentional, and published logs contain no account identifiers.

After a controlled shutdown, confirm open-position state and the last processed timestamp are persisted before restarting.

Run a paper-mode smoke test after dependency updates and confirm order sizing, precision, and rate-limit handling remain unchanged.

Verify startup fails closed when required live-trading credentials are missing or still set to placeholders.

Confirm the host clock is synchronized before testing timestamp-sensitive exchange requests.

Verify stale market data is rejected before order calculations so delayed feeds cannot trigger unintended decisions.

Confirm paper and live modes use separate state files or databases so test positions cannot leak into a live session.

Validate the resolved configuration in a dry run before live mode, showing symbols and limits while redacting all credentials.

Review one recent log sample to confirm API keys, signatures, and account identifiers are consistently redacted.

Confirm controlled shutdown logs clearly state whether state persistence completed successfully before the process exits.

Verify paper-mode startup rejects unsupported symbols before any market-data subscription is opened.

Confirm reconnect logic restores subscriptions without submitting duplicate orders from replayed events.

Verify configured quantity and price precision match current exchange metadata before enabling order submission.