# Maintenance checklist

Before any live-mode session, verify paper mode is the default, symbol configuration is intentional, and published logs contain no account identifiers.

After a controlled shutdown, confirm open-position state and the last processed timestamp are persisted before restarting.

Run a paper-mode smoke test after dependency updates and confirm order sizing, precision, and rate-limit handling remain unchanged.

Verify startup fails closed when required live-trading credentials are missing or still set to placeholders.

Confirm the host clock is synchronized before testing timestamp-sensitive exchange requests.

Verify stale market data is rejected before order calculations so delayed feeds cannot trigger unintended decisions.

Confirm paper and live modes use separate state files or databases so test positions cannot leak into a live session.

Validate the resolved configuration in a dry run before live mode, showing symbols and limits while redacting all credentials.