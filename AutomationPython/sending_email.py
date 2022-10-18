import requests #http requests
from bs4 import BeautifulSoup  #Web Scrapping
import smtplib #Send the email
from email.mime.multipart import MIMEMultipart #Email body
from email.mime.text import MIMEText
import datetime #System date and time manipulation

now = datetime.datetime.now()

#---Email content placeholder----
content = ''

#---Extracting Hacker News Stories---

def extract_news(url):
    print('Extracting Hacker News Stories...')
    cnt = ''
    cnt +=('<b> HN Top Stories:</b>\n'+'<br>'+'-'*50+'<br>')
    response=requests.get(url)
    content=response.content
    soup= BeautifulSoup(content, 'html.parser')

    for i,tag in enumerate(soup.find_all('td',attrs={'class':'title','valign':''})):
        cnt +=((str(i+1)+'::'+tag.text+"\n"+'<br>')if tag.text!='More' else '')
    return(cnt)

cnt=extract_news('https://news.ycombinator.com/')
content+=cnt
content+=('<br>------<br>')
content+=('<br><br>End of Message')

#lets send the email
print('Composing Email')

#Update your Email details
SERVER = 'smtp.gmail.com' #your smtp server
PORT = 587 #Your port number
FROM ='poorvi@gmail.com' #Your from email id
TO = 'poorvi@gmail.com' #Your to email ids  #It can be list
PASS='****************'  #App Password

msg = MIMEMultipart()

msg['Subject'] = 'Top News Stories HN[Automated Email]'+' '+str(now.day)+'-'+str(now.month)+'-'+str(now.year)
msg['From']=FROM
msg['To']=TO
msg.attach(MIMEText(content,'html'))

print('Initiating Server...')

server=smtplib.SMTP(SERVER,PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM, PASS)
server.sendmail(FROM,  TO, msg.as_string())

print('email sent...')

server.quit()

