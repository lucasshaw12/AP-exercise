#! python3

import datetime, threading, time

###############################################
# Passing arguments to the Threads 'target' function

# threadObj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep': ' & '})
# threadObj.start()

###############################################
# Launching programs from Python

import subprocess

# Open Atom
# subprocess.Popen('/Applications/Atom.app/Contents/MacOS/Atom')

# Opens a specific file within Atom
# subprocess.Popen(['/Applications/Atom.app/Contents/MacOS/Atom', '/Users/Lucas/Python/AP book exercise/Lists/8ball.py'])

###############################################
# Opening Files with default applications

# fileObj = open('hello.txt', 'w')
# fileObj.write('Hello, World')
# fileObj.close()
# subprocess.Popen(['open', 'hello.txt']) # Opens the appropriate program for .txt files. 
# subprocess.Popen(['open', '/System/Applications/Calculator.app']) 
