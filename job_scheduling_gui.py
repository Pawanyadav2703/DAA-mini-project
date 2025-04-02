import tkinter as tk
from tkinter import ttk, messagebox

# Function to perform Job Scheduling using Greedy Algorithm
def job_scheduling(jobs):
    if not jobs:
        return []

    # Sort jobs by profit in descending order
    jobs.sort(key=lambda x: x[1], reverse=True)

    # Get the maximum deadline
    max_deadline = max(job[2] for job in jobs)
    
    # Ensure at least one slot exists
    time_slots = [None] * max(1, max_deadline)  
    scheduled_jobs = []

    for job in jobs:
        job_id, profit, deadline = job
        for j in range(min(deadline, len(time_slots)) - 1, -1, -1):
            if time_slots[j] is None:
                time_slots[j] = job_id
                scheduled_jobs.append(job_id)
                break

    return scheduled_jobs

# Function to add job to the list
def add_job():
    job_id = job_id_entry.get().strip()
    profit = profit_entry.get().strip()
    deadline = deadline_entry.get().strip()

    if not job_id or not profit or not deadline:
        messagebox.showerror("Input Error", "Please enter all fields!")
        return

    try:
        profit = int(profit)
        deadline = int(deadline)
        if profit < 0 or deadline <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Input Error", "Profit must be positive and Deadline must be greater than zero!")
        return

    jobs.append((job_id, profit, deadline))
    
    # Insert into Table
    jobs_table.insert("", "end", values=(job_id, profit, deadline))
    
    # Clear Entry Fields
    job_id_entry.delete(0, tk.END)
    profit_entry.delete(0, tk.END)
    deadline_entry.delete(0, tk.END)

# Function to schedule jobs and display results
def schedule_jobs():
    if not jobs:
        messagebox.showerror("Error", "No jobs added!")
        return

    scheduled_jobs = job_scheduling(jobs)
    
    result_label.config(text="Scheduled Jobs: " + " → ".join(scheduled_jobs) if scheduled_jobs else "No Jobs Scheduled")

# Function to clear all jobs from the table
def clear_jobs():
    global jobs
    jobs = []
    jobs_table.delete(*jobs_table.get_children())  # Clear Table
    result_label.config(text="")  # Clear Result Label

# GUI Setup
root = tk.Tk()
root.title("Job Scheduling (Greedy Algorithm)")
root.geometry("500x550")
root.resizable(False, False)
root.configure(bg="#f5f5f5")  # Light gray background

# Title Label
title_label = tk.Label(root, text="Job Scheduling using Greedy Algorithm", font=("Arial", 14, "bold"), bg="#f5f5f5", fg="#333")
title_label.pack(pady=10)

# Input Frame
input_frame = tk.Frame(root, bg="#f5f5f5")
input_frame.pack(pady=5)

tk.Label(input_frame, text="Job ID:", bg="#f5f5f5", font=("Arial", 10)).grid(row=0, column=0, padx=5, pady=5)
job_id_entry = tk.Entry(input_frame, font=("Arial", 10))
job_id_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Profit:", bg="#f5f5f5", font=("Arial", 10)).grid(row=1, column=0, padx=5, pady=5)
profit_entry = tk.Entry(input_frame, font=("Arial", 10))
profit_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Deadline:", bg="#f5f5f5", font=("Arial", 10)).grid(row=2, column=0, padx=5, pady=5)
deadline_entry = tk.Entry(input_frame, font=("Arial", 10))
deadline_entry.grid(row=2, column=1, padx=5, pady=5)

add_job_button = tk.Button(input_frame, text="Add Job", command=add_job, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), padx=10)
add_job_button.grid(row=3, columnspan=2, pady=10)

# Table for Jobs
jobs = []
columns = ("Job ID", "Profit", "Deadline")
jobs_table = ttk.Treeview(root, columns=columns, show="headings", height=6)
for col in columns:
    jobs_table.heading(col, text=col)
    jobs_table.column(col, width=100, anchor="center")

jobs_table.pack(pady=10)

# Button Frame
button_frame = tk.Frame(root, bg="#f5f5f5")
button_frame.pack(pady=5)

schedule_button = tk.Button(button_frame, text="Schedule Jobs", command=schedule_jobs, bg="blue", fg="white", font=("Arial", 10, "bold"), padx=10)
schedule_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(button_frame, text="Clear Jobs", command=clear_jobs, bg="red", fg="white", font=("Arial", 10, "bold"), padx=10)
clear_button.grid(row=0, column=1, padx=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#f5f5f5", fg="#333")
result_label.pack(pady=10)

# Run the GUI Loop
root.mainloop()
