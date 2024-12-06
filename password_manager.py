import tkinter as tk
from tkinter import messagebox
import pickle


CREDENTIALS_FILE = "credentials.bin"
def load_credentials():
    with open(CREDENTIALS_FILE, "rb") as file:
        return pickle.load(file) 
    

def login_page(user_type):
    credentials = load_credentials() # Credentials dictionary
    login_window = tk.Tk()
    login_window.title(f"{user_type.capitalize()} Login")
    login_window.geometry("400x300")
    login_window.config(bg="#f0f0f5")

    tk.Label(login_window, text=f"{user_type.capitalize()} Login", font=("Arial", 18, "bold"), bg="#4d79ff", fg="white").pack(pady=10)

    username_entry = tk.Entry(login_window, font=("Arial", 14))
    username_entry.pack(pady=5)
    password_entry = tk.Entry(login_window, font=("Arial", 14), show="*")
    password_entry.pack(pady=5)

    def check_login():
        username = username_entry.get()
        password = password_entry.get()

        if username in credentials and credentials[username] == password:
            messagebox.showinfo("Login Successful", f"Welcome, {username}!")
            login_window.destroy()

            # Page import based on user type
            if user_type == "admin":
                from admin_interface import open_admin_interface
                open_admin_interface()
            elif user_type == "student":
                from student_interface import open_student_interface
                open_student_interface()
            elif user_type == "teacher":
                from teacher_interface import open_teacher_interface
                open_teacher_interface()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password!")

    tk.Button(login_window, text="Login", font=("Arial", 14), bg="#4d79ff", fg="white", command=check_login).pack(pady=10)
    tk.Button(login_window, text="Exit", font=("Arial", 14), bg="#ff6666", fg="white", command=login_window.quit).pack(pady=5)

    login_window.mainloop()
