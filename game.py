import numpy as np

number = np.random.randint(1,101)
count = 0

while True:
    count += 1
    predict_number = int(input("Угадай число от 1 до 100:  "))
    
    if predict_number > number:
        print("number must be lower!")
    elif predict_number < number:
        print("number must be higher!")
    else:
        print(f"You're right! This number = {number}, used = {count} attempts")