import time
import sys

def slow_print(text):
    for x in text + '\n':
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.02)
    time.sleep(1)
    
        
def slow_talk(text):
    for x in text + '\n':
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.08)
    time.sleep(1)
        
def scream(text):
    for x in text+ '\n':
        sys.stdout.write(x.upper())
        sys.stdout.flush()
        time.sleep(0.4)
    time.sleep(1)