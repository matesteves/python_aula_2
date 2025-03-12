try:
    name = str(input("What's your name? "))
    salary = float(input("What's your salary? "))
    bonus = float(input("What's your bonus %? "))
    final_bonus = 1000 + salary * bonus/100

    print(f"Hey, {name}! Acording to your bonus, this is you bonus for the month: {final_bonus}")
except:
    print("Make sure you are typing the right input for the question")