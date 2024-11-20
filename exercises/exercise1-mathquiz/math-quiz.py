import tkinter as tk
import random

class ArithmeticQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Arithmetic Quiz")
        self.root.configure(bg="#f0f0f0")
        self.score = 0
        self.question_count = 0
        self.difficulty = None
        self.current_problem = None

        self.menu_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.menu_frame.pack(pady=40)

        self.title_label = tk.Label(self.menu_frame, text="DIFFICULTY LEVEL", font=("Helvetica", 24, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=10)

        self.easy_button = tk.Button(self.menu_frame, text="Easy", command=lambda: self.start_quiz(1), width=20, bg="#d1e7dd", font=("Helvetica", 14))
        self.easy_button.pack(pady=10)

        self.moderate_button = tk.Button(self.menu_frame, text="Moderate", command=lambda: self.start_quiz(2), width=20, bg="#d1e7dd", font=("Helvetica", 14))
        self.moderate_button.pack(pady=10)

        self.advanced_button = tk.Button(self.menu_frame, text="Advanced", command=lambda: self.start_quiz(3), width=20, bg="#d1e7dd", font=("Helvetica", 14))
        self.advanced_button.pack(pady=10)

        self.result_frame = None

    def start_quiz(self, difficulty):
        self.difficulty = difficulty
        self.score = 0
        self.question_count = 0
        self.menu_frame.pack_forget()
        self.ask_question()

    def ask_question(self):
        if self.question_count < 10:
            self.current_problem = self.generate_problem()
            self.display_problem(self.current_problem)
        else:
            self.display_results()

    def generate_problem(self):
        num1 = self.random_int()
        num2 = self.random_int()
        operation = self.decide_operation()
        return (num1, num2, operation)

    def random_int(self):
        if self.difficulty == 1:
            return random.randint(0, 9)
        elif self.difficulty == 2:
            return random.randint(10, 99)
        else:
            return random.randint(1000, 9999)

    def decide_operation(self):
        return random.choice(['+', '-'])

    def display_problem(self, problem):
        num1, num2, operation = problem
        self.question_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.question_frame.pack(pady=20)

        question_text = f"{num1} {operation} {num2} = ?"
        self.question_label = tk.Label(self.question_frame, text=question_text, font=("Helvetica", 18), bg="#f0f0f0")
        self.question_label.pack(pady=10)

        self.answer_entry = tk.Entry(self.question_frame, font=("Helvetica", 16))
        self.answer_entry.pack(pady=5)

        self.submit_button = tk.Button(self.question_frame, text="Submit", command=lambda: self.check_answer(num1, num2, operation), bg="#d1e7dd", font=("Helvetica", 14))
        self.submit_button.pack(pady=10)

    def check_answer(self, num1, num2, operation):
        user_answer = self.answer_entry.get()
        self.answer_entry.delete(0, tk.END)

        if user_answer.lstrip('-').isdigit():
            user_answer = int(user_answer)
            correct_answer = eval(f"{num1} {operation} {num2}")

            if user_answer == correct_answer:
                self.score += 10
                self.question_count += 1
                self.is_correct("Correct! 10 points awarded.")
            else:
                self.is_correct("Incorrect! No points awarded.")
                self.question_count += 1
        else:
            self.is_correct("Please enter a valid number.")
            return

        self.ask_question()

    def is_correct(self, message):
        self.question_frame.pack_forget()
        self.feedback_label = tk.Label(self.root, text=message, font=("Helvetica", 16), bg="#f0f0f0")
        self.feedback_label.pack(pady=10)

    def display_results(self):
        self.question_frame.pack_forget()
        self.result_frame = tk.Frame(self.root, bg="#f0f 0f0")
        self.result_frame.pack(pady=20)

        result_text = f"Your final score: {self.score} / 100\n"
        if self.score >= 90:
            result_text += "Grade: A+"
        elif self.score >= 80:
            result_text += "Grade: A"
        elif self.score >= 70:
            result_text += "Grade: B"
        elif self.score >= 60:
            result_text += "Grade: C"
        else:
            result_text += "Grade: F"

        self.result_label = tk.Label(self.result_frame, text=result_text, font=("Helvetica", 18), bg="#f0f0f0")
        self.result_label.pack(pady=10)

        self.play_again_button = tk.Button(self.result_frame, text="Play Again", command=self.reset_quiz, width=20, bg="#d1e7dd", font=("Helvetica", 14))
        self.play_again_button.pack(pady=10)

    def reset_quiz(self):
        self.result_frame.pack_forget()
        self.menu_frame.pack(pady=40)

if __name__ == "__main__":
    root = tk.Tk()
    app = ArithmeticQuizApp(root)
    root.mainloop()