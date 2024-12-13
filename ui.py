import tkinter as tk
from queue import Queue
import main

news = ""
duration = 0
generate = False
generate_q = Queue()

window = tk.Tk()
window.geometry("600x800")
window.title("Daily News Compiler")
window.configure(bg="#009CFF")
window.resizable(False, False)

def createWindow():
    label.pack()
    btnSmall.pack()
    btnMedium.pack()
    btnLarge.pack()
    btnScience.pack()
    btnPolitics.pack()
    btnTech.pack()
    btnNature.pack()
    btnGenerate.pack()

    frame1.pack()
    frame2.pack()
    window.mainloop()

def button_callbackT():
    generate_q.put(True)
    generate_q.put(False)
def setGenerate():
    if generate == False:
        generate = True
    generate = False


def pickNewsType(newsType):
    news = newsType
    print(news)

def changeSize(size):
    duration = size
    print(duration)

frame1 = tk.Frame(
    master = window,
    width = 100, 
    height = 200,
    bg = "#009CFF"
)
frame2 = tk.Frame(
    master = window,
    width = 100,
    height = 200,
    bg = "#009CFF"
)
label = tk.Label(frame1, 
    text = "Welcome to News Compiler!", 
    bg = "#009CFF", 
    fg = "white"
)
btnSmall = tk.Button(frame1,
    width = 50,
    height = 5,
    bg = "#009CFF",
    fg = "white",
    text = "Small(~500 Words/5:00 Runtime)", 
    command = changeSize(500)     
)
btnMedium = tk.Button(frame1,
    width = 50,
    height = 5,
    bg = "#009CFF",
    fg = "white",
    text = "Medium(~1000 Words/10:00 Runtime)",
    command = changeSize(1000)     
)
btnLarge = tk.Button(frame1,
    width = 50,
    height = 5,
    bg = "#009CFF",
    fg = "white",
    text = "Large(~1500 Words/15:00 Runtime)",
    command = changeSize(1500)     
)
btnScience = tk.Button(frame1, 
    width = 50,
    height = 5,
    bg = "#009CFF", 
    text = "Science",
    fg = "white",
    command = pickNewsType("science")
)
btnPolitics = tk.Button(frame1, 
    width = 50,
    height = 5,
    bg = "#009CFF", 
    text = "Politics",
    fg = "white",
    command = pickNewsType("politics")
)
btnTech = tk.Button(frame1, 
    width = 50,
    height = 5,
    bg = "#009CFF", 
    text = "Technology",
    fg = "white",
    command = pickNewsType("technology")
)
btnNature = tk.Button(frame1, 
    width = 50,
    height = 5,
    bg = "#009CFF", 
    text = "Nature",
    fg = "white",
    command = pickNewsType("environment")
)

btnGenerate = tk.Button(frame1, 
    width = 50,
    height = 5,
    bg = "#009CFF", 
    text = "Generate Snippet",
    fg = "white",
    #command = button_callbackT()
    command = main.mainFunction()
)

createWindow()