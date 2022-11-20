from tkinter import *
from controller import distribution
from operations import rational_calc

#Словарь текста и цвета кнопок в зависимости от их координат
button_params = {
    '11': ['', 'lightblue'],
    '12': ['(', 'lightblue'],
    '13': [')', 'lightblue'],
    '14': ['/', 'lightblue'],
    '21': ['7', 'lightgray'],
    '22': ['8', 'lightgray'],
    '23': ['9', 'lightgray'],
    '24': ['*', 'lightblue'],
    '31': ['4', 'lightgray'],
    '32': ['5', 'lightgray'],
    '33': ['6', 'lightgray'],
    '34': ['-', 'lightblue'],
    '41': ['1', 'lightgray'],
    '42': ['2', 'lightgray'],
    '43': ['3', 'lightgray'],
    '44': ['+', 'lightblue'],
    '51': ['0', 'lightgray'],
    '52': ['.', 'lightgray'],
    '53': ['j', 'lightgray'],
    '54': ['=', 'lightblue']
}

edit = ''

def clear_btn_click():
    edit.delete(0,END)    
    edit.insert(0,'0')

def result_button_click():
    calc_string = edit.get()
    edit.delete(0,END)    
    edit.insert(0,distribution(calc_string))

def on_click(event):
    button_text = event.widget.cget('text')
    if edit.get() == '0':
        edit.delete(0,END)
    edit.insert(len(edit.get()), button_text)
    
def window_init():
    global edit
    
    root = Tk()
    root.title("Калькулятор")
    root_width=300
    root_height=300
    
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()

    x = (sw - root_width) / 2
    y = (sh - root_height) / 2
    root.geometry(f"300x300+{int(x)}+{int(y)}") 
    edit = Entry()
    edit.configure(font=("Courier", 16, "bold"), justify=RIGHT)
    edit.insert(0,'0')
    edit.grid(row=0, column=0, columnspan=4, sticky="news", padx=5,pady=5)
    root.columnconfigure(0, weight=1)

   
    # Отрисовка кнопок
    btn_font=("Courier", 16, "bold")
    
    btn = Button(root, font=btn_font, text = '(')
    btn.bind(f'<Button>', on_click)
    btn.grid(column=0, row=1, sticky="news", padx=1, pady=1)

    btn = Button(root, font=btn_font, text = ')')
    btn.bind(f'<Button>', on_click)
    btn.grid(column=1, row=1, sticky="news", padx=1, pady=1)
    
    for x in range(1,5):
        for y in range(1,6):
            cur_text = button_params[str(y)+str(x)][0]
            btn = Button(root, font=btn_font, text = cur_text)
            btn.bind(f'<Button>', on_click)
            btn.configure(bg = button_params[str(y)+str(x)][1])
            btn.grid(column=x-1, row=y, sticky="news", padx=1, pady=1)
                    
    clear_btn = Button(root, font=btn_font, text = 'C', command = clear_btn_click)
    clear_btn.configure(bg = "pink")
    clear_btn.grid(column=0, row=1, sticky="news", padx=1,pady=1)
    
    result_btn = Button(root, font=btn_font, text = '=', command = result_button_click)
    result_btn.grid(column=3, row=5, sticky="news", padx=1, pady=1)
    
    root.columnconfigure(tuple(range(4)), weight=1)
    root.rowconfigure(tuple(range(6)), weight=1)

    root.mainloop()
