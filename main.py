import sys
import pyautogui
import argparse
from datetime import datetime


# validate the given argument to ensure it is an integer.
def numeric_val(duration):
    if not duration.isnumeric():
        raise argparse.ArgumentTypeError('Input Error. Expected a numeric value for duration. Found "{}"'
                                         .format(duration))
    try:
        return int(duration)
    except Exception as e:
        raise argparse.ArgumentTypeError("""Couldn't parse the value passed into integer. Value passed is "{}" """
                                         .format(duration))


# convert seconds to day, hour, minutes and seconds
def get_formatted_time(duration):
    days = int(duration // (24 * 3600))
    duration = duration % (24 * 3600)
    hours = int(duration // 3600)
    duration %= 3600
    minutes = int(duration // 60)
    duration %= 60
    seconds = duration

    return f"{days} Day(s) {hours} Hours(s) {minutes} minute(s) and {seconds:.2f} seconds(s)"


# brains of the operation. after every interval seconds, it performs an ALT-TAB operation to keep the machine awake
# for duration specified.
def keep_awake(duration, interval):
    print('Keeping your computer awake for {}'.format(get_formatted_time(duration)))
    start_time = datetime.now()
    try:
        while True:
            if (datetime.now() - start_time).total_seconds() > duration:
                end_time = datetime.now()
                print(f'System has been awake since {start_time} until {end_time} for a total duration of {get_formatted_time((end_time - start_time).total_seconds())}')
                sys.exit(0)
            pyautogui.sleep(interval)
            pyautogui.hotkey('altleft', 'tab')
            current_time = datetime.now()
            print(f'Operation performed at {current_time}. Duration elapsed is {get_formatted_time((current_time - start_time).total_seconds())}')
    except Exception as e:
        print("Unable to keep the system awake")
        print(e)
        pyautogui.alert('KeepAwake Stopped. Please check the console output...')
        sys.exit(2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--duration', default=3600, help='Duration to be awake in seconds', type=numeric_val)
    parser.add_argument('-i', '--interval', default=60, help='Interval at which operation to be performed', type=numeric_val)
    args = parser.parse_args()

    keep_awake(args.duration, args.interval)
