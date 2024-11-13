import smtplib
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re


def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None


def send_email():
    smtp_object = None  # Initialize smtp_object to None
    try:
        # Set up the SMTP server
        smtp_object = smtplib.SMTP("smtp.gmail.com", 587)
        smtp_object.ehlo()
        smtp_object.starttls()

        # Get user credentials
        email = getpass.getpass("Email: ")
        password = getpass.getpass("Password: ")
        smtp_object.login(email, password)

        while True:
            to_address = input("Recipient Email: ")
            if not is_valid_email(to_address):
                print("Invalid email address. Please try again.")
                continue

            subject = input("Subject: ")
            message = input("Message: ")

            msg = MIMEMultipart()
            msg["From"] = email
            msg["To"] = to_address
            msg["Subject"] = subject
            msg.attach(MIMEText(message, "plain"))

            smtp_object.send_message(msg)
            print("Email sent successfully!")

            another = (
                input("Do you want to send another email? (Y/N): ").strip().upper()
            )
            if another != "Y":
                break

    except smtplib.SMTPAuthenticationError:
        print("Failed to login. Please check your email and password.")
    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if smtp_object is not None:  # Check if smtp_object is initialized
            smtp_object.quit()


if __name__ == "__main__":
    send_email()
