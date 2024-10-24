import tkinter as tk
import main

voice = "Voice1"
news = ""

window = tk.Tk()
window.geometry("400x400")
window.title("Daily News Compiler")
window.configure(bg="#009CFF")
window.resizable(False, False)

def createWindow():
    label.pack()
    btnScience.pack()
    btnPolitics.pack()
    btnTech.pack()
    btnNature.pack()
    btnGenerate.pack()

    frame1.pack()
    window.mainloop()

def pickNewsType(newsType):
    news = newsType
    print(news)
    return news

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
    command=pickNewsType("politics")
)
btnTech = tk.Button(frame1, 
    width = 50,
    height = 5,
    bg="#009CFF", 
    text="Technology",
    fg="white",
    command=pickNewsType("technology")
)
btnNature = tk.Button(frame1, 
    width = 50,
    height = 5,
    bg="#009CFF", 
    text="Nature",
    fg="white",
    command=pickNewsType("environment")
)

btnGenerate = tk.Button(frame1, 
    width = 50,
    height = 5,
    bg="#009CFF", 
    text="Science",
    fg="white",
    command=main.mainFunction()
)

createWindow()