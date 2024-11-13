import imaplib
import email
import getpass


def fetch_email():
    try:
        # Connect to the IMAP server
        M = imaplib.IMAP4_SSL("imap.gmail.com")

        # Get user credentials
        user_email = getpass.getpass("Email: ")
        password = getpass.getpass("Password: ")
        M.login(user_email, password)

        # Select the inbox
        M.select("INBOX")

        # Get the search term from the user
        search_term = input("Enter email message/topic to search for: ")

        # Search for emails containing the search term in the body
        typ, data = M.search(None, f'BODY "{search_term}"')

        if typ == "OK":
            email_ids = data[0].split()  # List of email IDs

            if email_ids:
                email_id = email_ids[0]  # Get the first email ID
                result, email_data = M.fetch(email_id, "(RFC822)")  # Fetch the email

                if result == "OK":
                    for response_part in email_data:
                        if isinstance(response_part, tuple):
                            msg = email.message_from_bytes(
                                response_part[1]
                            )  # Parse the email
                            print("Subject:", msg["subject"])  # Print the subject
                            print("From:", msg["from"])  # Print the sender
                            print("To:", msg["to"])  # Print the recipient
                            print("Date:", msg["date"])  # Print the date
                            print("Body:")

                            # Print the email body
                            if msg.is_multipart():
                                for part in msg.walk():
                                    if part.get_content_type() == "text/plain":
                                        print(part.get_payload(decode=True).decode())
                            else:
                                print(msg.get_payload(decode=True).decode())
                else:
                    print("Failed to fetch the email.")
            else:
                print("No emails found with the given subject.")
        else:
            print(f"Search failed: {typ}")

    except imaplib.IMAP4.error as e:
        print(f"IMAP error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        try:
            M.logout()  # Ensure the connection is closed
        except:
            pass


if __name__ == "__main__":
    fetch_email()
