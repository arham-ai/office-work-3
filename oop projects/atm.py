class Atm:
    def __init__(self):
        self.pin = None  # Initialize self.pin
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input('''
                          Hello, how would you like to proceed?
                         1. Enter 1 to create PIN.
                         2. Enter 2 to deposit.
                         3. Enter 3 to withdraw.
                         4. Enter 4 to check balance.
                         5. Enter 5 to exit.
                         ''')
        
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.deposit()
        elif user_input == "3":
            self.withdraw
        elif user_input == "4":
            self.check_balace
        else:
            print("Bye")
    def create_pin(self):
        self.pin=input("enteryour pin")
        print("pin set sucessfully")
    def deposit(self):
        temp = input("enter your pin")
        if temp==self.pin:
            amount =int(input("enter the amount"))
            self.balance=self.balance + amount
            print("deposit successfull")
        else:
            print("invalid pin")
    def withdraw(self):
         temp = input("enter your pin")
         if temp==self.pin:
             amount=int(input("enter the amount"))
             if amount is self.balance:
                 self.balance=self.balance - amount
                 print("operation sucessful")
    def check_balace(self):
         temp = input("enter your pin")
         if temp==self.pin:
             print(self.balance)
         else:
             print("invalid pin")
import tkinter as tk
from tkinter import messagebox

class AtmGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("ATM Machine")
        
        self.pin = None
        self.balance = 0
        
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Welcome to ATM Machine", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.pin_label = tk.Label(self.master, text="Enter PIN:")
        self.pin_label.pack()
        self.pin_entry = tk.Entry(self.master, show="*")
        self.pin_entry.pack()

        self.submit_button = tk.Button(self.master, text="Submit", command=self.authenticate_pin)
        self.submit_button.pack(pady=5)

    def authenticate_pin(self):
        entered_pin = self.pin_entry.get()
        if self.pin is None:
            self.pin = entered_pin
            messagebox.showinfo("PIN Set", "PIN set successfully.")
            self.pin_entry.delete(0, tk.END)
        elif entered_pin == self.pin:
            self.show_menu()
        else:
            messagebox.showerror("Error", "Invalid PIN.")
            self.pin_entry.delete(0, tk.END)

    def show_menu(self):
        self.label.config(text="Select an option:")
        self.pin_label.pack_forget()
        self.pin_entry.pack_forget()
        self.submit_button.pack_forget()

        options = ["Deposit", "Withdraw", "Check Balance", "Exit"]
        for option in options:
            button = tk.Button(self.master, text=option, command=lambda o=option: self.handle_option(o))
            button.pack(pady=5)

    def handle_option(self, option):
        if option == "Deposit":
            self.deposit()
        elif option == "Withdraw":
            self.withdraw()
        elif option == "Check Balance":
            self.check_balance()
        elif option == "Exit":
            self.master.destroy()

    def deposit(self):
        amount = tk.simpledialog.askinteger("Deposit", "Enter deposit amount:")
        if amount is not None and amount > 0:
            self.balance += amount
            messagebox.showinfo("Success", f"Deposit of {amount} made successfully. New balance: {self.balance}")
        else:
            messagebox.showerror("Error", "Invalid amount.")

    def withdraw(self):
        amount = tk.simpledialog.askinteger("Withdraw", "Enter withdrawal amount:")
        if amount is not None and amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                messagebox.showinfo("Success", f"Withdrawal of {amount} made successfully. New balance: {self.balance}")
            else:
                messagebox
