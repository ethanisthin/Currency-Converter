from forex_python.converter import CurrencyRates
import tkinter as tk
from tkinter import messagebox

def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_var.get().upper()
        to_currency = to_currency_var.get().upper()

        output = cr.convert(from_currency, to_currency, amount)
        rounded_output = round(output, 3)

        result_label.config(text=f"The converted rate is: {rounded_output} {to_currency}", fg="#3498db")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid amount.")

def exit_program():
    if messagebox.askokcancel("Exit", "Do you want to exit the program?"):
        root.destroy()

# Create the main window
root = tk.Tk()
root.title("Currency Converter v1.1")
root.configure(bg="#ecf0f1")  # Set background color

# Create CurrencyRates instance
cr = CurrencyRates()

# Currency options
currency_list = cr.get_rates('').keys()

# Create a frame for the main content area with a background color
content_frame = tk.Frame(root, bg="#ecf0f1")
content_frame.pack(padx=20, pady=20)

# Create and place GUI widgets with colors
amount_label = tk.Label(content_frame, text="Enter the amount to be converted:", bg="#ecf0f1")
amount_label.pack()

amount_entry = tk.Entry(content_frame)
amount_entry.pack()

from_currency_label = tk.Label(content_frame, text="Select the currency you are converting from:", bg="#ecf0f1")
from_currency_label.pack()

from_currency_var = tk.StringVar(value="USD")  # Default value
from_currency_menu = tk.OptionMenu(content_frame, from_currency_var, *currency_list)
from_currency_menu.pack()

to_currency_label = tk.Label(content_frame, text="Select the currency you want to convert to:", bg="#ecf0f1")
to_currency_label.pack()

to_currency_var = tk.StringVar(value="EUR")  # Default value
to_currency_menu = tk.OptionMenu(content_frame, to_currency_var, *currency_list)
to_currency_menu.pack()

convert_button = tk.Button(content_frame, text="Convert", command=convert_currency, bg="#27ae60", fg="white")
convert_button.pack()

result_label = tk.Label(content_frame, text="", font=("Helvetica", 14, "bold"), bg="#ecf0f1")
result_label.pack()

exit_button = tk.Button(content_frame, text="Exit", command=exit_program, bg="#e74c3c", fg="white")
exit_button.pack()

# Start the GUI event loop
root.mainloop()
