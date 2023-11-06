import random

already_asked = []


def guess_program():
    y = random.randint(1, 1000)
    count = 0
    while True:
        x = int(input("State your guess: "))
        if y not in already_asked:
            if x == y:
                print(f"Congratulations you have got it in {count} attempts! The number was {y}.")
                already_asked.append(x)
                continue
            elif x > y:
                print("Too high!")
            elif x < y:
                print("Too low!")
            count += 1
        else:
            continue



print("I have a number between 1 and 1000. Can you 'guess' my number.")
guess_program()
