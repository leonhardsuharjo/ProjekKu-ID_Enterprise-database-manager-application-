import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Window Switching App")

        # Create buttons to switch between windows
        self.button1 = tk.Button(root, text="Show Window 2", command=self.show_window2)
        self.button1.pack(pady=10)

        self.button2 = tk.Button(root, text="Show Window 1", command=self.show_window1)
        self.button2.pack(pady=10)

        # Create the first window
        self.window1 = tk.Toplevel(root)
        self.window1.title("Window 1")
        tk.Label(self.window1, text="This is Window 1").pack(pady=20)

        # Create the second window
        self.window2 = tk.Toplevel(root)
        self.window2.title("Window 2")
        tk.Label(self.window2, text="This is Window 2").pack(pady=20)
        self.window2.withdraw()  # Hide the second window initially

    def show_window1(self):
        self.window2.withdraw()  # Hide the second window
        self.window1.deiconify()  # Show the first window

    def show_window2(self):
        self.window1.withdraw()  # Hide the first window
        self.window2.deiconify()  # Show the second window

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()


