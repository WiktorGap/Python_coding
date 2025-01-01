import tkinter as tk

root = tk.Tk()

tk.Label(root, text='Moja_Pierwsza_apka').grid(row=0, column=0, columnspan=2)

tk.Button(root, text='Zamknij Aplikacje', width=25, command=root.destroy).grid(row=1, column=0, columnspan=2, pady=10)

tk.Label(root, text='Nazwa zdjęcia').grid(row=2, column=0)
tk.Entry(root).grid(row=2, column=1)

tk.Label(root, text='Format zdjęcia').grid(row=3, column=0)
tk.Entry(root).grid(row=3, column=1)

root.mainloop()
