from matplotlib import pyplot as plt


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
elif exampleChoice == 15:
    ## Data scientists in the company 
    users = [
        {"id": 0, "name": "Larry"}, 
        {"id": 1, "name": "Della"}, 
        {"id": 2, "name": "Gustavo"}, 
        {"id": 3, "name": "Stephanie"}, 
        {"id": 4, "name": "Chris"}, 
        {"id": 5, "name": "Dawne"}, 
        {"id": 6, "name": "Olivia"}, 
        {"id": 7, "name": "Isabel"}, 
        {"id": 8, "name": "Maria"}, 
        {"id": 9, "name": "Zayra"}]

    ## Set of friendhips across the company of Data scientists
    friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                   (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]
    
    ## test data
    years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
    gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
    plt.plot(years, gdp, color="green", marker='o', linestyle='solid')
    plt.title("Test graph")
    plt.ylabel("Billions of $")
    plt.show()
elif exampleChoice == 16: 
    ## Displays OR logical operator + does not equal (negation).
    def main(): 
        userInput6 = int(input("What is the X value? "))
        userInput7 = int(input("What is the Y value? "))
        ## OR
        if userInput6 > userInput7 or userInput7 > userInput6: 
            print("One is larger than the other")
        else:
            print("They are equal") 
        ## Does not equal (Simplified and efficient logic)
        if userInput6 != userInput7: 
            print("Values are not equal")
        else: 
            print("Values are equal")
    main()
elif exampleChoice == 17: 
    ## Displays AND logical operator for grade calculator
    # + further enhanced version for code efficiency.
    def main(): 
        score = int(input("Provide your score: "))
        machine = input("Choose which version to run: V1 or V2 ")
        
        if machine == "V1":
            if score >= 90 and score <= 100: 
                print("You recieved a letter grade: A")
            elif score >= 80 and score < 90: 
                print("You recieved a letter grade: B")
            elif score >= 70 and score < 80: 
                print("You recieved a letter grade: C")
            elif score >= 60 and score < 70: 
                print("You recieved a letter grade: D")
            elif score >= 0 and score < 60: 
                print("You recieved a letter grade: F")
            else: 
                print("The score provided is not in range. Try Again")
        elif machine == "V2": 
            print("Enhanced Grade calculator is now running...")
            if score >= 90: 
                print("You recieved a letter grade: A")
            elif score >= 80: 
                print("You recieved a letter grade: B")
            elif score >= 70: 
                print("You recieved a letter grade: C")
            elif score >= 60: 
                print("You recieved a letter grade: D")
            elif score >= 0: 
                print("You recieved a letter grade: F")
            else: 
                print("The score provided is not in range. Try Again")        
    main()
elif exampleChoice == 18:
    ## Displays proper function placement + custom parity testing function. 
    def main(): 
        userInput6 = int(input("Enter a number to test its parity: "))
        parityTest(userInput6)
    ## Custom parity function
    def parityTest(n):
        if n % 2 == 0:
            print("Number is even")
        else: 
            print("Number is odd") 
    main()
else: 
    print("No example was chosen, goodbye.")