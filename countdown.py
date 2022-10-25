import Time

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 50)
        timeformat = '{:02d}:{:02d}'.format(mins, sec)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    print("stop")

countdown(5)
