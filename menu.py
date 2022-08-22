'''
AJ Talbot
11/5/21
'''
# define function show_menu()
def show_menu():
    print("Welcome to the Shape Shifter. Your choices are")
    print("==============================================")
    print("1) Circle Area")
    print("2) Rectangle Area")
    print("3) Triangle Area")
    print("4) Exit")

    
# define function get_choice()
def get_choice():
    choice = input("Enter Your choice:\n")
    while not choice.isnumeric() or int(choice) < 1 or int(choice) >4:
        print("{} is invalid input. Should be a number between 1 and 4 inclusive. Try again".format(choice))
        
    return get_choice
        
     