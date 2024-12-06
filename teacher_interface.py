# teacher_interface.py

import tkinter as tk
from tkinter import messagebox
import re

# Initialize the Teacher Interface window
def open_teacher_interface():
    teacher_window = tk.Toplevel()
    teacher_window.title("Teacher Interface")
    teacher_window.geometry("1000x750")
    teacher_window.config(bg="#fef9e7")

    # Title Label
    title_label = tk.Label(teacher_window, text="Teacher Schedule", font=("Arial", 20, "bold"), bg="#b9770e", fg="white")
    title_label.pack(pady=10)

    # Function to view the teacher's schedule
    def view_schedule():
        try:
            with open("teacher_data.txt", "r") as file:
                teacher_data = file.readlines()
                schedule_text.delete(1.0, tk.END)
                for line in teacher_data:
                    schedule_text.insert(tk.END, line)
        except FileNotFoundError:
            messagebox.showerror("File Error", "Teacher data file not found.")

    # Function to request class cancellation
    def cancel_class():
        day = day_entry.get()
        subject = subject_entry.get()

        if not day or not subject:
            messagebox.showwarning("Input Error", "Please enter both day and subject.")
            return

        # Save the cancellation request
        try:
            with open("cancellations.txt", "a") as cancel_file:
                cancel_file.write(f"Cancellation - Day: {day}, Subject: {subject}\n")
            messagebox.showinfo("Cancellation Submitted", "Your class cancellation request has been submitted.")
        except Exception as e:
            messagebox.showerror("File Error", f"An error occurred: {e}")

    # Function to request a time slot swap
    def swap_class():
        day = day_entry.get()
        subject = subject_entry.get()
        swap_with = swap_entry.get()

        if not day or not subject or not swap_with:
            messagebox.showwarning("Input Error", "Please enter day, subject, and swap details.")
            return



        # Save the swap request
        try:
            with open("swap_requests.txt", "a") as swap_file:
                swap_file.write(f"Swap Request - Day: {day}, Subject: {subject}, Swap With: {swap_with}\n")
            messagebox.showinfo("Swap Request Submitted", "Your time slot swap request has been submitted.")
        except Exception as e:
            messagebox.showerror("File Error", f"An error occurred: {e}")

    # Frame for input fields
    input_frame = tk.Frame(teacher_window, bg="#fef9e7")
    input_frame.pack(pady=20)

    # Day Entry
    day_label = tk.Label(input_frame, text="Enter Day:", font=("Arial", 14), bg="#fef9e7")
    day_label.grid(row=0, column=0, padx=10, pady=5)
    day_entry = tk.Entry(input_frame, font=("Arial", 14))
    day_entry.grid(row=0, column=1, padx=10, pady=5)

    # Subject Entry
    subject_label = tk.Label(input_frame, text="Enter Subject:", font=("Arial", 14), bg="#fef9e7")
    subject_label.grid(row=1, column=0, padx=10, pady=5)
    subject_entry = tk.Entry(input_frame, font=("Arial", 14))
    subject_entry.grid(row=1, column=1, padx=10, pady=5)

    # Swap Entry
    swap_label = tk.Label(input_frame, text="Swap With (Subject):", font=("Arial", 14), bg="#fef9e7")
    swap_label.grid(row=2, column=0, padx=10, pady=5)
    swap_entry = tk.Entry(input_frame, font=("Arial", 14))
    swap_entry.grid(row=2, column=1, padx=10, pady=5)

    # Buttons for actions
    btn_view = tk.Button(teacher_window, text="View Schedule", font=("Arial", 14), bg="#3498db", fg="white", command=view_schedule)
    btn_view.pack(pady=10)

    btn_cancel = tk.Button(teacher_window, text="Cancel Class", font=("Arial", 14), bg="#e74c3c", fg="white", command=cancel_class)
    btn_cancel.pack(pady=10)

    btn_swap = tk.Button(teacher_window, text="Request Time Slot Swap", font=("Arial", 14), bg="#48c9b0", fg="white", command=swap_class)
    btn_swap.pack(pady=10)

    # Text box to display schedule
    schedule_text = tk.Text(teacher_window, height=15, width=70, font=("Arial", 12))
    schedule_text.pack(pady=10)

    # Close Button
    close_btn = tk.Button(teacher_window, text="Close", font=("Arial", 14), bg="#f5b041", fg="white", command=teacher_window.destroy)
    close_btn.pack(pady=10)


root = tk.Tk()
root.withdraw()  # Hide the main root window
open_teacher_interface()
root.mainloop()

