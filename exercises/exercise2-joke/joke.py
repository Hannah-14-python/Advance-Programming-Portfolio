import tkinter as tk
import random

class JokeApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Random Joke Generator")
        self.master.geometry("400x300")
        self.master.configure(bg="#f0f0f0")  # Background color

        self.jokes = self.load_jokes()
        
        # Title label
        self.title_label = tk.Label(master, text="Random Joke Generator", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=(10, 20))

        # Setup label
        self.setup_label = tk.Label(master, text="", wraplength=350, font=("Arial", 14), bg="#f0f0f0")
        self.setup_label.pack(pady=(0, 10))

        # Punchline label
        self.punchline_label = tk.Label(master, text="", wraplength=350, font=("Arial", 14), bg="#f0f0f0")
        self.punchline_label.pack(pady=(0, 20))

        # Show punchline button
        self.show_punchline_button = tk.Button(master, text="Show Punchline", command=self.show_punchline, state=tk.DISABLED, bg="#4CAF50", fg="white", font=("Arial", 12))
        self.show_punchline_button.pack(pady=(0, 10))

        # New joke button
        self.new_joke_button = tk.Button(master, text="Get New Joke", command=self.get_new_joke, bg="#2196F3", fg="white", font=("Arial", 12))
        self.new_joke_button.pack(pady=(0, 10))

        # Quit button
        self.quit_button = tk.Button(master, text="Quit", command=master.quit, bg="#f44336", fg="white", font=("Arial", 12))
        self.quit_button.pack(pady=(0, 20))

        self.current_joke = None

    def load_jokes(self):
        try:
            with open("exercises/exercise2-joke/resources/randomJokes.txt", "r") as file:
                jokes = [line.strip() for line in file.readlines()]
                print(f"Loaded {len(jokes)} jokes.")  
                return jokes
        except FileNotFoundError:
            print("Joke file not found. Please ensure the path is correct.")
            return []

    def get_new_joke(self):
        if not self.jokes:
            self.setup_label.config(text="No jokes available.")
            return
        self.current_joke = random.choice(self.jokes)
        setup, _ = self.current_joke.split("?", 1)
        self.setup_label.config(text=setup)
        self.punchline_label.config(text="")
        self.show_punchline_button.config(state=tk.NORMAL)

    def show_punchline(self):
        _, punchline = self.current_joke.split("?", 1)
        self.punchline_label.config(text=punchline)
        self.show_punchline_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = JokeApp(root)
    root.mainloop()