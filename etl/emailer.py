"""
emailer.py

Send ETL completion email with sales chart.
"""

import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

from dotenv import load_dotenv

from etl.logger import logger
from etl.utils import progress, completed

load_dotenv()

# ==========================================================
# EMAIL CONFIGURATION
# ==========================================================

SMTP_SERVER = os.getenv("SMTP_SERVER")

SMTP_PORT = int(
    os.getenv(
        "SMTP_PORT",
        587,
    )
)

SMTP_USER = os.getenv("SMTP_USER")

SMTP_PASS = os.getenv("SMTP_PASS")

TO_ADDRESS = os.getenv("TO_ADDRESS")

EMAIL_SUBJECT = os.getenv("EMAIL_SUBJECT")


# ==========================================================
# LOAD EMAIL TEMPLATE
# ==========================================================

def load_email_template():

    template_path = "templates/email_template.html"

    if not os.path.exists(template_path):

        raise FileNotFoundError(
            "Email template not found."
        )

    with open(
        template_path,
        "r",
        encoding="utf-8",
    ) as file:

        return file.read()


# ==========================================================
# SEND EMAIL
# ==========================================================

def send_email():
    """
    Send ETL completion email with sales chart.
    """

    progress("Preparing email notification...")

    logger.info("Preparing email.")

    if not SMTP_USER or not SMTP_PASS:

        raise ValueError(
            "Email credentials missing."
        )

    html = load_email_template()

    message = MIMEMultipart("related")

    message["Subject"] = EMAIL_SUBJECT

    message["From"] = SMTP_USER

    message["To"] = TO_ADDRESS

    message.attach(
        MIMEText(
            html,
            "html",
        )
    )

    # ------------------------------------------------------
    # ATTACH SALES CHART
    # ------------------------------------------------------

    image_path = "reports/sales_chart.png"

    if os.path.exists(image_path):

        with open(
            image_path,
            "rb",
        ) as image:

            img = MIMEImage(
                image.read()
            )

            img.add_header(
                "Content-ID",
                "<sales_chart>",
            )

            img.add_header(
                "Content-Disposition",
                "inline",
                filename="sales_chart.png",
            )

            message.attach(img)

        logger.info(
            "Sales chart attached."
        )

    else:

        logger.warning(
            "Sales chart not found."
        )

    # ------------------------------------------------------
    # SEND EMAIL
    # ------------------------------------------------------

    try:

        server = smtplib.SMTP(
            SMTP_SERVER,
            SMTP_PORT,
        )

        server.starttls()

        server.login(
            SMTP_USER,
            SMTP_PASS,
        )

        server.send_message(
            message
        )

        server.quit()

        completed(
            "Email sent successfully."
        )

        logger.info(
            "Email sent successfully."
        )

    except Exception as error:

        logger.exception(error)

        print("Email sending failed.")

        raise