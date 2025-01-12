## This is the first file in the PythonDSA repo.

exampleChoice = int(input("Which example would you like to run? "))
if exampleChoice == 1:
    ## Displays the concatenation of user input to text stream.
    print("Example 1 is now running...")
    userInput = input("Enter your name: ")
    print("Hello " + userInput + "!")
elif exampleChoice == 2:
    ## Displays the manipulation of the print function.
    print("Example 2 is now running...")
    print("Enter your other name: ")
    userInput2 = input()
    print("Hello " , end="")
    print(userInput2, "!")
elif exampleChoice == 3: 
    ## Displays quatations formatting in a text stream.
    print("Example 3 is now running...")
    print("He said \"this will not work\", which made me angry!")
    # OR (Notice the different quotes being used, the compiler will know your intent!)
    print('He said "this will not work", which made me angry!')
elif exampleChoice == 4: 
    ## Displays the formatting ability on a print function.
    print("Example 4 is now running...")
    userInput3 = input("What is your name? ")
    print(f"Hello {userInput3}!")
else: 
    print("No example was chosen, goodbye.")