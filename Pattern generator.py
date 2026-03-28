print("Welcome to the Pattern Generator and Number Analyzer!")

while True:
    print("\nSelect an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    # OPTION 1: PATTERN
    if choice == 1:
        num = int(input("Enter number of rows: "))

        print("\nSelect Pattern Type:")
        print("1. Right Triangle")
        print("2. Inverted Triangle")

        p_choice = int(input("Enter pattern choice: "))

        print("\nPattern:\n")

        if p_choice == 1:
            for i in range(1, num + 1):
                print("*" * i)

        elif p_choice == 2:
            for i in range(num, 0, -1):
                print("*" * i)

        else:
            print("Invalid pattern choice!")

    # OPTION 2: ANALYSIS
    elif choice == 2:
        start = int(input("Enter start of range: "))
        end = int(input("Enter end of range: "))

        even = []
        odd = []
        total_sum = 0

        for num in range(start, end + 1):
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)

            total_sum += num

        print("\nEven Numbers:", even)
        print("Odd Numbers:", odd)
        print("Total Numbers:", (end - start + 1))
        print("Sum:", total_sum)

    # EXIT
    elif choice == 3:
        print("Exiting the program...")
        break

    else:
        print("Invalid choice! Please try again.")