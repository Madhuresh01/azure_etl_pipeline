"""
logger.py

Centralized logging module for the Azure ETL Pipeline.

Author : Madhuresh
Project : Azure ETL Pipeline
"""

import logging
import os
from datetime import datetime

# ==========================================================
# LOG CONFIGURATION
# ==========================================================

LOG_DIRECTORY = "logs"

os.makedirs(LOG_DIRECTORY, exist_ok=True)

LOG_FILE = os.path.join(
    LOG_DIRECTORY,
    "pipeline.log",
)

logger = logging.getLogger("AzureETLPipeline")

logger.setLevel(logging.INFO)

logger.propagate = False

# ==========================================================
# LOGGER INITIALIZATION
# ==========================================================

if not logger.handlers:

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    file_handler = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8",
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

# ==========================================================
# CONSOLE HELPERS
# ==========================================================

LINE = "=" * 70

SUBLINE = "-" * 70

# ==========================================================
# BANNER
# ==========================================================

def banner():

    print()

    print(LINE)

    print("                     AZURE ETL PIPELINE")

    print(LINE)

    print()

    logger.info(LINE)
    logger.info("Azure ETL Pipeline Started")
    logger.info(LINE)


# ==========================================================
# STAGE HEADER
# ==========================================================

def stage(title):

    print()

    print(SUBLINE)

    print(title)

    print(SUBLINE)

    logger.info(title)


# ==========================================================
# STATUS HELPERS
# ==========================================================

def progress(message):

    print(f"[...] {message}")

    logger.info(message)


def completed(message):

    print(f"[OK] {message}")

    logger.info(message)


def success(message):

    print(f"[SUCCESS] {message}")

    logger.info(message)


def warning(message):

    print(f"[WARNING] {message}")

    logger.warning(message)


def error(message):

    print(f"[ERROR] {message}")

    logger.error(message)


# ==========================================================
# PIPELINE SUMMARY
# ==========================================================

def summary():

    print()

    print(LINE)

    print("Pipeline execution completed.")

    print(LINE)

    logger.info("Pipeline execution completed.")