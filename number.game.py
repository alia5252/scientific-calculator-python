import random 
# load high score 
try:
    with open("highscore.txt","r")as file:
        high_score = int(file.read())
except:
    high_score = 0
total_score = 0
while True:
    print("\n==== Number guessing game ==== ")
    print("High Score:", high_score)
    print("\nSelect Difficulty")
    print("1.Easy")
    print("2.Medium")
    print("3.Hard")
    choice = input("Enter choice: ")
    if choice == "1":
        limit = 10
        max_attempts =5
    elif choice =="2":
        limit = 50
        max_attempts = 7
    elif choice == "3":
        limit = 100
        max_attempts = 10
    else :
        print("Invaild choice")
        continue
    secret_number = random.randint(1,limit)
    attempts = 0
    while attempts <max_attempts :
        user_input = input(
            f"\nGuess a number between 1 and {limit}\n"
            "Type 'hint' for hint\n"
            "Type 'cheat' to reveal number\n"
            "Enter guess: "
        )


        # cheat mode
        if user_input.lower() == "cheat":

            print("Cheat Mode Activated!")
            print("Secret Number is:", secret_number)

            continue
            
        # hint mode
        elif user_input.lower() == "hint":

            if secret_number > limit // 2:
                print("Hint: The number is greater than", limit // 2)

            else:
                print("Hint: The number is less than or equal to", limit // 2)

            continue

        #input handling
        try:
            guess = int(input(f"guess a number between 1 and {limit}:"))
        except ValueError:
            print("please enter a vaild number")

        #range cheak
        if guess < 1 or guess> limit:
            print("Number is out of range")
            continue
        attempts += 1
        remaining = max_attempts-attempts

        if guess == secret_number:
            print("Correct! you guessed the number.")
            print("Total attempts :",attempts)
            score = (max_attempts- attempts + 1 ) * 10
            print("You earned",score,"points!") 
            total_score += score
            print("Total score:",total_score)

            #update high score 
            if total_score >high_score:
                high_score = total_score
                with open("highscore.txt","w")as file:
                    file.write(str(high_score))
                print("New High Score!")

            break 
        elif guess > secret_number:
            print("Too high!")
        else:
            print ("Too low!")
        print("Remaining attempts:",remaining)
    else:
        print("Game over")
        print("The number was:", secret_number)
    play_again = input("\nDo you want to play again (yes/no):")
    if play_again.lower() != "yes":
        print("Thanks for playing")
        break