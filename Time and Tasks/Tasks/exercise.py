#! python3

import datetime, threading, time

###############################################
# Passing arguments to the Threads 'target' function

threadObj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep': ' & '})
threadObj.start()