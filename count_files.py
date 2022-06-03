# Program : count_file
# Description : count the number of file
# Date : 02/06/22
# Author : Christophe Lagaillarde
# Version : 1.0

import os


def count_files(dir_name: str) -> int:
    number_of_files: int = 0

    for path in os.listdir(dir_name):
        if os.path.isfile(os.path.join(dir_name, path)):
            number_of_files += 1

    return number_of_files
