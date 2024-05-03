import random



def get_numbers_ticket(min_num, max_num, quantity):
    
    numbers = set()
    while len(numbers) < quantity:
        number = random.randint(min_num, max_num)
        numbers.add(number)
        numbers_list = list(numbers)
        numbers_list.sort()
    print(f'Ваші лотерейні числа: {numbers_list}')

get_numbers_ticket(1, 100, 6)
