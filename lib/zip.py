import utils
import zipfile
import os
from datetime import datetime
import re
import sys
import py7zr

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
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime('%y_%m_%d_%H_%M_%S')
        self.log_name = f'{os.path.join(os.path.dirname(__file__), "../log/")}{formatted_datetime}.log'
        with open(self.log_name, 'w') as file:
            file.close()

    def display(self) -> str:
        self.write_log(f'Feature in use  :   {self.feature}')
        self.write_log(f'Input folder    :   {self.input_folder}')
        self.write_log(f'Output folder   :   {self.output_folder}')
        self.write_log(f'Format          :   {self.format}')
        self.write_log(f'Filter          :   {self.filter}\n')

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
                self.write_log(f'Zipping {path} to {os.path.join(self.output_folder, name)}.zip')

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
                self.write_log(f'Zipping {path} to {os.path.join(self.output_folder, name)}.7z')

    def write_log(self, str) -> None:
        print(str)
        with open(self.log_name, 'a') as file:
            file.write(str + '\n')
            file.close()

    def execute(self) -> None:
        self.display()
        if utils.is_valid_regex(self.filter) is not None:
            self.write_log(f'Input filter error: {utils.is_valid_regex(self.filter)}')
            sys.exit(1)
        if self.format == ".7z":
            self.format_to_7z()
        elif self.format == ".zip":
            self.format_to_zip()