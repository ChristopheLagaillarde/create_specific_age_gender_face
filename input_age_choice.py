# Program :input_age_choice
# Description : get the age choice of the user
# Date : 28/05/22
# Author : Christophe Lagaillarde
# Version : 1.0

def input_age_choice(choice: int) -> str:
    if choice == 1:
        return '(0, 2)'

    if choice == 2:
        return '(4, 6)'

    if choice == 3:
        return '(8, 12)'

    if choice == 4:
        return '(15, 20)'

    if choice == 5:
        return '(25, 32)'

    if choice == 6:
        return '(38, 43)'

    if choice == 7:
        return '(48, 53)'

    if choice == 8:
        return '(60, 100)'

    else:
        raise ValueError