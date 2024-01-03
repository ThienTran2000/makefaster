import argparse
import sys
from datetime import datetime

sys.path.append('lib')

from lib import zip, checkin_checkout

def main():
    parser = argparse.ArgumentParser(description='This package to make your things are faster.')

    subparsers = parser.add_subparsers(dest='subcommand', help='Available features:')

    # Add arguments for zip feature
    parser_zip = subparsers.add_parser('zip', help='Zip the folder')
    parser_zip.add_argument('--input_folder', '-i', type=str, default='./', help='The path of folder contain the specific folders to zip')
    parser_zip.add_argument('--output_folder', '-o', type=str, default='./', help='The path of folder as the output path of package')
    parser_zip.add_argument('--format', '-f', type=str, choices=['.7z', '.zip'], default='.7z', help='The format to zip: 7z, zip')
    parser_zip.add_argument('--filter', type=str, default='.*', help='The filter as a string regular expression')
    parser_zip.set_defaults(func=zip.execute)

    # Add arguments for checkin_checkout feature
    current_time = datetime.now().hour
    parser_zip = subparsers.add_parser('checkin_checkout', help='Check-in Check-out automatically')
    parser_zip.add_argument('--hour_in', '-hi', type=int, default=8, help='The hour to check-in')
    parser_zip.add_argument('--minute_in', '-mi', type=int, default=30, help='The minute to check-in')
    parser_zip.add_argument('--hour_out', '-ho', type=int, default=datetime.now().hour, help='The hour to check-out')
    parser_zip.add_argument('--minute_out', '-mo', type=int, default=datetime.now().minute + 1, help='The minute to check-out')
    parser_zip.set_defaults(func=checkin_checkout.execute)

    parser.add_argument('-v', '--version', action='version', version='%(prog)s V1.00')

    args = parser.parse_args()

    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()