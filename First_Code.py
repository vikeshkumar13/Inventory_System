from Second_Code import milk_calculation
from Second_Code import Inventory, display_milk, display_inventory,delete_row


def main_function():
    while True:
        print('*********WELCOME*************')
        print('_____________________________')
        print('1->CALCULATE MILK FOR A MONTH ->')
        print('2->ENTER INVENTORY DETAILS ->')
        print('3->DISPLAY YOUR MILK DATABASE')
        print('4->DISPLAY YOUR INVENTORY DATABASE')
        print('5->DELETE YOUR DATA FROM THE DATABASE')
        print('6->TO EXIT FROM THIS PROGRAM')
        print('______________________________')
        print('Choose->')
        try:
            choose = int(input())
            if choose == 1:
                milk_calculation()
            elif choose == 2:
                Inventory()
            elif choose == 3:
                display_milk()
            elif choose == 4:
                display_inventory()
            elif choose == 5:
                delete_row()
            elif choose == 6:
                print('Thank You')
                break
            else:
                print('invalid input')
        except Exception as e:
            print('Invalid input please try again', e)

def normal_user():
    while True:
        print('***********WELCOME*************')
        print('_____________________________')
        print('1->CALCULATE MILK FOR A MONTH ->')
        print('2->ENTER INVENTORY DETAILS ->')
        print('3->TO EXIT FROM THIS PROGRAM')
        print('______________________________')
        print('Choose->')
        try:
            choose = int(input())
            if choose == 1:
                milk_calculation()
            elif choose == 2:
                Inventory()
            elif choose == 3:
                print('Thank You')
                break
            else:
                print('invalid input')
        except Exception as e:
            print('Invalid input please try again', e)