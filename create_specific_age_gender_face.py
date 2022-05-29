# Program : create_specific_age_gender_face
# Description : Allow to choose the generated pic according to gender and age
# Date : 26/05/22
# Author : Christophe Lagaillarde
# Version : 1.0

from age_and_gender_detection import predict_age_and_gender
from get_generated_face import get_generated_face
from selenium_tools.while_making_automation_headless import while_making_automation_headless
from selenium.common.exceptions import NoSuchElementException
from input_gender_choice import input_gender_choice
from input_age_choice import input_age_choice


def create_specific_age_gender_face() -> None:
    try:
        wanted_gender: str = str(input_gender_choice(int(input('Type 1 for Male\n'
                                                               'Type 2 for Female\n'))))

        wanted_age: str = str(input_age_choice(int(input('\n\nType 1 for age inbetween: (0, 2)\n'
                                                         'Type 2 for age inbetween: (4, 6)\n'
                                                         'Type 3 for age inbetween: (8, 12)\n'
                                                         'Type 4 for age inbetween: (15, 20)\n'
                                                         'Type 5 for age inbetween: (25, 32)\n'
                                                         'Type 6 for age inbetween: (38, 43)\n'
                                                         'Type 7 for age inbetween: (48, 53)\n'
                                                         'Type 8 for age inbetween: (60, 100)\n'))))

        obtained_result: str = 'To enter the while loop'
        image_path: str = "images/generated_face.jpg"

        get_generated_face(while_making_automation_headless())

        while not (wanted_gender in obtained_result and wanted_age in obtained_result):
            obtained_result = predict_age_and_gender(image_path)
            print(obtained_result)

            if wanted_gender in obtained_result and wanted_age in obtained_result:
                break

            get_generated_face(while_making_automation_headless())

        return None
    except NoSuchElementException:
        create_specific_age_gender_face()

    except TimeoutError:
        create_specific_age_gender_face()


create_specific_age_gender_face()

