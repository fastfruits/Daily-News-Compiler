import tkinter as tk

voice = "Voice1"
news = ""

window = tk.Tk()
window.geometry("400x400")
window.title("AI-Personality")
window.configure(bg="#009CFF")
window.resizable(False, False)

def createWindow():
    label.pack()
    personality.pack()
    btnScience.pack()
    btnPolitics.pack()
    btnUS.pack()
    btnNature.pack()

    frame1.pack()
    window.mainloop()

def pickNewsType(newsType):
    news = newsType

frame1 = tk.Frame(
    master=window,
    width=100, 
    height=200,
    bg="#009CFF"
)
label = tk.Label(frame1, 
    text="Welcome to News Compiler!", 
    bg="#009CFF", 
    fg="white"
)
personality = tk.Entry(frame1, 
    width=100, 
)
btnScience = tk.Button(frame1, 
    width = 50,
    height = 5,
    bg="#009CFF", 
    text="Science",
    fg="white",
    command=pickNewsType("science")
)
btnPolitics = tk.Button(frame1, 
    width = 50,
    height = 5,
    bg="#009CFF", 
    text="Politics",
    fg="white",
    command=pickNewsType("Politics")
)
btnUS = tk.Button(frame1, 
    width = 50,
    height = 5,
    bg="#009CFF", 
    text="United States",
    fg="white",
    command=pickNewsType("United States")
)
btnNature = tk.Button(frame1, 
    width = 50,
    height = 5,
    bg="#009CFF", 
    text="Nature",
    fg="white",
    command=pickNewsType("Nature")
)

createWindow()