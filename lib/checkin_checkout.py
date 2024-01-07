import pyautogui
import sys
sys.path.append('./lib')
from lib import utils

def execute(args):
    pyautogui.FAILSAFE = False
    obj_run = checkin_checkout(args)
    obj_run.execute()

class checkin_checkout:
    def __init__(self, args) -> None:
        self.hour_in = args.hour_in
        self.minute_in = args.minute_in
        self.hour_out = args.hour_out
        self.minute_out = args.minute_out
        self.feature = args.subcommand

    def display(self) -> str:
        print(f'Feature in use      :   {self.feature}')
        print(f'Hour in             :   {self.hour_in}')
        print(f'Minute in           :   {self.minute_in}')
        print(f'Hour out            :   {self.hour_out}')
        print(f'Minute out          :   {self.minute_out}\n')

    def execute(self) -> None:
        self.display()
        try:
            my_bv = 'C:\\Program Files\\MyBV\\MyBV.exe'
            status_out = False
            utils.close_app('MyBv')
            while True:
                sys.stdout.flush()
                is_time_in = utils.check_time(self.hour_in, self.minute_in)
                if is_time_in:
                    utils.open_app(my_bv)
                    print('Check-in is successfully.')
                    break
                if status_out == False:
                    is_time_out = utils.check_time(self.hour_out, self.minute_out)
                    if is_time_out:
                        utils.open_app(my_bv)
                        utils.time.sleep(5)
                        print('Check-out is successfully.')
                        utils.close_app('MyBv')
                        status_out = True
                utils.dont_sleep()
        except KeyboardInterrupt:
            pass