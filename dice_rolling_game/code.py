import random

count = 0
while True: 
    choice = input('Roll the dice: (y/n): ').lower()


    if choice == 'y':
        try: 
            n = int(input("How many time you wanna roll: "))
        except ValueError:
            print("Please enter correct value!")
            continue

            # loop in range
        for _ in range(n):  
                
                dice1 = random.randint(1,6)
                dice2 = random.randint(1,6)
                count += 1
                print(f'You rolled : ({count}). ({dice1},{dice2})')

        print("count", count)

    elif choice == 'n':
        print("Thank you for playing! Your total rolled {count}")
        break
    else:
        print("Invalid roll! please try again.")





   


  
# infinite loop
#   if user enter Y
#   generate a random numbers
#   print it
# If enter n
#   print thank you
#   terminat
# else
#   print Invalid choice

# additionally added how manny rolled and printed it