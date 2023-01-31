#  Name :- Amit Yadav  Email id :- amityadavbsc39@gmail.com
# python minor project given in AI training course
#  project title :- create a countdown timer using python

# importing gui modules


import tkinter as tk
import datetime


# creating a countdown class
class Countdown(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.create_widgets()
        self.show_widgets()
        self.seconds_left=0
        self._timer_on=False
    def show_widgets(self):
        self.Label.pack()
        self.Entry.pack()
        self.start.pack()
        self.reset.pack()
        self.stop.pack()
        self.resume.pack()


    def create_widgets(self):
        self.Label=tk.Label(self,text=" Enter the time in seconds .")
        self.Entry=tk.Entry(self,justify="center")
        self.Entry.focus_set()
        self.reset=tk.Button(self,text="Reset  ",command=self.reset_button)

        self.start = tk.Button(self, text="Start", command=self.start_button)

        self.stop = tk.Button(self, text="Stop / Pause ", command=self.stop_button)

        self.resume = tk.Button(self, text="Resume", command=self.resume_button)

    def countdown(self):
        self.Label["text"]=self.convert_seconds_left_to_time()

        if self.seconds_left:
            self.seconds_left-=1
            self._timer_on=self.after(1000,self.countdown)
        else:
            self._timer_on=False
            self.Label["text"]=" Time Up !"

    def reset_button(self):
        self.seconds_left=0
        self.stop_timer()
        self._timer_on=False
        self.Label["text"]="Enter the time in seconds."
        self.start.forget()
        self.reset.forget()
        self.stop.forget()
        self.stop.forget()
        self.start.pack()
        self.reset.pack()
        self.stop.pack()
        self.resume.pack()

    def stop_button(self):
        self.seconds_left = int(self.Entry.get())
        self.stop_timer()



    def resume_button(self):
        self.seconds_left = int(self.Entry.get())
        self.resume_timer()


    def start_button(self):
        self.seconds_left= int(self.Entry.get())
        self.stop_timer()
        self.countdown()
        self.start.forget()
        self.reset.forget()
        self.stop.forget()
        self.resume.forget()
        self.start.pack()
        self.reset.pack()
        self.stop.pack()
        self.resume.pack()

    def stop_timer(self):
        if self._timer_on:
            self.after_cancel(self._timer_on)
            self._timer_on = False


    def resume_timer(self):
       if self.seconds_left!=0:
            self.seconds_left-=1
            self._timer_on=self.after(1000,self.countdown)

       else:
            self._timer_on=False
            self.Label["text"]=" Time Up !"





    def convert_seconds_left_to_time(self):
        return datetime.timedelta(seconds=self.seconds_left)


#main loop
if __name__=="__main__":
    root=tk.Tk()
    root.geometry("600x600")
    root.resizable(True,True)
    countdown=Countdown(root)
    countdown.pack()
    root.mainloop()
























