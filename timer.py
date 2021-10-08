import sys
import time


def countdown(time_sec: int):
    print("\n\tTimer Started!")
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print("\tTime Left : {}".format(timeformat), end='\r')
        time.sleep(1)
        time_sec -= 1

    print("\tTime Left : 00:00")
    print("\tWhoops! Time's Up!\n")


if __name__ == "__main__":
    try: sec = int(input("\nEnter Number of Seconds to CountDown : "))
    except ValueError: sys.exit("Input Must Be an Integer!\n")
    countdown(sec)
