#! python3

import smtplib 

# smtpObj = smtplib.SMTP('smtp.google.com', 587)
smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
print(type(smtpObj))
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('lucaspythonprojects@gmail.com', 'f0@5iXRM2$mz') # once completed, use input() to enter the password value
