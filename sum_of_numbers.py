def sum_of_numbers():
    # Get a positive number from the user
    while True:
        try:
            user_input = int(input("Enter a positive number: "))
            if user_input >= 0:
                break  # Exit the loop if a positive number is provided
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Calculate the sum using a while loop
    total_sum = 0
    current_number = 0

    while current_number <= user_input:
        total_sum += current_number
        current_number += 1

    # Display the result
    print(f"The sum of whole numbers from 0 to {user_input} is: {total_sum}")


# Call the function to run the program
sum_of_numbers()
