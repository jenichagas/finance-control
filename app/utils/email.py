import os
from email.message import EmailMessage
import aiosmtplib

async def send_email(to_email: str, subject: str, html_body: str):
    message = EmailMessage()
    message["From"] = os.getenv("EMAIL_FROM", "orcana@app.com")
    message["To"] = to_email
    message["Subject"] = subject

    message.set_content("Olá! Sua senha foi redefinida com sucesso.")
    message.add_alternative(html_body, subtype="html")

    await aiosmtplib.send(
        message,
        hostname=os.getenv("EMAIL_HOST", "smtp.gmail.com"),
        port=int(os.getenv("EMAIL_PORT", 587)),
        username=os.getenv("EMAIL_USER"),
        password=os.getenv("EMAIL_PASS"),
        start_tls=True
    )
