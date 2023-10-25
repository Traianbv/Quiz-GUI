from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)


        self.title = Label(text="Quiz Brain !", fg="white", bg=THEME_COLOR, pady=25, font=("Arial", 25, "bold"))
        self.title.grid(column=1, row=0)

        self.label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, pady=15, font=("Arial", 15, "bold"))
        self.label.grid(column=0, row=1)

        self.canvas = Canvas(width=500, height=250)
        self.text_question = self.canvas.create_text(250, 125, width=480, text="bum", font=("Arial", 15, "italic"))
        self.canvas.grid(column=0, columnspan=2, row=2)

        true_image = PhotoImage(file="images/true.png")
        self.button_ok = Button(image=true_image, command=self.true_answer)
        self.button_ok.grid(column=1, row=3, pady=15)

        false_image = PhotoImage(file="images/false.png")
        self.button_cross = Button(image=false_image, command=self.false_answer)
        self.button_cross.grid(column=0, row=3, pady=15 )

        self.get_next_question()


        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text_question, text=q_text)
        else:
            self.canvas.itemconfig(self.text_question, text="No more question")
            self.button_ok.config(state="disabled")
            self.button_cross.config(state="disabled")
    def true_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def false_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)




