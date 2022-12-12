import random

def get_random_lotto_numbers(range_start_number: int, 
                             range_end_number: int, 
                             required_amount_of_numbers: int) -> int | list[int]:
    
    random_numbers: list[int] = list()

    if range_end_number - range_start_number < required_amount_of_numbers:
        return 0

    while len(random_numbers) < required_amount_of_numbers:
        
        random_number = random.randint(range_start_number, range_end_number)
        
        if random_number in random_numbers:
            #number is already stored in numbers. numbers can not be doubled.
            continue
            
        else:
            #append random number to lotto numbers.
            random_numbers.append(random_number)

    return random_numbers
