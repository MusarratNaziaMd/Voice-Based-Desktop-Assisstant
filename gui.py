from tkinter import*;
from PIL import Image ,ImageTk
import action
import speech_to_text
import text_to_speech
root=Tk();
root.title("AIZA - Your Voice Assistant");
root.geometry("600x750");
root.resizable(False,False)
root.config(bg="#0A0F2C");#adding color
def ask():
    user_val=speech_to_text.speech_to_text()
    aiza_val=action.Action(user_val)
    if user_val:
      response_text.insert(END, "User--->" + user_val + "\n")
    if aiza_val!=None:
        response_text.insert(END, "aiza<----" + str(aiza_val) + "\n")
    if aiza_val=="ok":
        root.destroy()


def send():
    send=user_entry.get()
    aiza=action.Action(send)
    response_text.insert(END,"User---->"  + send + "\n")
    if aiza!=None:
        response_text.insert(END,"aiza<----" + str(aiza) + "\n")
    if aiza=="ok":
        root.destroy()


def delete():
    response_text.delete("1.0","end")

def welcome_message():
    text_to_speech.text_to_speech("Hello! I am AIZA, your voice assistant. Click Ask or type a message to begin.")

#frame 
frame =LabelFrame(root,padx=20 , pady=20,borderwidth=2, relief="groove",bg="Midnight Blue",highlightcolor="Deep Sky Blue",highlightthickness=2)
#to center frame  horinzontaly by default
frame.pack(pady=50)
#frame.grid(row=0, column=1, padx=20 , pady=10)
#text label
text_label=Label(frame, text="AIZA Assistant ", font=("Segoe UI",18,"bold"),bg="Midnight Blue",fg="Deep Sky Blue") 
                 
text_label.pack(pady=(0,10))#centered default
sub_label = Label(root, text="Your Futuristic Voice Assistant",
                  font=("Segoe UI", 12, "italic"),
                  bg="navy blue", fg="light sky blue")
sub_label.pack()
#image 

image=Image.open("aiza.png")
image=image.resize((160,160))
photo=ImageTk.PhotoImage(image)
image_label=Label(frame, image=photo , bg="Midnight Blue")
image_label.pack(pady=10)
# Text area for AIZA's responses
response_label = Label(root, text="AIZA Says:", font=("Segoe UI", 12, "bold"),
                       bg="navy blue", fg="light sky blue")
response_label.pack(pady=(20, 5))

response_text = Text(root, height=6, width=50, font=("Segoe UI", 10),
                     bg="midnight blue", fg="white", wrap=WORD, relief=GROOVE, borderwidth=2)
response_text.pack()
# User input entry
input_label = Label(root, text="Your Message:", font=("Segoe UI", 12),
                    bg="navy blue", fg="white")
input_label.pack(pady=(20, 5))

user_entry = Entry(root, width=40, font=("Segoe UI", 10), bg="white", relief=GROOVE)
user_entry.pack(pady=5)

# Buttons: Ask, Send, Delete
button_frame = Frame(root, bg="navy blue")
button_frame.pack(pady=20)

ask_button = Button(button_frame, text="Ask", font=("Segoe UI", 10, "bold"),
                    bg="royal blue", fg="white", padx=20, pady=5,command=ask);
ask_button.grid(row=0, column=0, padx=10)

send_button = Button(button_frame, text="Send", font=("Segoe UI", 10, "bold"),
                     bg="dodger blue", fg="white", padx=20, pady=5,command=send)
send_button.grid(row=0, column=1, padx=10)
delete_button = Button(button_frame, text="Delete", font=("Segoe UI", 10, "bold"),
                       bg="crimson", fg="white", padx=20, pady=5,command=delete)
delete_button.grid(row=0, column=2, padx=10)
root.after(1000, welcome_message)


root.mainloop();