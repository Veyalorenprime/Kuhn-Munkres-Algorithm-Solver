import tkinter as tk

class MatrixInput(tk.Frame):
    def __init__(self, parent, rows, columns):
        tk.Frame.__init__(self, parent)
        self.create_matrix_with_numbers(rows, columns)

    def _configure_matrix_frame(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def create_matrix_with_numbers(self, rows, columns):
        self._entry = {}

        self.canvas = tk.Canvas(self)
        self.matrix_frame = tk.Frame(self.canvas)
        self.vbar = tk.Scrollbar(self, orient='vertical')
        self.vbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.config(yscrollcommand=self.vbar.set)

        self.vbar.config(command=self.canvas.yview)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.canvas.create_window((0,0), window=self.matrix_frame, anchor='nw')
        self.matrix_frame.bind("<Configure>", self._configure_matrix_frame)

        for i in range(1, rows+1):
            for j in range(1, columns+1):
                if i == 1:
                    lbl = tk.Label(self.matrix_frame, text=j, font=("Helvetica", 12), width=3)
                    lbl.grid(row=0, column=j)
                if j == 1:
                    lbl = tk.Label(self.matrix_frame, text=i, font=("Helvetica", 12), width=3)
                    lbl.grid(row=i, column=0)
                entry = tk.Entry(self.matrix_frame, width=3)
                self._entry[(i-1, j-1)] = entry
                self._entry[(i-1, j-1)].grid(row=i, column=j)
    def get(self):
        return [[int(self._entry[i, j].get()) for j in range(self.columns)] for i in range(self.rows)]

