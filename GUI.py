from tkinter import*
from PIL import Image, ImageTk
import speech_to_text
import action

root = Tk()
root.title("AI Assistant")
root.geometry("550x675")
root.resizable(False, False)
root.config(bg="Light blue")

#ask function  
def ask():
    user_val = speech_to_text.speech_to_text()
    bot_val = action.Action(user_val)
    text.insert(END, "USER---->"+ user_val+"\n")
    if bot_val != None:
        text.insert(END, "BOT<----"+str(bot_val)+"\n")
    if bot_val == "ok sir":
        root.destroy()
        
    
def send():
    send = entry.get()
    bot = action.Action(send)
    text.insert(END, "USER---->"+send+"\n")
    if bot != None:
        text.insert(END, "BOT<----"+str(bot)+"\n")
    if bot == "ok sir":
        root.destroy()
    

def delete():
    text.delete('1.0', "end")

# frame 
frame = LabelFrame(root, padx=100, pady=7, borderwidth=3,  relief="raised")
frame.config(bg="Light blue")
frame.grid(row=0, column=1, padx=55, pady=10)

#text label

text_label = Label(frame, text="AI Assistant", font=("Times new roman", 14, "bold"))
text_label.grid(row=0, column=0, padx=20, pady=10)

#image label
image = ImageTk.PhotoImage(Image.open("assitant.png"))
image_label = Label(frame, image=image)
image_label.grid(row=1, column=0,pady=20)


#adding some text widget

text = Text(root, font=('courier 10 bold'), bg='Light blue')
text.grid(row=2, column=0 )
text.place(x=100, y=375, width=375, height=100)

#entry widget
entry = Entry(root, justify=CENTER)
entry.place(x=100, y=500, width=350, height=30)

#button 1
Button1 = Button(root, text="ASK", bg='Light blue', pady=16, padx=40, borderwidth=3, relief=SOLID, command=ask)
Button1.place(x=70, y=575)

#button 2
Button2 = Button(root, text="SEND", bg='Light blue', pady=16, padx=40, borderwidth=3, relief=SOLID, command=send)
Button2.place(x=400, y=575)

#button 3
Button3 = Button(root, text="DELETE", bg='Light blue', pady=16, padx=40, borderwidth=3, relief=SOLID, command=delete)
Button3.place(x=225, y=575)

root.mainloop()
