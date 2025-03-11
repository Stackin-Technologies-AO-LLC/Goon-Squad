import json
import smtplib

def send_email(content):
    sender_email = "you@example.com"
    receiver_email = "client@example.com"
    subject = "Fresh Data Drop!"
    message = f"Subject: {subject}\n\n{content}"

    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login(sender_email, "password")
        server.sendmail(sender_email, receiver_email, message)
    print("✅ Data sent!")

if __name__ == "__main__":
    with open("sorted_data.json", "r") as file:
        data = json.load(file)
    send_email(json.dumps(data[:5], indent=4))
