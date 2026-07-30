"""
utils.py

Utility helpers used throughout the Azure ETL Pipeline.
"""

import time

from etl.logger import logger

# ==========================================================
# RETRY MECHANISM
# ==========================================================

def retry(function, retries=3, delay=5):
    """
    Execute a function with automatic retry support.
    """

    last_exception = None

    for attempt in range(1, retries + 1):

        try:

            logger.info(
                "Attempt %d of %d",
                attempt,
                retries,
            )

            return function()

        except Exception as error:

            last_exception = error

            logger.warning(
                "Attempt %d failed : %s",
                attempt,
                error,
            )

            print(
                f"[Retry {attempt}/{retries}] "
                f"Retrying in {delay} seconds..."
            )

            if attempt < retries:

                time.sleep(delay)

    logger.error("Retry limit exceeded.")

    raise last_exception


# ==========================================================
# PROGRESS MESSAGE
# ==========================================================

def progress(message):
    """
    Display pipeline progress.
    """

    print(f"[...] {message}")

    logger.info(message)


# ==========================================================
# COMPLETED MESSAGE
# ==========================================================

def completed(message):
    """
    Display successful completion message.
    """

    print(f"[OK] {message}")

    logger.info(message)


# ==========================================================
# EXECUTION TIME
# ==========================================================

def execution_time(start_time):
    """
    Return total execution time.
    """

    return round(
        time.time() - start_time,
        2,
    )


# ==========================================================
# WAIT MESSAGE
# ==========================================================

def wait(seconds):
    """
    Pause execution.
    """

    logger.info(
        "Waiting for %d seconds.",
        seconds,
    )

    time.sleep(seconds)


# ==========================================================
# DIVIDER
# ==========================================================

def divider():

    print("=" * 70)