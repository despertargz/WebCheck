__author__ = 'Christopher'

import requests
import yaml
from smtplib import SMTP_SSL
from email.mime.text import MIMEText

config = yaml.load(open("config.yaml", "r"))

def send_email(url):
	email = """From: me
To: you
Subject: Microcenter product is available!

"""

	email += url	

	smtp = SMTP_SSL("smtp.gmail.com", 465, timeout=20)
	smtp.login(config["username"], config["password"])

	smtp.sendmail(config["username"], config["username"], email)
	smtp.quit()


def in_stock(url):
    r = requests.get(url)
    return "'InStock', 'True'" in r.text


if in_stock(config["url"]):
    print("item in stock :)")
    print("sending email...")
    send_email(config["url"])
else:
    print("not in stock yet :(")

print("done!")
