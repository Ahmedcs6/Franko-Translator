from tkinter import *
import arabic_reshaper
import bidi.algorithm

########## the dictionary #########

franko_dict = {
    'th': 'ث',
    'TH': 'ث',
    'dh': 'ذ',
    'DH': 'ذ',
    'sh': 'ش',
    'SH': 'ش',
    'gh': 'غ',
    'GH': 'غ',
    'a': 'ا',
    'A': 'ا',
    'b': 'ب',
    'B': 'ب',
    'c': 'ص',
    'C': 'ص',
    'd': 'د',
    'D': 'د',
    'e': 'ي',
    'E': 'ي',
    'f': 'ف',
    'F': 'ف',
    'g': 'ج',
    'G': 'ج',
    'h': 'ه',
    'H': 'ه',
    'i': 'إ',
    'I': 'إ',
    'j': 'ج',
    'J': 'ج',
    'k': 'ك',
    'K': 'ك',
    'l': 'ل',
    'L': 'ل',
    'm': 'م',
    'M': 'م',
    'n': 'ن',
    'N': 'ن',
    'o': 'و',
    'O': 'و',
    'q': 'ق',
    'Q': 'ق',
    'r': 'ر',
    'R': 'ر',
    's': 'س',
    'S': 'س',
    't': 'ت',
    'T': 'ت',
    'u': 'أ',
    'U': 'أ',
    'v': 'ڤ',
    'V': 'ڤ',
    'w': 'و',
    'W': 'و',
    'x': 'إكس',
    'X': 'إكس',
    'y': 'ي',
    'Y': 'ي',
    'z': 'ز',
    'Z': 'ز',
    ',': '،',
    '.': '.',
    '?': '؟',
    '!': '!',
    ' ': ' ',
    '\n': '\n',
    "6'": 'ط',
    "z'": 'ظ',
    "Z'": 'ظ',
    '5': 'خ',
    '6': 'ض',
    '7': 'ح',
    '9': 'ص',
    '2': 'ق',
    '3': 'ع',
}

########### the functions ########

def f():
    #getting the input text
    texti = input_text.get('1.0', END)
    #clear the output text befor any actions
    text1.delete('1.0', END)
    #replacing key with value if it exist
    for key, value in franko_dict.items():
        if key in texti:
        	texti = texti.replace(key, value)
    '''fixing arabic text to be readable
    it can be readable without that
    in python version > 3.7 '''
    reshap = arabic_reshaper.reshape(texti)
    bidi_text = bidi.algorithm.get_display(reshap)
    text1.insert(END, bidi_text)#inserting the final text in the output text widgt

########## the GUI part #########

win = Tk() #main window
win.config(bg="#BAFA2F",width=80,heigh=60)

########### the title label #########

title = Label(win,
                    text='Franko Translator',
                    fg="black",
                    bg="#FAF42F",
                    width=43,
                    heigh=3,
                    font=("Times New Roman",8)
                    )

title.grid(row=0,column=0)

########## the input text #########

input_text = Text(win,
                   height=20,
                   width=45,
                   bg="#FADB2F",
                   fg="black",
                   bd=6,
                   relief="raised",
                   insertbackground="black",
                   selectbackground="blue",
                   selectforeground="lightgreen",
                   font=("Times New Roman",7),
                   )

input_text.grid(row=1,column=0)

######### translator button ########

button = Button(win,
                   text="Translate",
                   activebackground='blue',
                   activeforeground="white",
                   background="#65FA2F",
                   bd=4,
                   highlightbackground="cyan",
                   highlightcolor="cyan",
                   highlightthickness=3,
                   relief="sunken",
                   command=f,
                   )

button.grid(row=2,column=0)

########## the output text ########  

text1 = Text(win,
                    height=20,
                    width=45,
                    bg="#FADB2F",
                    fg="black",
                    bd=6,
                    relief="raised",
                    insertbackground="black",
                    selectbackground="green",
                    selectforeground="lightblue",
                    font=("Times New Roman",7),
                    )
text1.grid(row=3,column=0)
win.mainloop()
