import tkinter as tk
from tkinter import ttk
from typing import Literal
from settings.settings import ENTRY_SIZE, INITIAL_RANGE_END_REGULAR_NUMBER, INITIAL_RANGE_START_REGULAR_NUMBER, INITIAL_RANGE_SUPER_NUMBER_END, INITIAL_RANGE_SUPER_NUMBER_START, INITIAL_REGULAR_NUMBER_AMOUNT, INITIAL_SUPER_NUMBER_AMOUNT
from value_exception.value_exception import ValueException

class RandomLottoNumberGenerator(tk.Tk):

    """Basic tkinter lotto generator widget where all information are displayed on."""


    def __init__(self, generate_numbers_function: callable) -> None:
        super().__init__()
        
        self.generate_button = tk.Button(master= self,
                                         text= "Generate Lotto Numbers",
                                         command= lambda: self.generate_numbers())

        self.generate_button.pack(fill= tk.BOTH)

        tk.Button(master= self,
                  text= "Quit",
                  command= lambda: quit()).pack(fill= tk.BOTH)
       
        self.super_number_checkbox = ttk.Checkbutton(self, 
                                                    text= "Super Number?", 
                                                    command= lambda: self.change_super_number_entry_state())
        self.super_number_checkbox.pack(anchor=tk.W)

        self.number_input_frame = tk.Frame(master= self)
        self.number_input_frame.pack(fill= tk.BOTH)

        self.RANGE_START_REGULAR_NUMBER: int = INITIAL_RANGE_START_REGULAR_NUMBER
        self.RANGE_END_REGULAR_NUMBER: int = INITIAL_RANGE_END_REGULAR_NUMBER
        self.REGULAR_NUMBER_AMOUNT: int = INITIAL_REGULAR_NUMBER_AMOUNT

        self.RANGE_SUPER_NUMBER_START: int = INITIAL_RANGE_SUPER_NUMBER_START
        self.RANGE_SUPER_NUMBER_END: int = INITIAL_RANGE_SUPER_NUMBER_END
        self.SUPER_NUMBER_AMOUNT: int = INITIAL_SUPER_NUMBER_AMOUNT

        tk.Label(master= self.number_input_frame, 
                 text= "Regular Numbers Range Start: ",).grid(row= 0,
                                                              column= 0)
        tk.Label(master= self.number_input_frame, 
                 text= "Regular Numbers Range End: ").grid(row= 0, 
                                                           column= 2)
        tk.Label(master= self.number_input_frame, 
                 text= "Regular Numbers Amount: ").grid(row= 0, 
                                                        column= 4)

        self.regular_number_range_start_entry = tk.Entry(master= self.number_input_frame, 
                                                         width= ENTRY_SIZE, 
                                                         justify= tk.CENTER)
        self.regular_number_range_start_entry.grid(row= 0, 
                                                   column= 1)

        self.regular_number_range_start_entry.insert(0, self.RANGE_START_REGULAR_NUMBER)

        self.regular_number_range_end_entry = tk.Entry(master= self.number_input_frame, 
                                                width= ENTRY_SIZE, 
                                                justify= tk.CENTER)
        self.regular_number_range_end_entry.grid(row= 0, 
                                                 column= 3)

        self.regular_number_range_end_entry.insert(0, self.RANGE_END_REGULAR_NUMBER)

        self.regular_number_amount_entry = tk.Entry(master= self.number_input_frame, 
                                                    width= ENTRY_SIZE, 
                                                    justify= tk.CENTER)
        self.regular_number_amount_entry.grid(row= 0, 
                                              column= 5)

        self.regular_number_amount_entry.insert(0, self.REGULAR_NUMBER_AMOUNT)

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

        self.regular_numbers_label = tk.Label(master= self.result_frame, 
                                              justify= tk.LEFT)
        self.regular_numbers_label.pack(fill=tk.BOTH, 
                                        anchor=tk.W)

        self.super_number_label = tk.Label(master= self.result_frame, 
                                           justify= tk.LEFT)
        self.super_number_label.pack(fill= tk.BOTH, 
                                     anchor=tk.W)

        self.generate_numbers_function: callable = generate_numbers_function
        self.super_number_is_required: bool = False


    def __super_number_checkbox_selected(self) -> bool:

        """Checks the selection state of the super number checkbox. Returns true if selected, otherwise false"""

        return "selected" in self.super_number_checkbox.state()


    def change_super_number_entry_state(self) -> None:
        
        """Checks whether a super number is required or not according to the super number checkbox."""
        
        if self.__super_number_checkbox_selected():
            self.super_number_is_required = True
            self.__manage_super_number_entry_widget_state(tk.NORMAL)
        
        else:
            self.super_number_is_required = False
            self.__manage_super_number_entry_widget_state(tk.DISABLED)


    def __manage_super_number_entry_widget_state(self, new_state: Literal) -> None:
        
        """Manages the entry widgets for the super numbers depending on whether the super number checkbox is selected or not"""
        
        self.super_number_range_start_entry.config(state= new_state)
        self.super_number_range_end_entry.config(state= new_state)
        self.super_number_amount_entry.config(state= new_state)


    def __get_number_information(self) -> None:
        
        """Wrapper function to grab the numbers from the respective entry widgets and store them within instance variables."""
        
        self.__get_regular_numbers()
        self.__get_super_numbers()

    
    def __get_regular_numbers(self) -> None:

        """Gets the regular numbers from the respective entry widgets."""

        self.RANGE_START_REGULAR_NUMBER = int(self.regular_number_range_start_entry.get())
        self.RANGE_END_REGULAR_NUMBER = int(self.regular_number_range_end_entry.get())
        self.REGULAR_NUMBER_AMOUNT = int(self.regular_number_amount_entry.get())


    def __get_super_numbers(self) -> None:
        
        """Gets the super numbers from the respective entry widgets. Beforehand, it checks whether supernumbers are active or not."""

        if self.__super_number_checkbox_selected():
            self.RANGE_SUPER_NUMBER_START = int(self.super_number_range_start_entry.get())
            self.RANGE_SUPER_NUMBER_END = int(self.super_number_range_end_entry.get())
            self.SUPER_NUMBER_AMOUNT = int(self.super_number_amount_entry.get())

        else:
            return


    def generate_numbers(self) -> None:
        
        """Generates the random numbers either with or without supernumber. Updates the labels"""

        self.__get_number_information()
        self.__generate_super_numbers()
        self.__generate_regular_numbers()


    def __generate_super_numbers(self) -> None:

        """Generates the super numbers and updates the label"""

        if not self.super_number_is_required:

            self.super_number_label.config(text= "Super Number: -")
            return
        
        try:
            super_numbers = self.generate_numbers_function(range_start_number= self.RANGE_SUPER_NUMBER_START, 
                                                            range_end_number= self.RANGE_SUPER_NUMBER_END,
                                                            required_amount_of_numbers= self.SUPER_NUMBER_AMOUNT)

            self.update_label(numbers= super_numbers, 
                                string= "Super Number", 
                                number_label= self.super_number_label)
        
        except ValueException as value_error:
            self.update_label(string= value_error,
                              number_label= self.super_number_label)


    def __generate_regular_numbers(self) -> None:
 
        """Generates the regular numbers and updates the label"""

        try:
            regular_numbers = self.generate_numbers_function(range_start_number= self.RANGE_START_REGULAR_NUMBER, 
                                                             range_end_number= self.RANGE_END_REGULAR_NUMBER, 
                                                             required_amount_of_numbers= self.REGULAR_NUMBER_AMOUNT)
        
            self.update_label(numbers= regular_numbers,
                              string= "Regular Numbers", 
                              number_label= self.regular_numbers_label)
        
        except ValueException as value_error:
            self.update_label(string= value_error, 
                              number_label= self.regular_numbers_label)


    def update_label(self, string: str, number_label: tk.Label, numbers: int | list[int] = None) -> None:

        """Updates the label according to the numbers generated."""

        if numbers == None:
            number_label.config(text= string)

        else:
            number_label.config(text= f"{string}: {numbers}")