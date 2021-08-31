
from datetime import datetime

def main():
    now = datetime.now()
    print(now.strftime("%a, %d %b, %y"))
    print(now.strftime("%A, %D %B, %Y"))
    print(now.strftime("local date &time: %c"))
    print(now.strftime("local date: %x"))
    print(now.strftime("local time: %X"))
    print(now.strftime("current time:  %I:%M:%S %p"))
    print(now.strftime("24-hour time:  %H:%M"))
    
main()