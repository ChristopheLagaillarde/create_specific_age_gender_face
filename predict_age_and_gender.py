# Program : create_specific_age_gender_face
# Description : Allow to choose the generated pic according to gender and age
# Date : 26/05/22
# Author : Christophe Lagaillarde
# Version : 1.0
from sys import argv

from age_and_gender_detection import predict_age_and_gender
from display_image import display_image
from get_generated_face import get_generated_face
from selenium_tools.while_making_automation_headless import while_making_automation_headless
from check_gender_choice import check_gender_choice
from check_age_choice import check_age_choice
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import logging


def create_specific_age_gender_face() -> None:

    try:
        wanted_gender: str = argv[1]
        wanted_age: str = f'({argv[2]}, {argv[3]})'
        obtained_result: str = 'To enter the while loop'
        image_path: str = "images/generated_face.jpg"
        invisible_driver = while_making_automation_headless()

        logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

        check_gender_choice(wanted_gender)

        check_age_choice(argv[2], argv[3])  # Using argv is easier than using wanted_age

        get_generated_face(invisible_driver)

        while not (wanted_gender in obtained_result and wanted_age in obtained_result):
            obtained_result = predict_age_and_gender(image_path)
            logging.info(obtained_result)

            if wanted_gender in obtained_result and wanted_age in obtained_result:

                display_image('Obtained face', image_path)
                reply: str = str(input("Is this image what you are looking for ?(Y/N)\n"))

                if reply == 'Y':
                    break

                else:
                    print('Still searching...')
                    obtained_result = 'reset'
                    get_generated_face(invisible_driver)
                    continue

            get_generated_face(invisible_driver)

        return None

    except NoSuchElementException:
        create_specific_age_gender_face()

    except TimeoutError:
        create_specific_age_gender_face()

    except TimeoutException:
        create_specific_age_gender_face()


create_specific_age_gender_face()