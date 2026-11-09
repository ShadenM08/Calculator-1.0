running = True
while running:
    try:
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))

        operation = input("Choose your operation (+, -, /, *, **): ")

        if operation == "+":
            result = num1 + num2
            print("The result is:", result)

        elif operation == "-":
            result = num1 - num2
            print("The result is:", result)

        elif operation == "/":
            result = num1 / num2
            print("The result is:", result)

        elif operation == "*":
            result = num1 * num2
            print("The result is:", result)

        elif operation == "**":
            result = num1 ** num2
            print("The result is:", result)

        else:
            print("Invalid operation!")

        while True:
            again = input("Would you like to calculate again? (yes/no): ").lower()
            if again == "yes":
                break

            elif again == "no":
                running = False
                break

            else:
                print("Invalid answer. Please enter yes or no")


    except ValueError:
        print("Invalid input! Please enter a number.")

    except ZeroDivisionError:
        print("You cannot divide by zero.")