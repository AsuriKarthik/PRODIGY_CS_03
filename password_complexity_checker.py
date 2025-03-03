import tkinter as tk
from tkinter import messagebox
import re

def check_password_strength(password):
    # Initialize criteria flags
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[@$!%*?&]', password) is not None

    # Count the number of criteria met
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])

    # Determine password strength
    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Moderate"
    elif criteria_met == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    # Provide necessary feedback
    feedback = []
    if not length_criteria:
        feedback.append("At least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("At least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("At least one lowercase letter.")
    if not number_criteria:
        feedback.append("At least one number.")
    if not special_char_criteria:
        feedback.append("At least one special character (e.g., @$!%*?&).")

    return strength, feedback

def check_password():
    password = password_entry.get()
    strength, feedback = check_password_strength(password)

    # Prepare feedback message
    if feedback:
        feedback_message = "Your password is " + strength + ".\nIssues:\n" + "\n".join(feedback)
    else:
        feedback_message = "Your password is " + strength + ". It meets all the complexity requirements!"

    messagebox.showinfo("Password Strength", feedback_message)

def toggle_password():
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        toggle_button.config(text='Show')
    else:
        password_entry.config(show='')
        toggle_button.config(text='Hide')

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")
root.configure(bg="#f0f0f0")

# Create and place the password label and entry
password_label = tk.Label(root, text="Enter your password:", bg="#f0f0f0", font=("Helvetica", 12))
password_label.pack(pady=10)

password_entry = tk.Entry(root, show='*', width=30, font=("Helvetica", 12), bd=2, relief='solid')
password_entry.pack(pady=5)

# Create and place the toggle button
toggle_button = tk.Button(root, text='Show', command=toggle_password, font=("Helvetica", 12), bg="#4CAF50", fg="white", activebackground="#45a049")
toggle_button.pack(pady=5)

# Create and place the check button
check_button = tk.Button(root, text='Check Password', command=check_password, font=("Helvetica", 12), bg="#2196F3", fg="white", activebackground="#1e88e5")
check_button.pack(pady=20)

# Add a footer label
footer_label = tk.Label(root, text="Password must include uppercase, lowercase, numbers, and special characters.", bg="#f0f0f0", font=("Helvetica", 10))
footer_label.pack(side='bottom', pady=10)

# Run the application
root.mainloop()