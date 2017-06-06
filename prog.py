import tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    labels = ("P", "W", "G")
    entries = []
    for i in range(3):
        entries.append(tk.Entry(root))
        entries[i].grid(row=i, column=1)
        tk.Label(root, text=labels[i]).grid(row=i, column=0)
    result = tk.Label(root)
    result.grid(row=5, column=0, columnspan=2)
    tk.Button(root, command=lambda: result.config(
        text=sum([int(value.get()) * ((-1) ** n) for n, value in enumerate(entries)])),
              text="Calculate").grid(row=4, column=0, columnspan=2, sticky='ew')
    root.wm_title("Coefficients")
    root.mainloop()
