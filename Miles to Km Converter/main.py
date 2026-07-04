from tkinter import *  # Import everything from the tkinter module (for GUI)
from tkinter.ttk import Combobox  # Import Combobox widget for dropdown selection
import random  # Import the random module for generating random selections
from functions import Functions  # Import a custom Functions class that handles conversion logic

# Declare global variables for user choices and input value
global ch1, ch2, ch1_value

# Function to modify the main window's title and size
def modify_window():
    window.title("Miles to Km Converter")  # Set the window title
    window.geometry("300x100")  # Set the window dimensions

# Function to perform the conversion based on user selections
def convert_value():
    global ch1_value  # Reference the global variable for the input value
    ch1_value = choice_1_input.get()  # Get the value entered by the user

    # Call the value_converter function from the Functions class to perform the conversion
    result = function.value_converter(choice_1=ch1, value_1=ch1_value, choice_2=ch2)

    # Clear the text box that shows the result, then insert the converted value
    converted_value.delete("1.0", END)
    converted_value.insert("1.0", f"{round(result, 2)}")  # Insert the rounded result into the text box

# Function to update the available choices in the second dropdown based on the first selection
def update_available_conversions(event):
    global ch1  # Reference the global variable for the first user choice
    ch1 = user_choice_1.get()  # Get the selected value from the first dropdown

    # Call the valid_conversion_checker function to update valid conversions for the second dropdown
    function.valid_conversion_checker(ch1)
    user_choice_2["values"] = function.choices_2  # Update the second dropdown with valid choices
    function.choices_2 = function.choices_1.copy()  # Reset choices_2 for future use

# Function to set the second choice (conversion target) based on the user's selection
def setting_choice_2(event):
    global ch2  # Reference the global variable for the second user choice
    ch2 = user_choice_2.get()  # Get the selected value from the second dropdown

# Set the font to be used for labels and text boxes
FONT = ("Arial", 10)

# Create an instance of the Functions class to handle conversion logic
function = Functions()

# Initialize the main application window
window = Tk()
modify_window()  # Apply the window title and size modifications

# Create the first dropdown (choice 1) for the user to select a conversion category (e.g., miles, km)
user_choice_1 = Combobox(values=function.choices_1, width=10)
user_choice_1.set(random.choice(function.choices_1))  # Set a random default selection
user_choice_1.grid(column=2, row=0)  # Place the dropdown in the window
user_choice_1.bind("<<ComboboxSelected>>", func=update_available_conversions)  # Bind the selection event

# Create an input field where the user enters the value to be converted
choice_1_input = Entry(width=10)
choice_1_input.insert(0, "0")  # Set a default value of "0"
choice_1_input.grid(column=1, row=0)

# Label for showing "is equal to" text
equal_to_text = Label(text="is equal to", font=FONT)
equal_to_text.grid(column=0, row=1)

# Create the second dropdown (choice 2) for the user to select the conversion target (e.g., km)
user_choice_2 = Combobox(values=function.choices_1, width=10)
user_choice_2.grid(column=2, row=2)
user_choice_2.bind("<<ComboboxSelected>>", func=setting_choice_2)  # Bind the selection event

# Create a text box to display the converted value
converted_value = Text(height=1, width=8, font=FONT)
converted_value.insert("1.0", "0")  # Set a default value of "0"
converted_value.grid(column=1, row=2)

# Create a button to trigger the conversion when clicked
calc_button = Button(text="Calculate", command=convert_value)
calc_button.grid(column=1, row=3)

# Start the main event loop to keep the window open and responsive
window.mainloop()