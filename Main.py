#M1HW Main
#Alex Alejandro
#8/21/2024
from functions import *


def main():
    while True:
        choice = menu()

        if choice == "1":
            print("you chose to add:")
            numbers = add()
            result = calc_add(numbers)
            print(result)
            print("")

        elif choice == "2":
            print("you chose to subtract:")
            numbers = sub()
            result = calc_sub(numbers)
            print(result)
            print("")

        elif choice == "3":
            print("you chose to divide:")
            numbers = div()
            result = calc_div(numbers)
            print(result)
            print("")

        elif choice == "4":
            print("you chose to multiply:")
            numbers = mul()
            result = calc_mul(numbers)
            print(result)
            print("")

        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid input, please try again!")
                  
        


if __name__ == "__main__":
    main()
