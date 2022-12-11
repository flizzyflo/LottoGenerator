import tkinter as tk
from tkinter import ttk
from typing import Literal
from settings.settings import ENTRY_SIZE

class RandomLottoNumberGenerator(tk.Tk):

    def __init__(self, 
                 generate_numbers_function: callable, 
                 ) -> None:
        super().__init__()
        
        self.generate_button = tk.Button(self,
                                         text= "Generate Lotto Numbers",
                                         command= lambda: self.generate_numbers())

        self.generate_button.pack(fill= tk.BOTH)
       
        self.super_number_checkbox = ttk.Checkbutton(self, 
                                                    text= "Want Super Number?", 
                                                    command= lambda: self.super_number_required())
        self.super_number_checkbox.pack(anchor=tk.W)

        self.number_input_frame= tk.Frame(master= self)
        self.number_input_frame.pack(fill= tk.BOTH)

        self.RANGE_START_NUMBER = 1
        self.RANGE_END_NUMBER = 49
        self.NUMBER_AMOUNT = 6

        self.RANGE_SUPER_NUMBER_START = 1
        self.RANGE_SUPER_NUMBER_END = 9
        self.SUPER_NUMBER_AMOUNT = 1

        tk.Label(master= self.number_input_frame, 
                 text= "Regular Numbers Range Start: ",).grid(row= 0,
                                                              column= 0)
        tk.Label(master= self.number_input_frame, 
                 text= "Regular Numbers Range End: ").grid(row= 0, 
                                                           column= 2)
        tk.Label(master= self.number_input_frame, 
                 text= "Regular Numbers Amount: ").grid(row= 0, 
                                                        column= 4)

        self.normal_number_range_start_entry = tk.Entry(master= self.number_input_frame, 
                                                  width= ENTRY_SIZE, 
                                                  justify= tk.CENTER)
        self.normal_number_range_start_entry.grid(row= 0, 
                                            column= 1)

        self.normal_number_range_start_entry.insert(0, self.RANGE_START_NUMBER)

        self.normal_number_range_end_entry = tk.Entry(master= self.number_input_frame, 
                                                width= ENTRY_SIZE, 
                                                justify= tk.CENTER)
        self.normal_number_range_end_entry.grid(row= 0, 
                                          column= 3)

        self.normal_number_range_end_entry.insert(0, self.RANGE_END_NUMBER)

        self.normal_number_amount_entry = tk.Entry(master= self.number_input_frame, 
                                             width= ENTRY_SIZE, 
                                             justify= tk.CENTER)
        self.normal_number_amount_entry.grid(row= 0, 
                                       column= 5)

        self.normal_number_amount_entry.insert(0, self.NUMBER_AMOUNT)

        tk.Label(master= self.number_input_frame, 
                 text= "Super Number Range Start: ").grid(row= 1, 
                                                           column= 0)
        tk.Label(master= self.number_input_frame, 
                 text= "Super Number Range End: ").grid(row= 1, 
                                                        column= 2)

        tk.Label(master= self.number_input_frame, 
                 text= "Super Number Amount: ").grid(row= 1, 
                                                     column= 4)

        self.super_number_range_start_entry = tk.Entry(master= self.number_input_frame, 
                                                 state= tk.DISABLED, 
                                                 width= ENTRY_SIZE, 
                                                 justify= tk.CENTER)

        self.super_number_range_start_entry.grid(row= 1, 
                                                 column= 1)

        self.super_number_range_end_entry = tk.Entry(master= self.number_input_frame, 
                                               state= tk.DISABLED, 
                                               width= ENTRY_SIZE, 
                                               justify= tk.CENTER)
        self.super_number_range_end_entry.grid(row= 1, 
                                         column= 3)

        self.super_number_amount_entry = tk.Entry(master= self.number_input_frame, 
                                            state= tk.DISABLED, 
                                            width= ENTRY_SIZE, 
                                            justify= tk.CENTER)
        self.super_number_amount_entry.grid(row= 1, 
                                      column= 5)

        self.result_frame = tk.Frame(master= self)
        self.result_frame.pack(fill= tk.BOTH)

        self.random_regular_numbers_label = tk.Label(master= self.result_frame, 
                                                     justify= tk.LEFT)
        self.random_regular_numbers_label.pack(fill=tk.BOTH, 
                                               anchor=tk.W)

        self.super_number_label = tk.Label(master= self.result_frame, 
                                           justify= tk.LEFT)
        self.super_number_label.pack(fill= tk.BOTH, 
                                     anchor=tk.W)

        self.generate_numbers_function = generate_numbers_function
        self.super_number_is_required = False


    def super_number_checkbox_selected(self) -> bool:
        return "selected" in self.super_number_checkbox.state()


    def super_number_required(self) -> None:
        
        """Checks whether a super number is required or not according to the super number checkbox."""
        
        if self.super_number_checkbox_selected():
            self.super_number_is_required = True
            self.manage_super_number_state(tk.NORMAL)
        
        else:
            self.super_number_is_required = False
            self.manage_super_number_state(tk.DISABLED)


    def manage_super_number_state(self, new_state: Literal) -> None:
        self.super_number_range_start_entry.config(state= new_state)
        self.super_number_range_end_entry.config(state= new_state)
        self.super_number_amount_entry.config(state= new_state)


    def get_number_ranges(self) -> None:
        self.RANGE_START_NUMBER = int(self.normal_number_range_start_entry.get())
        self.RANGE_END_NUMBER = int(self.normal_number_range_end_entry.get())
        self.NUMBER_AMOUNT = int(self.normal_number_amount_entry.get())

        if self.super_number_checkbox_selected():
            self.RANGE_SUPER_NUMBER_START = int(self.super_number_range_start_entry.get())
            self.RANGE_SUPER_NUMBER_END = int(self.super_number_range_end_entry.get())
            self.SUPER_NUMBER_AMOUNT = int(self.super_number_amount_entry.get())


    def generate_numbers(self) -> None:
        
        """Generates the random numbers either with or without supernumber. Updates the labels"""

        self.get_number_ranges()
        self.super_number_label.config(text= "Super Number: -")

        if self.super_number_is_required:
            super_numbers = self.generate_numbers_function(range_start_number= self.RANGE_SUPER_NUMBER_START, 
                                                               range_end_number= self.RANGE_SUPER_NUMBER_END,
                                                               required_amount_of_numbers= self.SUPER_NUMBER_AMOUNT)

            self.update_label(numbers= super_numbers, 
                              string= "Super Number", 
                              number_label= self.super_number_label)


        regular_numbers = self.generate_numbers_function(range_start_number= self.RANGE_START_NUMBER, 
                                                                range_end_number= self.RANGE_END_NUMBER, 
                                                                required_amount_of_numbers= self.NUMBER_AMOUNT)
        
        self.update_label(numbers= regular_numbers,
                          string= "Regular Numbers", 
                          number_label= self.random_regular_numbers_label)


    def update_label(self, numbers: int | list[int], string: str, number_label: tk.Label) -> None:

        if numbers == 0:
            number_label.config(text= f"'Range Max - Range Min' has to be bigger as or equal to the amount of numbers to  generate.")

        else:
            number_label.config(text= f"{string}: {numbers}")