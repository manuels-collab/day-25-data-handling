from tkinter import messagebox
from tkinter import *
from random import *
import pandas


BACKGROUND_COLOR = "#B1DDC6"
WHITE = '#FFFFFF'
BLACK = '#000000'
#Generate a word:
csv_file = 'data/french_words.csv'
read_file = pandas.read_csv(csv_file)
csv_dict = read_file.to_dict(orient='records')
word_created = []
def generate_word():

        global word_created
        random_word = choice(csv_dict)
        #Import and read data from the csv file using Pandas
        canvas.itemconfig(second_text, text=random_word['French'])
        canvas.itemconfig(flash_cards, image=my_img)
        word_created.append(random_word)
        window.after(3000, flip_card)
        canvas.itemconfig(first_text, text='French', fill=BLACK)
#Svaing Progress
def save_progress():
    generate_word()
    global csv_dict
    global word_created
    global csv_file
    new_file = [item for item in csv_dict if word_created[0] == item]
    csv_dict.remove(new_file[0])
    pandas_df = pandas.DataFrame(csv_dict)
    pandas_df.to_csv(csv_file, index=False, mode='w')
    print(pandas_df)
    
#Initailising the Window Module
window = Tk()
window.config(bg=BACKGROUND_COLOR)
window.maxsize(width=900, height=700,)
window.config(padx= 50, pady= 50)


canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR,  highlightthickness=0)
my_img = PhotoImage(file='images/card_front.png')
flash_cards =  canvas.create_image(400, 263,  image=my_img)
first_text = canvas.create_text(400, 150, text='',  font=("Ariel", 40, "italic"))
second_text = canvas.create_text(400, 263, text='',  font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file='images/wrong.png')
off_button =  Button(height=100, width=100,  image=wrong_img, command=generate_word,  bg=BACKGROUND_COLOR,  highlightthickness=0)
off_button.grid(row=1, column=0)


right_img = PhotoImage(file='images/right.png')
right_button =  Button(height=100, width=100, command=save_progress,  image=right_img,  bg=BACKGROUND_COLOR,  highlightthickness=0)
right_button.grid(row=1, column=1)

#Flipping of the Card
new_img = PhotoImage(file='images/card_back.png')
def flip_card():
    canvas.itemconfig(flash_cards, image=new_img)
    canvas.itemconfig(first_text, text='English', fill=WHITE)
    try:
        canvas.itemconfig(second_text, text=word_created[0]['English'])
    except IndexError:
        messagebox.showinfo(title='Error', message='Wait of the cards to flip')
    word_created.clear()


#Creating the flash cards
generate_word()














window.mainloop()