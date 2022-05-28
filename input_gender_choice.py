# Program :input_gender_choice
# Description : get the gender choice of the user
# Date : 28/05/22
# Author : Christophe Lagaillarde
# Version : 1.0

def input_gender_choice(choice: int) -> str:
    if choice == 1:
        return 'Male'
    if choice == 2:
        return 'Female'
    else:
        raise ValueError