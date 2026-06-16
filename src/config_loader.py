"""Configuration loader for the demo trading bot.

This module loads JSON symbol configuration and environment variables.
It does not contain real API keys or secrets.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Dict


DEFAULT_CONFIG_PATH = "config/symbol_config.example.json"


class ConfigError(Exception):
    """Raised when configuration is missing or invalid."""


def load_json_config(path: str | None = None) -> Dict[str, Any]:
    """Load symbol configuration from JSON."""
    config_path = Path(path or os.getenv("SYMBOL_CONFIG_PATH", DEFAULT_CONFIG_PATH))

    if not config_path.exists():
        raise ConfigError(f"Config file not found: {config_path}")

    with config_path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if "symbols" not in data or not isinstance(data["symbols"], list):
        raise ConfigError("Config must contain a 'symbols' list")

    return data


def get_env_config() -> Dict[str, str]:
    """Load non-secret runtime options from environment variables.

    API key and secret are intentionally only read locally and should never be
    committed to the repository.
    """
    return {
        "trading_mode": os.getenv("TRADING_MODE", "paper"),
        "bybit_testnet": os.getenv("BYBIT_TESTNET", "true"),
        "trade_log_path": os.getenv("TRADE_LOG_PATH", "data/paper_trades_demo.csv"),
        "log_level": os.getenv("LOG_LEVEL", "INFO"),
    }
