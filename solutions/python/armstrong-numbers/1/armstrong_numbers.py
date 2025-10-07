def is_armstrong_number(number):
    num_to_str = str(number)
    sum = 0
    
    for c in num_to_str:
        sum += int(c) ** len(num_to_str)
    return sum == number
