import tkinter as tk
from tkinter import messagebox

# Function to calculate the grade
def calculate_grade():
    # Define weights for each category
    weights = {
        "Homework": 0.20,
        "Assignments": 0.20,
        "Quizzes": 0.10,
        "Midterm": 0.20,
        "Final": 0.30
    }
    
    total_weighted_score = 0
    total_used_weight = 0  # Track the total weight of categories with valid scores
    
    # Get scores from the Entry widgets
    for category, weight in weights.items():
        score = entry_fields[category].get().strip()  # Get the score and remove any extra spaces
        if score:  # If the score is not empty
            try:
                score = float(score)
                if 0 <= score <= 100:
                    total_weighted_score += score * weight
                    total_used_weight += weight
                else:
                    messagebox.showerror("Error", f"Please enter a score between 0 and 100 for {category}.")
                    return
            except ValueError:
                messagebox.showerror("Error", f"Invalid input for {category}. Please enter a number.")
                return
    
    # If no scores were entered, show an error
    if total_used_weight == 0:
        messagebox.showerror("Error", "Please enter at least one score.")
        return
    
    # Adjust the total weighted score if some categories were skipped
    if total_used_weight < 1.0:
        total_weighted_score /= total_used_weight  # Normalize the score to account for missing weights
    
    # Determine the final grade
    if total_weighted_score >= 90:
        grade = "A"
    elif total_weighted_score >= 80:
        grade = "B"
    elif total_weighted_score >= 70:
        grade = "C"
    elif total_weighted_score >= 60:
        grade = "D"
    else:
        grade = "F"
    
    # Show the result in a pop-up window
    messagebox.showinfo("Grade Result", f"Your total weighted score is: {total_weighted_score:.2f}\nYour final grade is: {grade}")

# Create the main application window
root = tk.Tk()
root.title("Grade Calculator")
root.geometry("400x400")

# Create a label and entry fields for each category
entry_fields = {}
row = 0
for category in ["Homework", "Assignments", "Quizzes", "Midterm", "Final"]:
    label = tk.Label(root, text=f"{category} Score (0-100):")
    label.grid(row=row, column=0, padx=10, pady=5)
    
    entry = tk.Entry(root)
    entry.grid(row=row, column=1, padx=10, pady=5)
    entry_fields[category] = entry  # Store the Entry widget in a dictionary
    
    row += 1

# Create a button to calculate the grade
calculate_button = tk.Button(root, text="Calculate Grade", command=calculate_grade)
calculate_button.grid(row=row, column=0, columnspan=2, pady=20)

# Run the application
root.mainloop()