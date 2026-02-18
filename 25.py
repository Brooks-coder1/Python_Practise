def container(a):
    if a in [1, 5, 8, 3]:
        print(True)
    else:
        print(False)


while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")

    if user_input.lower() == "exit":
        print("Program terminated.")
        break

    try:
        a = int(user_input)
        container(a)

    except ValueError:
        print("Oops! Please enter a valid number or 'exit'.")
