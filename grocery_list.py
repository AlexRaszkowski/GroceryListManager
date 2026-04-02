grocery = []

print(" 1). Add to your list")
print(" 2). Remove from your list")
print(" 3). View your list")

while True:
    # gets user input on what they would like to do
    choice = input("What would you like to do ").title().strip()

    if choice == "Add" or choice == "1":
        print("This is your current list", grocery)
        adding = input("What would you like to add?: ")
        # adds what the user input aboce to the list named groceries
        grocery.append(adding)
        print(f"Added {adding} to the list.")
        print("This is your list now.", grocery)
       
        # this ask the user if they would like to go back if yes they go back if no the program ends
        go_back = input("Would you like to go back?: ").title().strip()
        if go_back == "Yes":
            continue
        elif go_back == "No":
             break
    
    elif choice == "Remove" or choice == "2":
        print("This is your current list:", grocery)
        removing = input("What would you like to remove:")
        # this removes what the user inputed above in the list named groceries
        grocery.remove(removing)
        print(f"Removed {removing} from the list.")
        
         # this ask the user if they would like to go back if yes they go back if no the program ends
        go_back = input("Would you like to go back?").title().strip()
        if go_back == "Yes":
            continue
        elif go_back == "No":
            break
        
    elif choice == "View" or choice == "3":
        # this just prints the current list
        print("This is your current list", grocery)
       
         # this ask the user if they would like to go back if yes they go back if no the program ends
        go_back = input("Would you like to go back?").title().strip()
        if go_back == "Yes":
            continue
        elif go_back == "No":
            break
        
    

    

