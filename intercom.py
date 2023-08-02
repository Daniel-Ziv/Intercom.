
#downloading the libs needed for the code to work.
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from scripts.datagatherer import datagatherer
from scripts.driversetup import setup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
"""
names interpretation:
csat - costumer
frt - first response time
ttc - time to close
"""

#setting up the driver source(it will always in sync with and current chrome version)
driver = webdriver.Chrome(ChromeDriverManager().install())

#setup
setup(driver)

#setup complete - starts with data gathering
datagatherer(driver)

#Sending the email with the CSV details
# Email details
from_address = "mail@gmail.com"  # Replace with your Gmail address
to_address = "mail@gmail.com"
subject = "This is the sub "
body = "The body of the email"

# Create the email message
msg = MIMEMultipart()
msg['From'] = from_address
msg['To'] = to_address
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Attach the CSV file
filename = "datanalysis.csv"
attachment = open('csv_data/userdata.csv', "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

# Add the attachment to the email
msg.attach(part)

# Connect to the email server and send the email
server = smtplib.SMTP('smtp.gmail.com', 587)  # Use Gmail's SMTP server
server.starttls()  # Use Transport Layer Security (TLS)
server.login(from_address, "password")  # Replace with your Gmail password
server.sendmail(from_address, to_address, msg.as_string())
server.quit()
