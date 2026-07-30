import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from dotenv import load_dotenv

load_dotenv()


def send_email():

    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = int(os.getenv("SMTP_PORT"))
    smtp_user = os.getenv("SMTP_USER")
    smtp_pass = os.getenv("SMTP_PASS")
    to_address = os.getenv("TO_ADDRESS")

    if not smtp_user or not smtp_pass or not to_address:
        print("❌ Email credentials missing in .env")
        return

    subject = "ETL Pipeline Report"

    html = """
    <html>
        <body>
            <h2>ETL Pipeline Completed Successfully ✅</h2>

            <p>The ETL pipeline has finished successfully.</p>

            <ul>
                <li>✔ Data Extracted</li>
                <li>✔ Data Transformed</li>
                <li>✔ Uploaded to Azure SQL</li>
                <li>✔ Visualization Generated</li>
            </ul>

            <p>Sales chart is attached below.</p>

            <img src="cid:sales_chart" width="700">

        </body>
    </html>
    """

    msg = MIMEMultipart("related")
    msg["Subject"] = subject
    msg["From"] = smtp_user
    msg["To"] = to_address

    msg.attach(MIMEText(html, "html"))

    image_path = "reports/sales_chart.png"

    if os.path.exists(image_path):
        with open(image_path, "rb") as f:
            img = MIMEImage(f.read())
            img.add_header("Content-ID", "<sales_chart>")
            img.add_header(
                "Content-Disposition",
                "inline",
                filename="sales_chart.png"
            )
            msg.attach(img)

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.send_message(msg)
        server.quit()

        print("✅ Email sent successfully!")

    except Exception as e:
        print("❌ Email Error:", e)