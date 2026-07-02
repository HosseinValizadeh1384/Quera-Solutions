def find(num1, num2, num3):
    all_numbers = [1, 2, 3, 4]
    existed_numbers = [num1, num2, num3]
    for number in all_numbers:
        if number not in existed_numbers:
            return number
