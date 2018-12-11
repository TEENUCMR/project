import tkinter as tk

r = tk.Tk()

v = tk.IntVar()

tk.Label(r, 
        text="""Choose an 
option:""",
        justify = tk.LEFT,
        padx = 20).pack()
tk.Radiobutton(r, 
              text="encrypt",
              padx = 20, 
              variable=v, 
              value=1).pack(anchor=tk.W)
tk.Radiobutton(r, 
              text="decrypt",
              padx = 20, 
              variable=v, 
              value=2).pack(anchor=tk.W)

r.title('secret message') 
button = tk.Button(r, text='Submit', width=25, command=r.destroy) 
button.pack() 

r.mainloop()
exit()