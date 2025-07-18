import time 
def countdown(second):
    while second > 0:
        print("Time Left: ",second,"second")
        time.sleep(1)
        second -=1
    print("Time's Up !!")

n=int(input("Enter Time for Timer: "))
countdown(n)    