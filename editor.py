import tkinter as tk
from tkinter.filedialog import asksaveasfilename, askopenfilename
import os

def open_file(txt_edit, window):
    global current_file
    filepath = askopenfilename(
        filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')]
    )

    if not filepath:
        return
    
    txt_edit.delete(1.0, tk.END)
    with open(filepath, 'r') as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)

    window.title(f'Text Editor - {filepath}')
    current_file = filepath

def create_new_file(txt_edit, window):
    global current_file
    txt_edit.delete(1.0, tk.END)
    current_file = None
    window.title('Text Editor - New File')


def save_as_file(txt_edit, window):
    global current_file
    filepath = asksaveasfilename(
        filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')]
    )
    if not filepath:
        return

    with open(filepath, 'w') as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
        print("File saved as")

    window.title(f'Text Editor - {filepath}')
    current_file = filepath



def save_file(txt_edit, window):
    global current_file
    if current_file is not None and os.path.exists(current_file):

        with open(current_file, 'w') as output_file:
            text = txt_edit.get(1.0, tk.END)
            output_file.write(text)
            print("File saved")

    else:
        save_as_file(txt_edit, window)



def text_editor():
    window = tk.Tk()
    window.title('Text Editor ZC')
    window.rowconfigure(0, minsize=800, weight=1)
    window.columnconfigure(1, minsize=800, weight=1)

    txt_edit = tk.Text(window)
    fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)

    btn_open = tk.Button(fr_buttons, text='Open', command=lambda: open_file(txt_edit, window))
    btn_save = tk.Button(fr_buttons, text='Save', command=lambda: save_file(txt_edit, window))
    btn_new = tk.Button(fr_buttons, text='New', command=lambda: create_new_file(txt_edit, window))
    btn_save_as = tk.Button(fr_buttons, text='Save As.....', command=lambda: save_as_file(txt_edit, window))


    btn_open.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
    btn_save.grid(row=1, column=0, sticky='ew', padx=5, pady=5)
    btn_new.grid(row=2, column=0, sticky='ew', padx=5, pady=5)
    btn_save_as.grid(row=3, column=0, sticky='ew', padx=5, pady=5)

    fr_buttons.grid(row=0, column=0, sticky='ns')

    txt_edit.grid(row=0, column=1, sticky='nsew')

    window.mainloop()

if __name__ == '__main__':
    text_editor()