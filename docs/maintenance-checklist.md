# Maintenance checklist

Before any live-mode session, verify paper mode is the default, symbol configuration is intentional, and published logs contain no account identifiers.

After a controlled shutdown, confirm open-position state and the last processed timestamp are persisted before restarting.

Run a paper-mode smoke test after dependency updates and confirm order sizing, precision, and rate-limit handling remain unchanged.