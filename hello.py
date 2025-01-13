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
elif exampleChoice == 5: 
    ## Displays the formatting ability on a print function AND string manipulations.
    print("Example 5 is now running...")
    userInput4 = input("What is your name? ").strip().title()
    print(f"Hello {userInput4}!")  
elif exampleChoice == 6: 
    ## Displays type casting so compiler recognizes input as an int.
    classSize = int(input("What is the size of your class? "))
    seatsNeeded = (classSize * 2)
    print(f"We will need {seatsNeeded} seats for our trip since every student is bringing a plus one!")
elif exampleChoice == 7: 
    ## Displays type casting + nesting functions in print statement for code efficiency
    print("What is your combined net worth? ")
    print(int(input("Person 1: ")) + int(input("Person 2: ")))
elif exampleChoice == 8: 
    ## Displays type casting + nesting functions in print statement for code efficiency
    print("What is your combined net worth? ")
    print(float(input("Person 1: ")) + float(input("Person 2: ")))
elif exampleChoice == 9: 
    ## Displays type casting + the rounding function + formatting , for american number format
    print("What is your combined net worth? ")
    person1 = float(input("Person 1: "))
    person2 = float(input("Person 2: "))
    combinedNW = round(person1 + person2)
    print(f"The combined net worth rounded is {combinedNW:,}")
elif exampleChoice == 10: 
    ## Displays the creation of basic function using def.
    def helloWorld():
        print("Hello World!")
    print("Example 10 is running...")
    helloWorld()
elif exampleChoice == 11: 
    ## Displays the creation of basic function using def + accepts parameters.
    def helloUser(x):
        print("Hello", x)
    userInput5 = input("What is your name? ")
    helloUser(userInput5)
elif exampleChoice == 12: 
    ## Displays the creation of basic function using def + setting default params.
    def helloUser(x = "world!"):
        print("Hello", x)
    helloUser() ## example of function call w/o args
    userInput5 = input("What is your name? ")
    helloUser(userInput5) ## example of function call w/ args
elif exampleChoice == 13:
    ## Displays the proper function placement in code.
    def main(): 
        name = input("What is your name? ")
        helloUser(name)
    def helloUser(y): 
        print(f"Hello {y}")
    main()
elif exampleChoice == 14:
    ## Displays proper function placement + return keyword used for computation (gain) function 
    def main(): 
        userInput6 = int(input("How much are you wanting to invest this year? "))
        print(f"You can expect your investments to be worth {gain(userInput6)} due to the current 8% returns.")
    def gain(x): 
        return ((x * .08) + x)
    main()
else: 
    print("No example was chosen, goodbye.")