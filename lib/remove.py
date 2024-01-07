import os
import re
import sys
from send2trash import send2trash
import shutil
sys.path.append('./lib')
from lib import utils

def execute(args):
    obj_run = remove(args)
    obj_run.execute()

class remove:
    def __init__(self, args) -> None:
        self.input_folder = args.input_folder
        self.type = args.type
        self.delete_type = args.delete
        self.filter = args.filter
        self.feature = args.subcommand

    def display(self) -> str:
        print(f'Feature in use      :   {self.feature}')
        print(f'Input folder        :   {self.input_folder}')
        print(f'Type                :   {self.type}')
        print(f'Permanently delete  :   {self.delete_type}')
        print(f'Filter              :   {self.filter}\n')

    def find_item_to_remove(self) -> None:
        self.remove_item = []
        self.filtered_list = []
        for root, dirs, files in os.walk(self.input_folder):
            if self.type == 'both' or self.type == 'folder':
                for folder in dirs:
                    folder_path = os.path.join(root, folder)
                    if re.match(self.filter, folder_path) is not None:
                        self.remove_item.append(folder_path)

            if self.type == 'both' or self.type == 'file':
                for file in files:
                    file_path = os.path.join(root, file)
                    if re.match(self.filter, file_path) is not None:
                        self.remove_item.append(file_path)

        for item in self.remove_item:
            flag = False
            for sub in self.remove_item:
                if sub != item and sub in item:
                    flag = True
                    break
            if not flag:
                self.filtered_list.append(item)
        self.filtered_list.sort()

    def user_determine(self) -> None:
        print('All items that will be removed are listed below:')
        for item in self.filtered_list:
            print('--> ' + item)

    def execute(self) -> None:
        self.display()
        if utils.is_valid_regex(self.filter) is not None:
            print(f'Input filter error: {utils.is_valid_regex(self.filter)}')
            sys.exit(1)
        self.find_item_to_remove()
        self.user_determine()
        input = utils.user_input('Do you want to continue? (Yes/No): ', ['Yes', 'No'])

        if self.delete_type:
            if input == 'yes':
                for item in self.filtered_list:
                    if os.path.isdir(item):
                        try:
                            print(f'Removing {item}')
                            shutil.rmtree(item)
                        except Exception as e:
                            print(f"Error removing folder '{item}': {e}")

                    if os.path.isfile(item):
                        try:
                            print(f'Removing {item}')
                            os.remove(item)
                        except Exception as e:
                            print(f"Error removing folder '{item}': {e}")
            else:
                sys.exit()
        else:
            for item in self.filtered_list:
                try:
                    print(f'Removing {item}')
                    send2trash(item)
                except Exception as e:
                    print(f"Error removing folder '{item}': {e}")