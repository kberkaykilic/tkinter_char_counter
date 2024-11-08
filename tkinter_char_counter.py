import tkinter as tk


def result_count():
    user_input = entry1.get()
    char_count = {}
    for c in user_input:
        current_count = char_count.get(c, 0)
        char_count[c] = current_count + 1
    label2.configure(text=str(char_count))


win = tk.Tk()
win.title("Char Counter")
win.iconbitmap("python.ico")  # If code is not running, try to create your own path.

label1 = tk.Label(win, text="Enter a message:")
label1.pack(padx=5, pady=5)
entry1 = tk.Entry(win)
entry1.pack(padx=5, pady=5)
button1 = tk.Button(win, text="Count Occurrences", command=result_count)
button1.pack(padx=5, pady=5)
label2 = tk.Label(win)
label2.pack(padx=5, pady=5)

win.mainloop()
