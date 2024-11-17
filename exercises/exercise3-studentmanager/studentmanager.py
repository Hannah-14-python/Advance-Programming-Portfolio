import tkinter as tk
from tkinter import messagebox, ttk

class StudentManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Manager")
        self.root.geometry("600x600")
        self.root.configure(bg='lightblue')

        # Title
        self.title_label = tk.Label(root, text="Student Manager", font=("Arial", 36, "bold"), bg='lightblue')
        self.title_label.pack(pady=20)

        # Load student data
        self.students = self.load_student_data()

        # Buttons for viewing records
        self.option_frame = tk.Frame(root, bg='lightblue')
        self.option_frame.pack(pady=10)

        self.view_all_button = tk.Button(self.option_frame, text="View All Student Records", bg='grey', fg='white', width=30, command=self.view_all_records)
        self.view_all_button.grid(row=0, column=0, padx=10, pady=10)

        self.highest_score_button = tk.Button(self.option_frame, text="Show Highest Score", bg='grey', fg='white', width=30, command=self.show_highest_score)
        self.highest_score_button.grid(row=0, column=1, padx=10, pady=10)

        self.lowest_score_button = tk.Button(self.option_frame, text="Show Lowest Score", bg='grey', fg='white', width=30, command=self.show_lowest_score)
        self.lowest_score_button.grid(row=0, column=2, padx=10, pady=10)

        # Individual student record section
        self.individual_record_label = tk.Label(root, text="View Individual Student Record", bg='lightblue')
        self.individual_record_label.pack(pady=10)

        self.student_name_var = tk.StringVar()
        self.student_entry = ttk.Combobox(root, textvariable=self.student_name_var, values=[f"{s[1]} ({s[0]})" for s in self.students], width=30)
        self.student_entry.pack(pady=5)

        self.view_record_button = tk.Button(root, text="View Record", bg='grey', fg='white', command=self.view_record)
        self.view_record_button.pack(pady=5)

        self.record_display = tk.Text(root, height=10, width=50, bg='white')
        self.record_display.pack(pady=10)

    def load_student_data(self):
        students = []
        try:
            with open('exercises/exercise3-studentmanager/resources/studentMarks.txt', 'r') as file:
                num_students = int(file.readline().strip())
                for _ in range(num_students):
                    line = file.readline().strip()
                    parts = line.split(',')
                    student_code = int(parts[0].strip())
                    student_name = parts[1].strip()
                    coursework_marks = list(map(int, parts[2:5]))
                    exam_mark = int(parts[5].strip())
                    students.append((student_code, student_name, coursework_marks, exam_mark))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load student data: {e}")
        return students

    def calculate_student_record(self, student):
        student_code, student_name, coursework_marks, exam_mark = student
        total_coursework = sum(coursework_marks)
        total_marks = total_coursework + exam_mark
        overall_percentage = (total_marks / 160) * 100
        grade = self.calculate_grade(overall_percentage)
        return {
            "name": student_name,
            "code": student_code,
            "coursework": total_coursework,
            "exam": exam_mark,
            "percentage": overall_percentage,
            "grade": grade
        }

    def calculate_grade(self, percentage):
        if percentage >= 70:
            return 'A'
        elif percentage >= 60:
            return 'B'
        elif percentage >= 50:
            return 'C'
        elif percentage >= 40:
            return 'D'
        else:
            return 'F'

    def view_all_records(self):
        self.record_display.delete(1.0, tk.END)  
        total_percentage = 0
        num_students = len(self.students)

        for student in self.students:
            record = self.calculate_student_record(student)
            self.record_display.insert(tk.END, f"Name: {record['name']}\n")
            self.record_display.insert(tk.END, f"Student Number : {record['code']}\n")
            self.record_display.insert(tk.END, f"Total Coursework Mark: {record['coursework']}\n")
            self.record_display.insert(tk.END, f"Exam Mark: {record['exam']}\n")
            self.record_display.insert(tk.END, f"Overall Percentage: {record['percentage']:.2f}%\n")
            self.record_display.insert(tk.END, f"Grade: {record['grade']}\n")
            self.record_display.insert(tk.END, "-" * 40 + "\n")
            total_percentage += record['percentage']

        average_percentage = total_percentage / num_students if num_students > 0 else 0
        self.record_display.insert(tk.END, f"Total Students: {num_students}\n")
        self.record_display.insert(tk.END, f"Average Percentage: {average_percentage:.2f}%\n")

    def view_record(self):
        selected_student = self.student_name_var.get()
        if selected_student:
            student_code = int(selected_student.split('(')[-1].strip(')'))
            student = next((s for s in self.students if s[0] == student_code), None)
            if student:
                record = self.calculate_student_record(student)
                self.record_display.delete(1.0, tk.END)  # Clear previous content
                self.record_display.insert(tk.END, f"Name: {record['name']}\n")
                self.record_display.insert(tk.END, f"Student Number: {record['code']}\n")
                self.record_display.insert(tk.END, f"Total Coursework Mark: {record['coursework']}\n")
                self.record_display.insert(tk.END, f"Exam Mark: {record['exam']}\n")
                self.record_display.insert(tk.END, f"Overall Percentage: {record['percentage']:.2f}%\n")
                self.record_display.insert(tk.END, f"Grade: {record['grade']}\n")
            else:
                messagebox.showwarning("Selection Error", "Student not found.")
        else:
            messagebox.showwarning("Selection Error", "Please select a student.")

    def show_highest_score(self):
        if self.students:
            highest_student = max(self.students, key=lambda s: sum(s[2]) + s[3])
            record = self.calculate_student_record(highest_student)
            self.record_display.delete(1.0, tk.END)  # Clear previous content
            self.record_display.insert(tk.END, f"Highest Scoring Student:\n")
            self.record_display.insert(tk.END, f"Name: {record['name']}\n")
            self.record_display.insert(tk.END, f"Student Number: {record['code']}\n")
            self.record_display.insert(tk.END, f"Total Coursework Mark: {record['coursework']}\n")
            self.record_display.insert(tk.END, f"Exam Mark: {record['exam']}\n")
            self.record_display.insert(tk.END, f"Overall Percentage: {record['percentage']:.2f}%\n")
            self.record_display.insert(tk.END, f"Grade: {record['grade']}\n")
        else:
            messagebox.showwarning("Data Error", "No student records available.")

    def show_lowest_score(self):
        if self.students:
            lowest_student = min(self.students, key=lambda s: sum(s[2]) + s[3])
            record = self.calculate_student_record(lowest_student)
            self.record_display.delete(1.0, tk.END)  # Clear previous content
            self.record_display.insert(tk.END, f"Lowest Scoring Student:\n")
            self.record_display.insert(tk.END, f"Name: {record['name']}\n")
            self.record_display.insert(tk.END, f"Student Number: {record['code']}\n")
            self.record_display.insert(tk.END, f"Total Coursework Mark: {record['coursework']}\n")
            self.record_display.insert(tk.END, f"Exam Mark: {record['exam']}\n")
            self.record_display.insert(tk.END, f"Overall Percentage: {record['percentage']:.2f}%\n")
            self.record_display.insert(tk.END, f"Grade: {record['grade']}\n")
        else:
            messagebox.showwarning("Data Error", "No student records available.")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagerApp(root)
    root.mainloop()