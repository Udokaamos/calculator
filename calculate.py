def add(x, y):
    return x + y
    # return result

def subtract(x, y):
    return x - y
    # return result

def multiply(x, y):
    return x* y
    # return result

def divide(x, y):
    return x/y
    # return result

print("Please select which operation you would like to perform\n\n"\
    "1. Add\n" \
    "2. Subtract \n" \
    "3. Multiply \n" \
    "4. Divide \n" \
    "5. Exit \n")


while True:
    """This takes input from the user from '1' to '4'"""
    operation = input("Enter your choice of operation operation you want to perform: 1, 2, 3, 4, or 5 to exit:  \n")
    
    if operation in ('1','2','3','4'):
        """Validates the choice input of the user"""
        try:
            num_1 = int(input("Please enter the first number:  "))
            num_2 = int(input("Please enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter a number")
            break

        if operation == '1':
            print(add(num_1, num_2))
     
        elif operation == '2':
            print(subtract(num_1, num_2))

        elif operation =='3':
            print(multiply(num_1, num_2))
            
        elif operation == '4':
            print(divide(num_1, num_2))
            break
    else:
        print("Invalid input")
        break

     

        
    
