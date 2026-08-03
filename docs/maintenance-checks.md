# Maintenance Checks

Before testing:

- Confirm all configured services use the intended test environment.
- Review enabled symbols and documented safety limits.
- Verify reconnects restore state without duplicate actions.
- Ensure example logs and screenshots contain no private identifiers or secrets.
- Confirm startup fails safely when required market metadata is unavailable.
- Verify system clock drift is detected before authenticated requests are enabled.
