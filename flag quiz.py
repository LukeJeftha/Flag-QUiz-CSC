import tkinter as tk
from tkinter import messagebox
import random



flags = {
    "France": "C:/path/to/your/images/france.png",
    "Germany": "germany.png",
    "Japan": "japan.png",
    "United States": "usa.png",
    "United Kingdom": "uk.png",
    "Canada": "canada.png",
    "Brazil": "brazil.png",
    "Australia": "australia.png",
    "China": "china.png",
    "India": "india.png",
    "Russia": "russia.png",
    "South Africa": "south_africa.png",
    "Mexico": "mexico.png",
    "Italy": "italy.png",
    "Spain": "spain.png",
    "South Korea": "south_korea.png",
    "New Zealand": "new_zealand.png",
    "Argentina": "argentina.png",
    "Netherlands": "netherlands.png",
    "Sweden": "sweden.png",
    "Turkey": "turkey.png",
    "Saudi Arabia": "saudi_arabia.png"
}

class FlagQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Flag Quiz")
        self.root.geometry("400x400")  
        self.create_menu()
        self.reset_quiz()

    def create_menu(self):
        self.root.config(bg="#f0f0f0")  

        menu_frame = tk.Frame(self.root, bg="#f0f0f0")
        menu_frame.pack(pady=20)

        start_button = tk.Button(menu_frame, text="Start Quiz", command=self.start_quiz, bg="#4CAF50", fg="white", font=("Helvetica", 14, "bold"))
        start_button.pack(pady=10, padx=20)

    def reset_quiz(self):
        self.score = 0
        self.questions = list(flags.keys())
        self.current_question = None

    def start_quiz(self):
        self.create_quiz_frame()

    def create_quiz_frame(self):
        
        if hasattr(self, 'quiz_frame'):
            self.quiz_frame.destroy()
        
        self.quiz_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.quiz_frame.pack(pady=20)

        self.country_label = tk.Label(self.quiz_frame, text="Which country's flag is this?", bg="#f0f0f0", font=("Helvetica", 16, "bold"))
        self.country_label.pack(pady=10)

        self.flag_label = tk.Label(self.quiz_frame, bg="#f0f0f0")
        self.flag_label.pack(pady=10)

        self.answer_entry = tk.Entry(self.quiz_frame, font=("Helvetica", 14))
        self.answer_entry.pack(pady=10)

        enter_button = tk.Button(self.quiz_frame, text="Enter", command=self.check_answer, bg="#2196F3", fg="white", font=("Helvetica", 14, "bold"))
        enter_button.pack(pady=10, padx=20)

        self.next_button = tk.Button(self.quiz_frame, text="Next", command=self.next_question, bg="#FFC107", fg="black", font=("Helvetica", 14, "bold"))
        self.next_button.pack(pady=10, padx=20)
        self.next_button.config(state=tk.DISABLED)

        self.feedback_label = tk.Label(self.quiz_frame, text="", bg="#f0f0f0", font=("Helvetica", 14))
        self.feedback_label.pack(pady=10)

        self.next_question()

    def next_question(self):
        self.next_button.config(state=tk.DISABLED)
        self.feedback_label.config(text="")
        self.answer_entry.delete(0, tk.END)

        if not self.questions:
            self.end_quiz()
            return

        self.current_question = random.choice(self.questions)
        self.questions.remove(self.current_question)

       
        try:
           
            image = __import__.open(flags[self.current_question])
            
            image = image.resize((300, 150), image.ANTIALIAS)
            
            self.flag_image = __import__.PhotoImage(image)
            
            self.flag_label.config(image=self.flag_image)
            
            self.flag_label.image = self.flag_image
        except Exception as e:
            print(f"Error loading image: {e}")
            self.flag_label.config(text="Error loading image")

    def check_answer(self):
        answer = self.answer_entry.get().strip().lower()
        correct_answer = self.current_question.lower()

        if answer == correct_answer:
            self.feedback_label.config(text="Correct!", fg="green")
            self.score += 1
        else:
            self.feedback_label.config(text=f"Wrong! The correct answer was {self.current_question}.", fg="red")

        self.next_button.config(state=tk.NORMAL)

    def end_quiz(self):
        self.quiz_frame.destroy()
        play_again_button = tk.Button(self.root, text="Play Again", command=self.play_again, bg="#4CAF50", fg="white", font=("Helvetica", 14, "bold"))
        play_again_button.pack(pady=20)
        messagebox.showinfo("Quiz Finished", f"Your final score is: {self.score}/{len(flags)}")

    def play_again(self):
        
        self.root.children['!button'].destroy()  
        self.reset_quiz()
        self.start_quiz()

if __name__ == "__main__":
    root = tk.Tk()
    app = FlagQuiz(root)
    root.mainloop()
