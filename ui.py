from tkinter import *

class Ui():
    def __init__(self):
        self.window = Tk()
        self.window.minsize(width = 300, height = 300)
        self.window.title("coffee machine")
        self.window.config(pady=20,padx=20)

        self.canva = Canvas(height = 200, width = 300, bg = "white")
        #self.img = PhotoImage(file = "conffee_machine.png")
        #self.canva.create_image(280, 380, image = self.img)
        #self.big_text_bg = self.canva.create_rectangle(100,100,300,200, fill = "white")
        self.big_text = self.canva.create_text(100, 100,
                                               text = "big text",
                                               font = ("Arial", 20, "normal"))
        self.canva.grid(column=0, row=0, columnspan = 3)

        self.user_want_label = Label(text = "Your choice:" )
        self.user_want_label.grid(column = 0, row = 1)

        self.input_user_want = Entry(width= 10 ,bg = "white")
        self.input_user_want.grid(column = 0, row = 2)


        self.quarter_label = Label(width = 5, text = "quarter")
        self.quarter_label.grid(column = 1, row = 1)
        self.quarter_input = Entry(width=5)
        self.quarter_input.grid(column=2, row=1)

        self.dime_label = Label(width=5, text="dime")
        self.dime_label.grid(column=1, row=2)
        self.dime_input = Entry(width=5)
        self.dime_input.grid(column=2, row=2)

        self.nickel_label = Label(width=5, text="nickel")
        self.nickel_label.grid(column=1, row=3)
        self.nickel_input = Entry(width=5)
        self.nickel_input.grid(column=2, row=3)

        self.penny_label = Label(width=5, text="penny")
        self.penny_label.grid(column=1, row=4)
        self.penny_input = Entry(width=5)
        self.penny_input.grid(column=2, row=4)

        self.change = Label(text="change")
        self.change.grid(column=0, row=3)
        self.change_label = Label(width=10, text="change", bg = "white")
        self.change_label.grid(column=0, row=4)

        self.proceed_button = Button(width = 10, text = "Proceed", font = ("Arial", 15, "bold"), bg = "green")
        self.proceed_button.grid(column = 0, row = 5)

        self.window.mainloop()
