# Web scrapping with python

#----------------------------------------------#
# Scrape financial/business news website
# Extract:
    # headlines
    # timestamps
    # categories
    # links
# Filter based on keywords
# Generate clean HTML email report
# Automatically send email daily

#---------------------------------------------------#

import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import datetime

now = datetime.datetime.now()

# content body placeholder
content = ''
