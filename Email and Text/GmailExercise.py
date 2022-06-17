import ezgmail, os

os.chdir(r'/Users/Lucas/Python/AP book exercise/Email and Text/')
ezgmail.init()
print(ezgmail.EMAIL_ADDRESS) # Shows which email address token.json is configured to use. Only works after .init()

#######################################
# Sending Email from a Gmail account

# ezgmail.send('lucaspythonprojects@gmail.com', 'Subject Line', 'Body of the email', ['attachment1.png', \
# 	'attachment2.png'], cc='lucaspythonprojects@gmail.com', bcc='lucaspythonprojects@gmail.com')

