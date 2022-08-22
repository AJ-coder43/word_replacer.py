# import the module
import menu

menu.show_menu()
menu.get_choice()

# write a while loop to call the function until 4 is entered
while 1 <= int(choice) < 4:
    print("You chose {}. Excellent Choice\n".format(choice))
    menu.show_menu()
    choice = menu.get_choice()
if int(choice) == 4:
        print("You chose to Exit . . . Buh Bye")
        quit()
    
    
        
# call the function