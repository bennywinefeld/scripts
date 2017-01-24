from Tkinter import *
import turtle

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.button_clicks = 0

    def createWidgets(self):        
        #self.QUIT.pack({"side": "left"})
        self.click_count = Button(self)
        self.click_count["text"]  = "Total clicks"
        self.click_count["command"] = self.updateCount
        #self.click_count.pack({"side": "left"})

        self.instruction = Label(self, text = "Enter radius")
        self.instruction.grid(row = 0, column=0, sticky = W)
        
        self.value1 = Entry(self)
        self.value1.grid(row=0,column=1,sticky=W)
        
        # Submit button
        self.submit_btn = Button(self,text="Submit",command= self.submit)
        self.submit_btn.grid(row=1,column=0,sticky=W)

        # Quit button
        self.quit_btn = Button(self,text="Quit",command=self.quit)
        self.quit_btn.grid(row=1,column=1,sticky=E)

    def updateCount(self):
        self.button_clicks += 1
        self.click_count["text"] = "Total clicks " + str(self.button_clicks)

    def submit(self):
        radius = int(self.value1.get())
        print "Value =", radius
        j.circle(radius)

# Create turtle objects
j = turtle.Turtle()


root = Tk()
root.title("My program")
root.geometry("200x200")
app = Application(master=root)
app.mainloop()
j.mainloop()
