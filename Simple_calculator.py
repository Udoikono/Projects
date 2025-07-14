def more():
    while True:
        more = input(
            f'\nWill you like to perform a calculation? (y / n): ')
        if more == 'y':
            if more == 'y':
                break
        else:
            print('Goodbye!!!\n')
            continue


while True:
    try:
        print('\n-- WHAT DO YOU WANT TO DO? --')
        print('1. Addition')
        print('2. Subtraction')
        print('3. Multiplication')
        print('4. Division')
        print('5. Modulo')
        print('6. Exponentiation')
        print('7. Exit \n')

        choice = int(input('Enter your choice: '))
        if choice == 7:
            more()
            continue
        elif choice not in range(1, 7):
            print('Invalid choice')
            continue
        else:
            pass

        number1 = float(input('\nEnter first number: '))
        number2 = float(input('Enter second number: '))

        if choice == 1:
            while True:
                result = number1 + number2
                print(f'{number1} + {number2} = {result}\n')
                more()
                break
            continue

        elif choice == 2:
            while True:
                result = number1 - number2
                print(f'{number1} - {number2} = {result}')
                more()
                break
            continue

        elif choice == 3:
            while True:
                result = number1 * number2
                print(f'{number1} * {number2} = {result}')
                more()
                break
            continue

        elif choice == 4:
            while True:
                result = number1 / number2
                print(f'{number1} / {number2} = {result}')
                more()
                break
            continue

        elif choice == 5:
            while True:
                result = number1 // number2
                print(f'{number1} // {number2} = {result}')
                more()
                break
            continue

        elif choice == 6:
            while True:
                result = number1 ** number2
                print(f'{number1}^{number2} = {result}')
                more()
                break
            continue

    except:
        continue
