while True: 
    user_input = input (" Please Enter the word to be checked : ")
    user_input_lower = user_input.lower()
    reversed_word= user_input_lower[::-1]

    def palindrome_func(user_input_lower):
        if user_input_lower == reversed_word :
            print (f" Your word --> {user_input} , is reversed --> {reversed_word} --> and it's Palindrome ! You're Smart :)")
        else:
            print (" Hard Luck , Your word is not Palindrome !")
    palindrome_func(user_input_lower)

    user_decision= input(" Would you like to try aother word ? (y/n)")

    if user_decision == "y":
        continue
    else:
        break


