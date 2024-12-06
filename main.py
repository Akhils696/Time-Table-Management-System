import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from password_manager import login_page

# Initialize the main window
root = tk.Tk()
root.title("College Time Table Management System")
root.geometry("1920x1080")
root.config(bg="#d4e6f1")

# Load the college logo
logo_path = "avv.jpg"
try:
    logo_image = Image.open(logo_path)
    logo_image = logo_image.resize((400, 100), Image.LANCZOS)
    logo_photo = ImageTk.PhotoImage(logo_image)
except:
    messagebox.showerror("Image Error", "Failed to load the logo image")
    logo_photo = None

# Create a frame for the header
header_frame = tk.Frame(root, bg="#154360", pady=20)
header_frame.pack(fill=tk.X)

# Display the logo image
if logo_photo:
    logo_label = tk.Label(header_frame, image=logo_photo, bg="#154360")
    logo_label.pack()

# Title Label
title_label = tk.Label(header_frame, text="College Time Table Management System",
                       font=("Arial", 24, "bold"), fg="white", bg="#154360")
title_label.pack(pady=10)

# Main menu frame
menu_frame = tk.Frame(root, bg="#d4e6f1", pady=30)
menu_frame.pack()

# Navigation Functions
def open_student_login():
    login_page("student")

def open_teacher_login():
    login_page("teacher")

def open_admin_login():
    login_page("admin")

# Navigation buttons
btn_student = tk.Button(menu_frame, text="Student", font=("Arial", 16), bg="#5dade2", fg="white", width=20, command=open_student_login)
btn_student.pack(pady=(50, 10))

btn_teacher = tk.Button(menu_frame, text="Teacher", font=("Arial", 16), bg="#48c9b0", fg="white", width=20, command=open_teacher_login)
btn_teacher.pack(pady=10)

btn_admin = tk.Button(menu_frame, text="Admin", font=("Arial", 16), bg="#f5b041", fg="white", width=20, command=open_admin_login)
btn_admin.pack(pady=10)

# Footer
footer_label = tk.Label(root, text="Developed by CSE-B", font=("Times", 12), bg="#d4e6f1")
footer_label.pack(side=tk.BOTTOM, pady=20)

# Run the Tkinter main loop
root.mainloop()

