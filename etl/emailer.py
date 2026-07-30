import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from dotenv import load_dotenv

load_dotenv()

# ==========================================
# Email Configuration
# ==========================================

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")
TO_ADDRESS = os.getenv("TO_ADDRESS")
EMAIL_SUBJECT = os.getenv("EMAIL_SUBJECT")


def send_email():
    """
    Send ETL completion email with sales chart attached.
    """

    if not SMTP_USER or not SMTP_PASS or not TO_ADDRESS:
        print("❌ Email configuration missing in .env")
        return

    html = """
    <html>
        <body>
            <h2>ETL Pipeline Completed Successfully ✅</h2>

            <p>The ETL pipeline has finished successfully.</p>

            <ul>
                <li>✔ Data Extracted</li>
                <li>✔ Data Transformed</li>
                <li>✔ Uploaded to Azure SQL Database</li>
                <li>✔ Uploaded to Azure Blob Storage</li>
                <li>✔ Visualization Generated</li>
            </ul>

            <p>Sales chart is shown below.</p>

            <img src="cid:sales_chart" width="700">

        </body>
    </html>
    """

    msg = MIMEMultipart("related")
    msg["Subject"] = EMAIL_SUBJECT
    msg["From"] = SMTP_USER
    msg["To"] = TO_ADDRESS

    msg.attach(MIMEText(html, "html"))

    image_path = "reports/sales_chart.png"

    if os.path.exists(image_path):
        with open(image_path, "rb") as image:
            img = MIMEImage(image.read())
            img.add_header("Content-ID", "<sales_chart>")
            img.add_header(
                "Content-Disposition",
                "inline",
                filename="sales_chart.png"
            )
            msg.attach(img)

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg)
        server.quit()

        print("✅ Email sent successfully!")

    except Exception as error:
        print(f"❌ Email Error: {error}")