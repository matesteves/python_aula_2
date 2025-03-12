import numpy as np
#1
#n1 = float(input("What's the first number? "))
#n2 = float(input("What's the second number? "))
#sum = n1 + n2
#print(f"The sum of the two numbers is: {sum}")

#2
#n1 = float(input("What's the first number? "))
#n2 = float(input("What's the second number? "))
#remainder = n1 % n2
#print(f"The remainder of the division is: {remainder}")

#3
#n1 = float(input("What's the first number? "))
#n2 = float(input("What's the second number? "))
#multiplication = n1 * n2
#print(f"The result of the multiplication is: {multiplication}")

#4
#n1 = int(input("What's the first integer? "))
#n2 = int(input("What's the second integer? "))
#division = n1//n2
#print(f"The result of the division is: {division}")

#5 
#n1 = int(input("What's the number? "))
#square = n1**2
#print(f"{n1} squared is: {square}")

#6
#n1 = float(input("What's the first number? "))
#n2 = float(input("What's the second number? "))
#sum = n1 + n2
#print(f"The sum is: {sum}")

#7
#n1 = float(input("What's the first number? "))
#n2 = float(input("What's the second number? "))
#avg = (n1 + n2)/  2
#print(f"The average is: {avg}")

#8
#n1 = float(input("Number for the exponentiation: "))
#n2 = float(input("Power of: "))
#exp = n1 ** n2
#print(f"{n1} to the power of {n2} is: {exp}")

#9
#c = float(input("What's the temperature in Celsius? "))
#f = (c * 9/5) + 32
#print(f"The temperature in Fahrenheits is: {f}")

#10
#r = float(input("What's the radius of the circle? "))
#area = round(2 * np.pi * r, 2)
#print(f"The area of the circle is: {area}")

#11
#phrase = str(input("What's your input? "))
#phrase_caps = phrase.upper()
#print(f"Here's your input in all caps: {phrase_caps}")

#12
#phrase = str(input("What's your input? "))
#phrase_lower_case = phrase.lower()
#print(f"Here's your input in lower case: {phrase_lower_case}")

#13
#phrase = str(input("What's your input? "))
#trimmed_phrase = phrase.strip()
#print(f"Here's your cleaned text: {trimmed_phrase}")

#14
#date = str(input("What's the date? DD/MM/YYYY "))
#date_list = date.split("/")
#print(f"Day: {date_list[0]}, month: {date_list[1]}, year: {date_list[2]}")

#15
#phrase1 = str(input("What's your first input? "))
#phrase2 = str(input("What's your second input? "))
#phrase3 = phrase1 + phrase2
#print(f"The concatenation is: {phrase3}")

#16
#bool1 = False
#bool2 = True
#resultado_and = bool1 and bool2
#print("Resultado do AND lógico:", resultado_and)

#17
#bool1 = str(input("What's your first boolean? "))
#bool2 = str(input("What's your second boolean? "))
#
#logical_test = bool1 or bool2 
#print(logical_test)

#18
#bool1 = str(input("What's your boolean value? "))
#
#inverted = not bool1
#print(f"Your inverted value: {inverted}")

#19
#n1 = float(input("What's the first number? "))
#n2 = float(input("What's the second number? "))
#test = (n1 == n2)
#
#print(f"Are your numbers equal? {test}")

#21

#try:
#    c = float(input("What's the temperature in Celsius? "))
#    f = (c * 9/5) + 32
#    print(f"The temperature in Fahrenheits is: {f}")
#except:
#    print("Your input needs to be a number.")

#22
#text = input("Type your input: ")
#if isinstance(text, str):
#    formatted_text = text.replace(" ", "").lower()
#    if formatted_text == formatted_text[::-1]:
#        print("It's a palindrome.")
#    else:
#        print("It's not a palindrome.")
#else:
#    print("Invalid input. Write a text.")

#23
#try:
#    num1 = float(input("Type the first number: "))
#    num2 = float(input("Type the second number: "))
#    operation = input("What's the operation you want to perform? (+, -, *, /) ")
#    if operation == '+':
#        result = num1 + num2
#    elif operation == '-':
#        result = num1 - num2
#    elif operation == '*':
#        result = num1 * num2
#    elif operation == '/' and num2 != 0:
#        result = num1 / num2
#    else:
#        print("Invalid operator or division by 0")
#    print("Resultado:", result)
#except ValueError:
#    print("Error: Invalid entry. Make sure to type numbers only.")

#24
#try:
#    number = int(input("Type a number: "))
#    if number > 0:
#        print("Positive")
#    elif number < 0:
#        print("Negative")
#    else:
#        print("Zero")
#    if number % 2 == 0:
#        print("Even")
#    else:
#        print("Odd")
#except ValueError:
#    print("Please, make sure to type a number.")

#25
#list = input("Type a list of numbers separated by commas.")
#num_str = list.split(",")
#num_int = []
#try:
#    for num in num_str:
#        num_int.append(int(num.strip()))
#    print("Integer list:", num_int)
#except ValueError:
#    print("Error: make sure that all numbers are valid integers.")