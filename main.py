
from user_interface.main_window import RandomLottoNumberGenerator
from random_numbers.random_number_generator import get_random_lotto_numbers
import tkinter as tk

class test(tk.Tk):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

if __name__ == "__main__":
    root = RandomLottoNumberGenerator(generate_numbers_function= get_random_lotto_numbers)

    root.title("Lotto Game")
    root.mainloop()

