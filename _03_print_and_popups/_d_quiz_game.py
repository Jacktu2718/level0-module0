from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    user_score = 0
    simpledialog.message = user_score
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    user_answer = simpledialog.askstring(prompt="where is the best place to learn python?",title="answer")
    #      // 3.  Use an if statement to check if their answer is correct
    if user_answer == "The League":

    #      // 4.  if the user's answer was correct, add one to their score
        user_score += 1
    else:
        simpledialog.askstring(prompt="you are wrong!",title="answer")

    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    user_answer = simpledialog.askstring(prompt="how tall is the tallest building in meters?",title="answer")
    if user_answer == "828":
       user_score + 1
    else:
        simpledialog.askstring(prompt="you are wrong!",title="answer")


    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    user_answer = simpledialog.askstring(prompt="you are done!",title="answer")

    # Run the window's .mainloop() method
