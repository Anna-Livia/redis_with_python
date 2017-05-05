import hashes



name_undefined = True
print("")
print("")
print("##### MESSAGING BOARD #####")

while name_undefined :

    print("")
    print("")
    print("What is your name ?")
    print("A name stars with @, can contain alpha num, - or _")
    print("")
    print("")
    given_name = input("Your name : ")

    if hashes.name_check(given_name):
        name_undefined = False
        user_name = str.lower(given_name)
        if user_name not in hashes.get_user_names() :
            print("")
            print("Are you new ?")
            is_new_user = input("Your Answer (y/n):  ")
            password = input("set your password:  ")
            print("")
            if is_new_user == "n" :
                print("verify your username:  " + given_name)
                is_name_correct = input("confirm this is your handle (y/n):  ")
                if is_name_correct == 'n' :
                    name_undefined = True
            else :
                r.hset('users', given_name, password)
        else :
            not_auth = True
            while not_auth :
                input_password = input("enter your password:   ")
                if hashes.check_user_password(given_name, input_password) :
                    not_auth = False
                else :
                    print("This is not the right password")
                    exit_option = input("try again ? (y/n) --> ")
                    if exit_option == 'n' :
                        name_undefined = True
                        break
                    else :
                        pass


    else:
        print("this name is not valid")

print("")
print("")
print("######  Welcome " + given_name + " !  #####")

while True:
    print("")
    print("")
    print("##### MENU #####")
    print("")
    print("c - to write a new message")
    print("r - to read all the messages")
    print("@[user_handle] - to see a user timeline")
    print("")
    print("q - to quit")
    print("")
    print("################")
    interface = input("Your choice:  ")
    print("")
    print("")
    print("")
    if interface == 'c':
        input_message = input("Enter your message: ")
        hashes.create_tweet(given_name, input_message)
    elif interface == 'r':
        hashes.print_tweets(hashes.get_all_tweets())
    elif interface == 'q':
        break
    else:
        res = hashes.get_tweet_for_one_user(interface)
        if len(res) > 0 :
            hashes.print_tweets(res)
        else :
            print("this user does not exist")

