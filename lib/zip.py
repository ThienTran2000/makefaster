import zipfile
import os
from datetime import datetime
import re
import sys
import py7zr
sys.path.append('./lib')
from lib import utils

def execute(args):
    obj_run = zip(args)
    obj_run.execute()

class zip:
    def __init__(self, args) -> None:
        self.input_folder = args.input_folder
        self.output_folder = args.output_folder
        self.format = args.format
        self.filter = args.filter
        self.feature = args.subcommand

    def display(self) -> str:
        print(f'Feature in use  :   {self.feature}')
        print(f'Input folder    :   {self.input_folder}')
        print(f'Output folder   :   {self.output_folder}')
        print(f'Format          :   {self.format}')
        print(f'Filter          :   {self.filter}\n')

    def format_to_zip(self) -> None:
        items_to_zip = utils.get_sub_folder_path(self.input_folder)
        for name, path in items_to_zip.items():
            with zipfile.ZipFile(f'{os.path.join(self.output_folder, name)}.zip', 'w') as zipf:
                for root, dirs, files in os.walk(path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, path)
                        if re.match(self.filter, arcname) is not None:
                            zipf.write(file_path, arcname=arcname)
                print(f'Zipping {path} to {os.path.join(self.output_folder, name)}.zip')

    def format_to_7z(self) -> None:
        items_to_zip = utils.get_sub_folder_path(self.input_folder)
        for name, path in items_to_zip.items():
            with py7zr.SevenZipFile(f'{os.path.join(self.output_folder, name)}.7z', 'w') as archive:
                for root, dirs, files in os.walk(path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, path)
                        if re.match(self.filter, arcname) is not None:
                            archive.write(file_path, arcname)
                print(f'Zipping {path} to {os.path.join(self.output_folder, name)}.7z')

    def execute(self) -> None:
        self.display()
        if utils.is_valid_regex(self.filter) is not None:
            print(f'Input filter error: {utils.is_valid_regex(self.filter)}')
            sys.exit(1)
        if self.format == ".7z":
            self.format_to_7z()
        elif self.format == ".zip":
            self.format_to_zip()