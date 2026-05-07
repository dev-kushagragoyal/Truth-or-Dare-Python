import random
import time 

print("1.Start the game     2.Quit")
print()
start_choice = int(input("Enter your choice : "))
print()

if start_choice == 1:
    player_1 = input("Enter your name : ")
    print()
    player_2 = input("Enter another player name : ")
    print()
    print("Welcome to the game",player_1,"and",player_2)
    print()

    if random.randint(0,1) == 0:
            current_player = player_1
    else:
        current_player = player_2

    while True:

        # Player 1
        if current_player == player_1:

            print("-----------------------------------")
            print()
            print(player_1,"Choose Truth(1) or Dare(2)")
            print()
            player_1_choice = int(input("Enter your choice : "))
            print()

            # Player 1 Truth
            if player_1_choice == 1:
                Truth = random.randint(1,5)
                if Truth == 1:
                    T_1 = ("When was the last time you cleaned your room ?")
                    print("Here is your Truth : ")
                    print()
                    print(T_1)
                    print()
                    print("1.Done     2.Not done")
                    print()
                    done = int(input("Enter the result : "))
                    print()
                    if done == 1:
                        print("Congrats!!!")
                        print()
                        current_player = player_2
                    else:
                        print("Your friends can give you a dare!!!")
                        print()
                        time.sleep(1)
                        current_player = player_2
                elif Truth == 2:
                    T_2 = ("What famous person would you not like to meet ?")
                    print("Here is your Truth : ")
                    print()
                    print(T_2)
                    print()
                    print("1.Done     2.Not done")
                    print()
                    done = int(input("Enter the result : "))
                    print()
                    if done == 1:
                        print("Congrats!!!")
                        print()
                        current_player = player_2
                    else:
                        print("Your friends can give you a dare!!!")
                        print()
                        time.sleep(1)
                        current_player = player_2
                elif Truth == 3:
                    T_3 = ("What job would you like when you grow up ?")
                    print("Here is your Truth : ")
                    print()
                    print(T_3)
                    print()
                    print("1.Done     2.Not done")
                    print()
                    done = int(input("Enter the result : "))
                    print()
                    if done == 1:
                        print("Congrats!!!")
                        print()
                        current_player = player_2
                    else:
                        print("Your friends can give you a dare!!!")
                        print()
                        time.sleep(1)
                        current_player = player_2
                elif Truth == 4:
                    T_4 = ("If you had to live with another family, who would it be ?")
                    print("Here is your Truth : ")
                    print()
                    print(T_4)
                    print()
                    print("1.Done     2.Not done")
                    print()
                    done = int(input("Enter the result : "))
                    print()
                    if done == 1:
                        print("Congrats!!!")
                        print()
                        current_player = player_2
                    else:
                        print("Your friends can give you a dare!!!")
                        print()
                        time.sleep(1)
                        current_player = player_2
                elif Truth == 5:
                    T_5 = ("What type of bird would you like to be ?")
                    print("Here is the Truth : ")
                    print()
                    print(T_5)
                    print()
                    print("1.Done     2.Not done")
                    print()
                    done = int(input("Enter the result : "))
                    print()
                    if done == 1:
                        print("Congrats!!!")
                        print()
                        current_player = player_2
                    else:
                        print("Your friends can give you a dare!!!")
                        print()
                        time.sleep(1)
                        current_player = player_2

            # Player 1 Dare
            else:
                Dare = random.randint(1,5)
                if Dare == 1:
                    D_1 = ("Pretend to be a monkey and groom your friend's hair.")
                    print("Here is your Dare : ")
                    print()
                    print(D_1)
                    print()
                    print("1.Done     2.Not done")
                    print()
                    done = int(input("Enter the result : "))
                    print()
                    if done == 1:
                        print("Congrats!!!")
                        print()
                        current_player = player_2
                    else:
                        print("Your friends can give you a dare!!!")
                        print()
                        time.sleep(1)
                        current_player = player_2
                elif Dare == 2:
                    D_2 = ("Act like you're in an earthquake.")
                    print("Here is your Dare : ")
                    print()
                    print(D_2)
                    print()
                    print("1.Done     2.Not done")
                    print()
                    done = int(input("Enter the result : "))
                    print()
                    if done == 1:
                        print("Congrats!!!")
                        print()
                        current_player = player_2
                    else:
                        print("Your friends can give you a dare!!!")
                        print()
                        time.sleep(1)
                        current_player = player_2
                elif Dare == 3:
                    D_3 = ("Catch three pieces of candy in your mouth.")
                    print("Here is your Dare : ")
                    print()
                    print(D_3)
                    print()
                    print("1.Done     2.Not done")
                    print()
                    done = int(input("Enter the result : "))
                    print()
                    if done == 1:
                        print("Congrats!!!")
                        print()
                        current_player = player_2
                    else:
                        print("Your friends can give you a dare!!!")
                        print()
                        time.sleep(1)
                        current_player = player_2
                elif Dare == 4:
                    D_4 = ("Talk with your thumb in your mouth.")
                    print("Here is your Dare : ")
                    print()
                    print(D_4)
                    print()
                    print("1.Done     2.Not done")
                    print()
                    done = int(input("Enter the result : "))
                    print()
                    if done == 1:
                        print("Congrats!!!")
                        print()
                        current_player = player_2
                    else:
                        print("Your friends can give you a dare!!!")
                        print()
                        time.sleep(1)
                        current_player = player_2
                elif Dare == 5:
                    D_5 = ("Do an impression of your dad.")
                    print("Here is your Dare : ")
                    print()
                    print(D_5)
                    print()
                    print("1.Done     2.Not done")
                    print()
                    done = int(input("Enter the result : "))
                    print()
                    if done == 1:
                        print("Congrats!!!")
                        print()
                        current_player = player_2
                    else:
                        print("Your friends can give you a dare!!!")
                        print()
                        time.sleep(1)
                        current_player = player_2

        # Player 2 
        elif current_player == player_2:

            print("-----------------------------------")
            print()
            print(player_2,"Choose Truth(1) or Dare(2)")
            print()
            player_2_choice = int(input("Enter your choice : "))
            print()

            # Player 2 truth
            if player_2_choice == 1:
                Truth = random.randint(1,5)
                if Truth == 1:
                    T_1 = ("When was the last time you cleaned your room ?")
                    print("Here is your Truth : ")
                    print()
                    print(T_1)
                    print()
                    print("1.Done     2.Not done")
                    print()
                    done = int(input("Enter the result : "))
                    print()
                    if done == 1:
                        print("Congrats!!!")
                        print()
                        current_player = player_1
                    else:
                        print("Your friends can give you a dare!!!")
                        print()
                        time.sleep(1)
                        current_player = player_1
                elif Truth == 2:
                    T_2 = ("What famous person would you not like to meet ?")
                    print("Here is your Truth : ")
                    print()
                    print(T_2)
                    print()
                    print("1.Done     2.Not done")
                    print()
                    done = int(input("Enter the result : "))
                    print()
                    if done == 1:
                        print("Congrats!!!")
                        print()
                        current_player = player_1
                    else:
                        print("Your friends can give you a dare!!!")
                        print()
                        time.sleep(1)
                        current_player = player_1
                elif Truth == 3:
                    T_3 = ("What job would you like when you grow up ?")
                    print("Here is your Truth : ")
                    print()
                    print(T_3)
                    print()
                    print("1.Done     2.Not done")
                    print()
                    done = int(input("Enter the result : "))
                    print()
                    if done == 1:
                        print("Congrats!!!")
                        print()
                        current_player = player_1
                    else:
                        print("Your friends can give you a dare!!!")
                        print()
                        time.sleep(1)
                        current_player = player_1
                elif Truth == 4:
                    T_4 = ("If you had to live with another family, who would it be ?")
                    print("Here is your Truth : ")
                    print()
                    print(T_4)
                    print()
                    print("1.Done     2.Not done")
                    print()
                    done = int(input("Enter the result : "))
                    print()
                    if done == 1:
                        print("Congrats!!!")
                        print()
                        current_player = player_1
                    else:
                        print("Your friends can give you a dare!!!")
                        print()
                        time.sleep(1)
                        current_player = player_1
                elif Truth == 5:
                    T_5 = ("What type of bird would you like to be ?")
                    print("Here is your Truth : ")
                    print()
                    print(T_5)
                    print()
                    print("1.Done     2.Not done")
                    print()
                    done = int(input("Enter the result : "))
                    print()
                    if done == 1:
                        print("Congrats!!!")
                        print()
                        current_player = player_1
                    else:
                        print("Your friends can give you a dare!!!")
                        print()
                        time.sleep(1)
                        current_player = player_1

            # Player 2 Dare
            else:
                Dare = random.randint(1,5)
                if Dare == 1:
                    D_1 = ("Pretend to be a monkey and groom your friend's hair.")
                    print("Here is your Dare : ")
                    print()
                    print(D_1)
                    print()
                    print("1.Done     2.Not done")
                    print()
                    done = int(input("Enter the result : "))
                    print()
                    if done == 1:
                        print("Congrats!!!")
                        print()
                        current_player = player_1
                    else:
                        print("Your friends can give you a dare!!!")
                        print()
                        time.sleep(1)
                        current_player = player_1
                elif Dare == 2:
                    D_2 = ("Act like you're in an earthquake.")
                    print("Here is your Dare : ")
                    print()
                    print(D_2)
                    print()
                    print("1.Done     2.Not done")
                    print()
                    done = int(input("Enter the result : "))
                    print()
                    if done == 1:
                        print("Congrats!!!")
                        print()
                        current_player = player_1
                    else:
                        print("Your friends can give you a dare!!!")
                        print()
                        time.sleep(1)
                        current_player = player_1
                elif Dare == 3:
                    D_3 = ("Catch three pieces of candy in your mouth.")
                    print("Here is your Dare : ")
                    print()
                    print(D_3)
                    print()
                    print("1.Done     2.Not done")
                    print()
                    done = int(input("Enter the result : "))
                    print()
                    if done == 1:
                        print("Congrats!!!")
                        print()
                        current_player = player_1
                    else:
                        print("Your friends can give you a dare!!!")
                        print()
                        time.sleep(1)
                        current_player = player_1
                elif Dare == 4:
                    D_4 = ("Talk with your thumb in your mouth.")
                    print("Here is your Dare : ")
                    print()
                    print(D_4)
                    print()
                    print("1.Done     2.Not done")
                    print()
                    done = int(input("Enter the result : "))
                    print()
                    if done == 1:
                        print("Congrats!!!")
                        print()
                        current_player = player_1
                    else:
                        print("Your friends can give you a dare!!!")
                        print()
                        time.sleep(1)
                        current_player = player_1
                elif Dare == 5:
                    D_5 = ("Do an impression of your dad.")
                    print("Here is your Dare : ")
                    print()
                    print(D_5)
                    print()
                    print("1.Done     2.Not done")
                    print()
                    done = int(input("Enter the result : "))
                    print()
                    if done == 1:
                        print("Congrats!!!")
                        print()
                        current_player = player_1
                    else:
                        print("Your friends can give you a dare!!!")
                        print()
                        time.sleep(1)
                        current_player = player_1

else:
    print("You got quit")
