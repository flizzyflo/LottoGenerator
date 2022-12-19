import random
from value_exception.value_exception import ValueException

def get_random_lotto_numbers(range_start_number: int, 
                             range_end_number: int, 
                             required_amount_of_numbers: int) -> list[int]:
    
    """Random number generator. Returns 0 if input parameter are not correct."""

    random_numbers: list[int] = list()

    if not input_values_correct(required_amount_of_numbers= required_amount_of_numbers,
                                range_end_number= range_end_number,
                                range_start_number= range_start_number):
        
        # raising exception avoids infinte loop
        raise ValueException(f"Error: '{range_end_number=}' - '{range_start_number=}' has to be >= '{required_amount_of_numbers=}'")

    while len(random_numbers) < required_amount_of_numbers:
        
        random_number = random.randint(range_start_number, range_end_number)
        
        if random_number in random_numbers:
            #number is already stored in numbers. numbers can not be doubled.
            continue
            
        else:
            #append random number to lotto numbers.
            random_numbers.append(random_number)

    return sorted(random_numbers)


def input_values_correct(range_start_number: int, range_end_number: int, required_amount_of_numbers: int) -> bool:
    
    """Checks the input values passed in to the randomizer"""

    return range_end_number - range_start_number + 1 >= required_amount_of_numbers