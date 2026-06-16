import logging
import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()


def send_email(subject, body):
    sender = os.getenv("SMTP_FROM")
    receiver = os.getenv("SMTP_TO")
    host = os.getenv("SMTP_HOST")
    port = int(os.getenv("SMTP_PORT", "587"))
    username = os.getenv("SMTP_USER")
    password = os.getenv("SMTP_PASSWORD")

    if not sender:
        sender = "dry-run@example.com"

    if not receiver:
        receiver = "student@example.com"

    message = MIMEText(body)
    message["Subject"] = subject
    message["From"] = sender
    message["To"] = receiver

    if not host or not username or not password:
        logging.info("Email dry run. SMTP settings are missing.")
        logging.info("To: %s", receiver)
        logging.info("Subject: %s", subject)
        logging.info("Body: %s", body)
        return

    with smtplib.SMTP(host, port) as smtp:
        smtp.starttls()
        smtp.login(username, password)
        smtp.send_message(message)

    logging.info("Email sent to %s", receiver)
