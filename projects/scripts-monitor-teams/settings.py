"""Configuraci?n central del watchdog."""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
LOGS_DIR = BASE_DIR / "Logs"
LOG_FILE = LOGS_DIR / "logs_ejecucion.csv"
CONFIG_FILE = BASE_DIR / "config_scripts.xlsx"

TEAMS_WEBHOOK_URL = os.getenv("TEAMS_WEBHOOK_URL")
TEAMS_WATCHDOG_WEBHOOK_URL = os.getenv("TEAMS_WATCHDOG_WEBHOOK_URL")
