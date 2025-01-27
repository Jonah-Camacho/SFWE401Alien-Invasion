import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

scope = ['https://www.googleapis.com/auth/spreadsheets']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Pantry Inventory').sheet1

inventory = sheet.get_all_records()

def send_email(to_email, subject, body):
    from_email = 'your_email@gmial.com'
    password = 'your_password'

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

today = datetime.date.today()
expiring_items = []

for item in inventory:
    expiration_date = datetime.datetime.strptime(item['Expiration Date'], '%m/%d/%Y').date()
    days_until_expiration = (expiration_date - today).days
    if days_until_expiration <= 7:
        expiring_items.append(item)

if expiring_items:
    email_body = "Expiring Items:\n"
    for item in expiring_items:
        email_body += f"{item['Item']} - Expiration on {item['Expiration Date']}\n"

    send_email('reciept_email@example.com', 'Expiring Items Notification', email_body)