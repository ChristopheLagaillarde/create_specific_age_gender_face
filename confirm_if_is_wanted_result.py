# Program : confirm_if_is_wanted_result
# Description : Confirm the
# Date : 02/06/22
# Author : Christophe Lagaillarde
# Version : 1.0

from display_image import display_image
from count_files import count_files

import sys
import shutil


def confirm_if_is_wanted_result(image_path: str) -> None:
    display_image('Obtained face', image_path)
    reply: str = str(input("Is this image what you are looking for ?(Y/N)\n"))

    if reply == 'Y':
        number_of_files: int = count_files('saved')
        shutil.copyfile(image_path, f'saved\\saved_result_{number_of_files}.jpg')
        sys.exit()

    else:
        print('Still searching...')

    return None