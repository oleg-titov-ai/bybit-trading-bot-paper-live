# Maintenance Checks

Before testing:

- Confirm all configured services use the intended test environment.
- Review enabled symbols and documented safety limits.
- Verify reconnects restore state without duplicate actions.
- Ensure example logs and screenshots contain no private identifiers or secrets.
- Confirm startup fails safely when required market metadata is unavailable.
- Verify system clock drift is detected before authenticated requests are enabled.
- Confirm a controlled shutdown persists only the minimum state needed for a safe restart.
- Recheck configured order limits after any symbol or account-mode change.
- Validate the configuration file before startup and reject unknown or misspelled keys.
