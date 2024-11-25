# Name: Rayan Roshan
# Date: November 24th, 2024
# Project Name: FinTeen
# Project Description:
"""
This is a financial management program for young adults who would like to create and manage their crypto portfolio. 
This solves the problem on the complicated process of purchasing crypto currencies. 
As for young investors, they want to able to easily purchase and sell crypto currencies, and to be apart of the market.

The features would be the following:

Product:
- Creating and managing a crypto portfolio.
- Being able to purchase and sell crypto currencies.

Security Features: 
- Adding user function.
    - Adding the user to user database.
- Login function.
    - grabbing the user's information and database.
"""

# This function is used to understand how much money is in the user's checking account. 
# Here we use the user_database file to access the user's information. 
def checking_account_request(user_name):
    # This would grab the user's details regarding the checking account, using the database file and reading it.
    user_database = open("user_database", "r")
    lines = user_database.readlines()
    # This is where we locate the user's information using indexing.
    user_name_index = lines.index(user_name + "\n")
    checking_account_value = lines[user_name_index + 3]
    # This is where we close the file and return the amount.
    user_database.close()
    return checking_account_value

# This function is used to find the user's crypto portfolio. 
# Here we use the user_database file to access the user's information. 
def crypto_portfolio_request(user_name):
    # This would grab the user's details regarding the crypto portfolio, using the database file and reading it.
    user_database = open("user_database", "r")
    lines = user_database.readlines()
    # This is where we locate the user's information using indexing.
    user_name_index = lines.index(user_name + "\n")
    crypto_portfolio = str(lines[(user_name_index + 5)])
    # This would close the user_database file.
    user_database.close()
    # This would allow us to create the portfolio dictionary. This would enable us to access values. We would then return the dictionary.
    # This eval() function is used parse strings that formated as dictionaries and to create a functionable dictionary. 
    portfolio_dict = eval(crypto_portfolio.strip())
    #portfolio_dict = {crypto_portfolio[0]: int(crypto_portfolio[1]), crypto_portfolio[2]: int(crypto_portfolio[3]), crypto_portfolio[4]: int(crypto_portfolio[5]), crypto_portfolio[6]: int(crypto_portfolio[7])}
    return portfolio_dict

# This function is used to update values and details for the user.
def update_account_function(user_name, checking_account, crypto_portfolio):
    # This is where we open our user_database file that would allow us to access user's information. 
    user_database = open("user_database", "r")
    lines = user_database.readlines()
    # This is where we locate the user's information using indexing.
    user_name_index = lines.index(user_name + "\n")
    # This is where we make the changes. These changes are focused on their crypto portfolio and the amount in their checking account.
    lines[user_name_index + 3] = str(checking_account) + "\n"
    lines[user_name_index + 5] = str(crypto_portfolio)
    # This is where we make the updates directly on the file using the update string, lines, and rewrite the file.
    user_database = open("user_database", "w")
    user_database.writelines(lines)
    user_database.close()

# This function is focused on allowing the user to purchase crypto currencies.
def purchase_crypto(user_name):
    print ("\n****************************************************************************\n")
    # This is where we call the functions that allow us to grab the user information. 
    checking_account = int(checking_account_request(user_name))
    crypto_portfolio = crypto_portfolio_request(user_name)
    # This is where direct the user to the selection crypto currencies that they can purchase.
    print ("\nWhat crypto currency would you like to purchase?\n")
    print ("Please take a look at the crypto curriences that you can purchase: \n")
    # These are the crypto currencies that are avaliable to purchase. We're using a dictionary to make it easy to access values. 
    crypto_currencies = {"BITCOIN": 125040, "ETHEREUM": 4374, "SOLANA": 297, "XRP":1}
    # This for-loop is used to print out values from the dictionary. 
    for key, value in crypto_currencies.items():
        print(key, ":", value)

    # This while-loop is used to grab the user's choices. 
    # This is also a loop because we want to make sure that the user doesn't input anything wrong.
    user_choice = ""
    while True:
        # This is where we grab the user's choice.
        user_choice = input("\nPlease enter the name of crypto currency you would ike to purhcase: ").upper()
        # This is where we check the user's choice. If they input something wrong, then we ask them to input something again. 
        if user_choice in crypto_currencies:
            break
        else:
            print ("\nYour chosen coin is not up for sale. Please try again!\n")
            print ("\nPlease enter the name of the coin that you would like to purchase!\n")
    
    # This is where we grab how many coins the user would like to purchase. 
    user_purchase_amount = 0
    # This while-loop is used to grab the user's choices. 
    # This is also a loop because we want to make sure that the user doesn't input anything wrong.
    while True:
        # This is where we grab the user's choice.
        user_purchase_amount = int(input("Please enter the amount of coins would you like to purhcase: "))
        # We would check if the user has enough to pay for the crypto currency and to check if they input an integer.
        # This is where we a try-atch to check for any errors. 
        try:
            if user_purchase_amount * crypto_currencies[user_choice] > checking_account:
                print ("Please enter a lower amount.")
            else:
                break
        except ValueError:
            print ("\nPlease enter the integer value. Ex) 2, 3 \n")

    # This is where do our calculations that would update the user's crypto portfolio and their checking account amount.
    crypto_portfolio[user_choice] += user_purchase_amount
    checking_account -= user_purchase_amount * crypto_currencies[user_choice]
    # This is where we call the update function to update the user's details directly with the file.
    update_account_function(user_name, checking_account, crypto_portfolio)
    # This is telling the user that the operation has been completed. 
    # The user will be redirected to selection stage to complete any other tasks.
    print ("\nOperation done!\n")
    # This is used to print out the user's updated portfolio and the amount in their checking account.
    print ("Updated Portfolio:\n")
    # This for-loop is used to print out values from their portfolio dictionary. 
    for key, value in crypto_portfolio.items():
        print(key, ":", value)
    print (f"\nUpdated checking account amount: {checking_account}\n")
    crypto_selection_func(user_name)

# This function is focused on allowing the user to purchase crypto currencies.
def sell_crypto(user_name):
    print ("\n****************************************************************************\n")
    # This is where we call the functions that allow us to grab the user information. 
    checking_account = int(checking_account_request(user_name))
    crypto_portfolio = crypto_portfolio_request(user_name)
    # This is where direct the user to where we can help the user sell their crypto currencies.
    print ("\nWhat crypto currency would you like to sell?\n")
    print ("Please take a look at the crypto curriences that you can sell: \n")
    # These are the crypto currencies that are avaliable to sell. We're using a dictionary to make it easy to access values. 
    for key, value in crypto_portfolio.items():
        print(key, ":", value)
    
    # This while-loop is used to grab the user's choices. 
    # This is also a loop because we want to make sure that the user doesn't input anything wrong.
    user_choice = ""
    while True:
        # This is where we grab the user's choice.
        user_choice = input("\nPlease enter the name of crypto currency you would ike to sell: ").upper()
        # This is where we check the user's choice. If they input something wrong, then we ask them to input something again. 
        if user_choice in crypto_portfolio:
            break
        else:
            print ("\nYour chosen coin is not up for sale. Please try again!\n")
            print ("\nPlease enter the name of the coin that you would like to sell!\n")
    
    # This is where we grab how many coins the user would like to sell. 
    user_purchase_amount = 0
    while True:
        # This is where we grab the user's choice.
        user_purchase_amount = int(input("Please enter the amount of coins would you like to sell: "))
        try:
            # This is where we check the user's choice. If they input something wrong, then we ask them to input something again. 
            if user_purchase_amount > crypto_portfolio[user_choice]:
                print ("Please enter a lower amount.")
            else:
                break
        except ValueError:
            print ("\nPlease enter the integer value. Ex) 2, 3 \n")

     # This is where do our calculations that would update the user's crypto portfolio and their checking account amount.
    crypto_portfolio[user_choice] -= user_purchase_amount
     # These are the crypto currencies that are avaliable to purchase. We're using a dictionary to make it easy to access values. 
    crypto_currencies = {"BITCOIN": 125040, "ETHEREUM": 4374, "SOLANA": 297, "XRP":1}
    checking_account += (user_purchase_amount * crypto_currencies[user_choice])
    print ("\nOperation done!\n")
    # This is used to print out the user's updated portfolio and the amount in their checking account.
    print ("Updated Portfolio:\n")
    # This for-loop is used to print out values from their portfolio dictionary. 
    for key, value in crypto_portfolio.items():
        print(key, ":", value)
    print (f"\nUpdated checking account amount: {checking_account}\n")
    crypto_selection_func(user_name)

# This function is used to purchase and show their crypto currency. 
def crypto_selection_func(user_name):
    print ("\n****************************************************************************\n")
    # This the introduction for the user to the crypto exchange.
    print ("\nHello! Welcome to the FinTeen crypto exchange!\n")
    print ("\nPlease choose an operation that you would like to perform: \n")
    print ("1. Purchase crypto currency\n2. Sell crypto currency\n3. Leave\n")
    # This while-loop is used to check what operation that the user would like to perform. 
    # This while-loop is used to grab the user's choices. 
    # This is also a loop because we want to make sure that the user doesn't input anything wrong.
    while True:
        try:
            user_choice = int(input("Please enter your choice: "))
            if user_choice != 1 and user_choice != 2 and user_choice != 3:
                 print ("\nPlease choose 1 out of the three options!\n")
            else:
                break
        except ValueError:
            print ("\nPlease the integer value of the operation you would like to perform!\n")
    # This if-else block statement is used to decide what operation would we perform and then call the function.
    if user_choice == 1:
        purchase_crypto(user_name)
    elif user_choice == 2:
        sell_crypto(user_name)
    elif user_choice == 3:
        print ("Alright. Have a great day and thank you for using FinTeen.\n")

# This function is used to login-in users to the user database.
def loginIn_functions():
    print ("\n****************************************************************************\n")
    # This is where direct the user to login-in using their username and password.
    print ("Hello there! Please provide your username and password:\n")
    # This is where we open our user database. 
    user_info_file = open("user_info", "r")

    # This while-loop is used to grab the user's username and password. 
    # If they are not in the system or provide incorrect information, they would be within the bounds of the loop.
    while True:

        # This is to get the user's username and password.
        user_name = input("\nPlease provide your unique username: ")
        user_password = input("\nPlease provide your password: ")

        # This is to get the data from the file itself.
        lines = user_info_file.readlines()
        # This if-else block is used to check if the user is in the system or not.
        if user_name + "\n" in lines:
            password_index = lines.index(user_name + "\n") + 1
            if user_password + "\n" == lines[password_index]:
                print ("\nWelcome Back!\n")
                break
            else:
                print ("\nYour password is incorrect. Please try again.\n")
        else:
            print ("\nYour username is incorrect. Please try again.\n")

    # This is to close the user_info file.
    user_info_file.close()
    # This is used to call a function that would allow the user to operate any functions. 
    crypto_selection_func(user_name)

# This function is used to add users to the user database when they are just joining the program.
def adding_user():
    print ("\n****************************************************************************\n")
    print ("\nHello! Let's sign you up!\n")
    print ("We're going to ask you fill in some information!\n")
    
    # This would be used to grab the user's name. 
    user_name = input("Please enter your full name: ")
    # This while-loop would be used to grab the user's age. 
    while True:
        try: 
            # This is to get the user's age input. 
            user_age = int(input("Please enter you age: "))
            if user_age < 18:
                print ("\nYou must be 18+ to use this program!\n")
            else:
                break
        # This is used to catch any error's the user may cause to crash the program.
        except:
            print ("\nPlease try again! You must enter the integer value!\n")

    # This is used to open our user info file.
    check_file = open("user_info", "r")
    # This while-loop is used to enter the user's username and password. 
    # If they are not in the system or provide incorrect information, they would be within the bounds of the loop.
    while True:
        # This is to grab the user's input.
        userName_tag = input("Please enter a unique username: ")
        # This check variable will be used to check if the user's username is in the system. 
        check = False
        check_file.seek(0)
        # This for for-loop would be used to check if the username tag has been used and already in our system. 
        for line in check_file:
            if line.strip("\n") == userName_tag:
                print ("\nThis username has been taken! Please try again!\n")
                break
        else:
            check = True
        
        # If the check is True, it will break out and start the writing process.
        if check:
            break
    check_file.close()   

    # This would be used to grab the user's unique password.
    user_password = input("Please enter a password that is at least 10 characters long: ")
    
    # This while-loop would be used to check if the user has entered a password that is at least 10 characters long.
    while len(user_password) < 10:
        if len(user_password) < 10:
            print("\nPlease try again\n")
            user_password = input("Please enter a password that is at least 10 characters long: ")
        else:
            break
    
    # This print statement would be used to tell the user that they had joined the program.
    print ("\nYou have successfully joined FinTeen!\n")

    # This while-loop is used to make sure that the user's an integer value for their checking account. 
    # We are also using a try-catch to make sure that we catch any error's that may come from the user's input.
    while True:
        # This would catch any error's from the user.
        try: 
            user_deposit = int(input("Please enter an intial deposit amount for FinTeen checking account: "))
        except ValueError:
            print ("\nPlease try again!\n")
        else:
            break
    
    print ("\nRedirecting you to the login function!\n")

    # Opening and writing the user_info as well as the user_database file.
    user_info_file = open("user_info", "a")
    # This is used to write the user's details on to the user_info_file.
    user_info_file.write(f"{user_name.lower()}\n")
    user_info_file.write(f"{str(user_age)}\n")
    user_info_file.write(f"{userName_tag}\n")
    user_info_file.write(f"{user_password}\n")
    user_info_file.close()

    user_database_file = open("user_database", "a")
    # This is used to write the file in the user_database file.
    user_database_file.write(f"\n{user_name.lower()}\n")
    user_database_file.write(f"{userName_tag}\n")
    user_database_file.write(f"{user_password}\n")
    user_database_file.write(f"User checking account value: \n")
    user_database_file.write(f"{user_deposit}\n")
    user_database_file.write("Crypto portfolio: \n")
    user_database_file.write("{'BITCOIN': 0, 'ETHEREUM': 0, 'SOLANA': 0, 'XRP': 0}")
    user_database_file.close()
    
    # This would redirect the user to login-in to the program.
    loginIn_functions()

# This is the first function that is used to introduce the user to the program itself.
print ("Welcome to FinTeen!\n")
def introduction_function():

    # These print statements are used to redirect the user to various operations they can perform within the program.
    print ("Please enter the number option for one of the following options: ")
    print ("1. Logining in.")
    print ("2. Joining the program!")
    print ("3. Leave.\n")

    # This while-loop is used to ensure that the user has entered a valid input and that the user has chosen a valid option. 
    while True:
        # This is where we get the user's input.
        user_input = input("Please enter your option here: ")
        # This if-else statement block is used to decide what function to call and what operation to perform. 
        if user_input == "1":
            print ("\nAlright, logging in!")
            loginIn_functions()
            break
        elif user_input == "2":
            print ("\nGreat! Taking you to the join feature!\n")
            adding_user()
            break
        elif user_input == "3":
            print ("\nAlright. Have a great day and thank you for using FinTeen.\n")
            break
        else:
            print ("\nSorry, I don't understand. Please try again!\n")

# This would call the first function that is used to introduce the user to the program.
introduction_function()
print ("\n****************************************************************************")