import time
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:


    def __init__(self,quizbrain_object):
        self.question = quizbrain_object

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score_txt = Label()
        self.score_txt.config(text=f"Score: {0}",bg=THEME_COLOR,font=("Roboto",14),fg="white")
        self.score_txt.grid(column=1,row=0,padx=20)

        self.question_canvas = Canvas()
        self.question_canvas.config(width=300,height=250)
        self.question_text = self.question_canvas.create_text(150,125,text="",font=("Arial",15,"italic"),fill=THEME_COLOR,width=300)
        self.question_canvas.grid(column=0,row=1,columnspan=2,pady=20)

        self.true_button = Button(width=100,height=97,command=lambda: self.check_answer("True"))
        self.true_img = PhotoImage(file="true.png")
        self.true_button.config(image=self.true_img,highlightthickness=0,bd=0)
        self.true_button.grid(column=0,row=3)

        self.false_button = Button(width=100,height=97,command=lambda: self.check_answer("True"))
        self.false_img = PhotoImage(file="false.png")
        self.false_button.config(image=self.false_img,highlightthickness=0,bd=0)
        self.false_button.grid(column=1,row=3)

        self.write_question_text()

        self.window.mainloop()


    def write_question_text(self):
        q_text = self.question.next_question()
        self.question_canvas.itemconfig(self.question_text,text=q_text)


    def check_answer(self, user_choice):
        try:
            if self.question.check_answer(user_choice):
                self.question_canvas.config(bg="green")
                self.score_txt.config(text=f"Score: {self.question.score}")
            else:
                self.question_canvas.config(bg="red")

            # Use after() to wait 1 second, then reset color and move to the next question
            self.window.after(1000, self.check_for_remaining_question)
        except IndexError:
            self.window.destroy()
            print(f"You Completed the Quiz! Your Score is: {self.question.score}/{self.question.question_number}")


    def check_for_remaining_question(self):
        self.question_canvas.config(bg="white")
        if self.question.still_has_questions():
            self.write_question_text()
        else:
            self.window.destroy()
            print(f"You Completed the Quiz! Your Score is: {self.question.score}/{self.question.question_number}")