import tkinter as tk #creates windows, button, label
from tkinter import messagebox #shows pop up dialogs
from tabulate import tabulate #grid table

# Initialize the Student Interface window
def open_student_interface():
    student_window = tk.Tk()
    student_window.title("Student Interface")
    student_window.geometry("1000x800")
    student_window.config(bg="#eafaf1")

    # Title Label
    title_label = tk.Label(student_window, text="Student Time Table", font=("Arial", 20, "bold"), bg="#117a65", fg="white")
    title_label.pack(pady=10)

    # Function to view the time table
    def view_time_table():
        try:
            with open("time_table.txt", "r") as file:
                time_table_data = []
                for line in file.readlines():
                    time_table_data.append(line.strip().split(",")) #form a list
                               
                # Use tabulate to format data as a table
                headers = time_table_data[0]  # Assuming first line is header
                table_data = time_table_data[1:]
                formatted_table = tabulate(table_data, headers, tablefmt="grid") # data to grid like table
                
                # Display the formatted table in table_text widget
                table_text.delete(1.0, tk.END) #clears existing content before creating a table
                table_text.insert(tk.END, formatted_table) 
        
        except:
            messagebox.showerror("Error","An error occurred") #shows error when file is not found

    # Function to request class cancellation
    def request_cancellation():
        day = day_entry.get() #input for day and subject
        subject = subject_entry.get()

        if day == "" or subject == "":
            messagebox.showwarning("Input Error", "Please enter both day and subject.")
            return

        # Save the request in a text file
        try:
            with open("cancellations.txt", "a") as request_file:
                request_file.write(f"Cancellation Request - Day: {day}, Subject: {subject}\n")
            messagebox.showinfo("Request Submitted", "Your class cancellation request has been submitted.")
            return
        except Exception as e:
            messagebox.showerror("File Error", f"An error occurred: {e}") # if file is not found

    # Frame for input fields
    input_frame = tk.Frame(student_window, bg="#eafaf1")
    input_frame.pack(pady=20)

    # Day Entry
    day_label = tk.Label(input_frame, text="Enter Day:", font=("Arial", 14), bg="#eafaf1")
    day_label.grid(row=0, column=0, padx=10, pady=5)
    day_entry = tk.Entry(input_frame, font=("Arial", 14))
    day_entry.grid(row=0, column=1, padx=10, pady=5)

    # Subject Entry
    subject_label = tk.Label(input_frame, text="Enter Subject:", font=("Arial", 14), bg="#eafaf1")
    subject_label.grid(row=1, column=0, padx=10, pady=5)
    subject_entry = tk.Entry(input_frame, font=("Arial", 14))
    subject_entry.grid(row=1, column=1, padx=10, pady=5)

    # Buttons for actions
    btn_view = tk.Button(student_window, text="View Time Table", font=("Arial", 14), bg="#3498db", fg="white", command=view_time_table)
    btn_view.pack(pady=10)

    btn_request = tk.Button(student_window, text="Request Class Cancellation", font=("Arial", 14), bg="#e74c3c", fg="white", command=request_cancellation)
    btn_request.pack(pady=10)

    # Text box to display time table
    table_text = tk.Text(student_window, height=20, width=85, font=("Courier", 12))  # Changed font to Courier for alignment
    table_text.pack(pady=10)

    # Close Button
    close_btn = tk.Button(student_window, text="Close", font=("Arial", 14), bg="#f5b041", fg="white", command=student_window.destroy)
    close_btn.pack(pady=10)

# Testing the student interface locally
if __name__ == "__main__": #runs when executed directly and not as module
    root = tk.Tk() #create main window
    root.withdraw()  # Hide the main root window
    open_student_interface()
    root.mainloop() 
