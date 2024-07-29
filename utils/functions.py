import time

def slow_print(text):
    for x in text:
        time.sleep(0.04)
        print(x,end='')
    print('')
    time.sleep(1)
    
        
def slow_talk(text):
    for x in text:
        time.sleep(0.1)
        print(x,end='')
    print('')
    time.sleep(1)
        
def scream(text):
    for x in text:
        time.sleep(0.4)
        print(x.upper(),end='')
    print('')
    time.sleep(1)