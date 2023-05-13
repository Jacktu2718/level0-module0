from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Ask the user if they know how to write code.
    user_answer = simpledialog.askstring(prompt="do you know how to write a code",title="answer")
    # 2. If they say "yes", tell them they will rule the world in a message box pop-up.
    if user_answer == "yes":
        messagebox.showinfo(message="Nice job! you will rule the world",title="answer")
    # 3. Otherwise, tell them to sign up for classes at The League in an error box pop-up.
    else:
        messagebox.showinfo(message="sigh up classes at The League Ps: they are the best",title="answer")
    # Run the window's .mainloop() method
    window.mainloop()
