import smtplib
import ssl
from email.message import EmailMessage
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(file_link, location):
    # Define the path to your config file
    config_file_path = 'apps_pw_config.json'

    # Load the config from the JSON file
    try:
        with open(config_file_path, 'r') as config_file:
            config = json.load(config_file)
        # Retrieve the password from the config
        email_password = config.get('email_password')
    except FileNotFoundError:
        print(f"Config file not found: {config_file_path}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in config file: {e}")

    # Define email sender and receiver
    email_sender = 'tehxueer29@gmail.com'
    email_receiver = 'iotonlyg2.6@gmail.com'

    # Set the subject and body of the email
    subject = 'Alert: Collision detected'
    html = f"""
    <html>
                <head>
                    <title></title>
                    <link href="https://svc.webspellchecker.net/spellcheck31/lf/scayt3/ckscayt/css/wsc.css" rel="stylesheet" type="text/css" />
                </head>
                <body>Dear Sir/Mdm,<br />
                    <br />
                    There has been a collision of overhanging branches at location <strong>{location}</strong>. Please take the following actions&nbsp;as soon as possible to prevent incidents from happening. Thank you.<br />
                    &nbsp;
                    <hr /><br />
                    <strong>[For Action] </strong>Click on this link to assess the situation: <a href="{file_link}">{file_link}</a>.
                    <br />
                    <br />
                    <strong>[For Action] </strong>Contact NParks&nbsp;to remove the overhanging branches.<br />
                    Contact Number:&nbsp;1800-476-1600<br />
                    Email: www.nparks.gov.sg/feedback<br />
                    <br />
                    Best Regards,<br />
                    BranchWatch Team
                    <div>
                    <div>&nbsp;</div>

                    <div>&nbsp;</div>
                    </div>
                </body>
                </html>
    """

    em = MIMEMultipart()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    html_text = MIMEText(html, 'html')
    em.attach(html_text)
    # em.set_content(body)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
