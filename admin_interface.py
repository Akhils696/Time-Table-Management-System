import tkinter as tk
from tkinter import messagebox

# Admin Interface Function
def open_admin_interface():
    admin_window = tk.Tk()
    admin_window.title("Admin Interface")
    admin_window.geometry("1000x800")
    admin_window.config(bg="#e8f8f5")

    # Title Label
    title_label = tk.Label(admin_window, text="Admin Control Panel", font=("Arial", 24, "bold"), bg="#148f77", fg="white")
    title_label.pack(pady=10)

    # Function to view the entire time table
    def view_time_table():
        try:
            with open("time_table.txt", "r") as file:
                time_table_data = file.readlines()
                time_table_text.delete(1.0, tk.END)
                for line in time_table_data:
                    time_table_text.insert(tk.END, line)
        except FileNotFoundError:
            messagebox.showerror("File Error", "Time table file not found.")

    # Function to add a time slot
    def add_time_slot():
        day = day_entry.get().capitalize()
        time = time_entry.get()
        subject = subject_entry.get().capitalize()
        teacher = teacher_entry.get().capitalize()

        if day == '' or time == '' or subject == '' or teacher == '':
            messagebox.showwarning("Input Error", "Please enter all fields.")
            return

        try:
            with open("time_table.txt", "a") as file:
                file.write(f"{day},{time},{subject},{teacher}\n")
            messagebox.showinfo("Success", "Time slot added successfully.")
        except:
            messagebox.showerror("File Error", "An error occurred")

    # Function to delete a time slot
    def delete_by_day_and_time():
        day = day_entry.get().strip().capitalize()
        time_slot = time_entry.get().strip()

        if day == '' or time_slot == '':
            messagebox.showwarning("Input Error", "Please enter both the day and the time slot.")
            return

        try:
            with open("time_table.txt", "r") as file:
                lines = file.readlines()

            new_lines = []
            entry_found = False
            for line in lines:
                line_parts = [part.strip() for part in line.split(",")]
                if len(line_parts) == 4:
                    entry_day, entry_time = line_parts[0:2]
                    if entry_day.lower() == day.lower() and entry_time == time_slot:
                        entry_found = True
                        continue  # Skip the matched entry
                    new_lines.append(line)
            if entry_found == False:
                messagebox.showinfo("Delete Status", "No matching time slot found for the given day and time.")
                return
            with open("time_table.txt", "w") as file:
                file.writelines(new_lines)
            messagebox.showinfo("Success", "Time slot deleted successfully.")
        except:
            messagebox.showerror("File Error", "An error occurred")

    def delete_by_subject():
        subject = subject_entry.get().strip().capitalize()

        if subject == '':
            messagebox.showwarning("Input Error", "Please enter the subject.")
            return

        try:
            with open("time_table.txt", "r") as file:
                lines = file.readlines()

            new_lines = []
            entry_found = False

            for line in lines:
                line_parts = [part.strip() for part in line.split(",")]
                if len(line_parts) == 4:

                    entry_subject = line_parts[2]
                    if entry_subject.lower() == subject.lower():
                        entry_found = True
                        continue  # Skip the matched subject
                    new_lines.append(line)
                

            if entry_found == False:
                messagebox.showinfo("Delete Status", "No entries found for the given subject.")
                return

            with open("time_table.txt", "w") as file:
                file.writelines(new_lines)

            messagebox.showinfo("Success", "All time slots for the subject have been deleted.")
        except:
            messagebox.showerror("File Error", "An error occurred")

    def delete_by_teacher():
        teacher = teacher_entry.get().strip().capitalize()
        if teacher == '':
            messagebox.showwarning("Input Error", "Please enter the teacher's name.")
            return
        try:
            with open("time_table.txt", "r") as file:
                lines = file.readlines()
            new_lines = []
            entry_found = False
            for line in lines:
                line_parts = [part.strip() for part in line.split(",")]
                if len(line_parts) == 4:

                    entry_teacher = line_parts[3]
                    if entry_teacher.lower() == teacher.lower():
                        entry_found = True
                        continue  # Skip the matched teacher
                    new_lines.append(line)
               

            if entry_found == False:
                messagebox.showinfo("Delete Status", "No entries found for the given teacher.")
                return

            with open("time_table.txt", "w") as file:
                file.writelines(new_lines)

            messagebox.showinfo("Success", "All time slots for the teacher have been deleted.")
        except:
            messagebox.showerror("File Error", "An error occurred")


    # Function to handle cancellation requests
    def handle_cancellations():
        try:
            with open("cancellations.txt", "r") as file:
                cancellations = file.readlines()

            if cancellations == []:
                messagebox.showinfo("No Requests", "No cancellation requests found.")
                return

            messagebox.showinfo("Cancellation Requests", "".join(cancellations))
        except:
            messagebox.showerror("File Error", "Cancellations file not found.")

    # Function to handle swap requests
    def handle_swaps():
        try:
            with open("swap_requests.txt", "r") as file:
                swaps = file.readlines()

            if swaps == []:
                messagebox.showinfo("No Requests", "No swap requests found.")
                return

            messagebox.showinfo("Swap Requests", "".join(swaps))
        except:
            messagebox.showerror("File Error", "Swap requests file not found.")

    # Frame for input fields
    input_frame = tk.Frame(admin_window, bg="#e8f8f5")
    input_frame.pack(pady=20)

    # Day Entry
    day_label = tk.Label(input_frame, text="Day:", font=("Arial", 14), bg="#e8f8f5")
    day_label.grid(row=0, column=0, padx=10, pady=5)
    day_entry = tk.Entry(input_frame, font=("Arial", 14))
    day_entry.grid(row=0, column=1, padx=10, pady=5)

    # Time Entry
    time_label = tk.Label(input_frame, text="Time:", font=("Arial", 14), bg="#e8f8f5")
    time_label.grid(row=1, column=0, padx=10, pady=5)
    time_entry = tk.Entry(input_frame, font=("Arial", 14))
    time_entry.grid(row=1, column=1, padx=10, pady=5)

    # Subject Entry
    subject_label = tk.Label(input_frame, text="Subject:", font=("Arial", 14), bg="#e8f8f5")
    subject_label.grid(row=2, column=0, padx=10, pady=5)
    subject_entry = tk.Entry(input_frame, font=("Arial", 14))
    subject_entry.grid(row=2, column=1, padx=10, pady=5)

    # Teacher Entry
    teacher_label = tk.Label(input_frame, text="Teacher:", font=("Arial", 14), bg="#e8f8f5")
    teacher_label.grid(row=3, column=0, padx=10, pady=5)
    teacher_entry = tk.Entry(input_frame, font=("Arial", 14))
    teacher_entry.grid(row=3, column=1, padx=10, pady=5)

    # Buttons for admin actions
    tk.Button(admin_window, text="View Time Table", font=("Arial", 14), command=view_time_table).pack(pady=5)
    tk.Button(admin_window, text="Add Time Slot", font=("Arial", 14), command=add_time_slot).pack(pady=5)
    tk.Button(admin_window, text="Delete by Day and Time", font=("Arial", 14), command=delete_by_day_and_time).pack(pady=5)
    tk.Button(admin_window, text="Delete by Subject", font=("Arial", 14), command=delete_by_subject).pack(pady=5)
    tk.Button(admin_window, text="Delete by Teacher", font=("Arial", 14), command=delete_by_teacher).pack(pady=5)
    tk.Button(admin_window, text="Handle Cancellations", font=("Arial", 14), command=handle_cancellations).pack(pady=5)
    tk.Button(admin_window, text="Handle Swaps", font=("Arial", 14), command=handle_swaps).pack(pady=5)
    
    # Text box for displaying the time table
    time_table_text = tk.Text(admin_window, height=15, width=80)
    time_table_text.pack(pady=10)

# Run Admin Interface

root = tk.Tk()
root.withdraw()
open_admin_interface()
root.mainloop()
