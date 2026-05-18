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

def extract_content(url):
    print("Extrcting the content from the webpage....")
    cnt = '' # temporary place holder
    cnt += ("<b> Extracted Content : </b> \n" + "<br>" + "_"*50 + "<br>")
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')

    # Find all articles
    articles = soup.find_all("article")

    for i, article in enumerate(articles):

        # headings
        heading_tag = article.find(
            attrs={"data-testid": "Heading"}
            )
        
        # links
        link_tag = article.find(
            attrs= {"data-testid" : "Link"}
            )
        
        link = "https://www.reuters.com" + link_tag['href']

        #timestamps
        time_tag = article.find("time")

        # Manage Missing time stamps
        timestamp = (
            time_tag["datetime"]
            if time_tag and time_tag.has_attr("datetime")
            else "No Timestamp"
            )
        
        cnt += ( f"{i+1} :: {heading_tag.text} <br>"
        f"timestamp :  {time_tag} <br>"
        f"Link :  <a href='{link}'>{link}</a><br>"
        )
    print(f"Articles found: {len(articles)}")
    return(cnt)

cnt = extract_content("https://www.reuters.com/business/")
content += cnt
content += ('<br>---------------------<br>')
content += ('<br><br>End of Message')

