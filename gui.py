from tkinter import *
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from tkinter import messagebox

dec = None


def go():
    global dec
    query = ask_entry.get()

    if len(query) < 1:
        messagebox.showwarning("Oops!!",message='Query area is empty')

    else:
        text.delete("1.0", "end")
        url = f'http://www.google.com/search?q={ask_entry.get()}'
        # to get desktop site we can use requests_html
        session = HTMLSession()
        session.headers['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' \
                                        '(KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
        response = session.get(url, headers=session.headers)
        data = response.text

        soup = BeautifulSoup(data, 'html.parser')
        try:

            div = soup.find('div', class_='kno-rdesc')
            dec = div.find('span').text
        except AttributeError:
            messagebox.showinfo('Sorry!!!', message="Can't find any result")

        text.insert(END, chars=f'{dec}')


FONT = ('roboto', 15, 'bold')
window = Tk()
window.title('Scraper')
window.minsize(width=500, height=500)
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=176)
Img = PhotoImage(file='ask (2).png')
canvas.create_image(100, 88, image=Img)
canvas.grid(row=0, column=1, columnspan=2)

label = Label(text="Type your Query", font=FONT)
label.grid(row=1, column=1, sticky='n', pady=10)

ask_entry = Entry(width=45, )
ask_entry.grid(row=2, column=1, pady=10)

button = Button(text='SEARCH', command=go)
button.grid(row=3, column=1)

text = Text(height=9, width=60)
text.grid(row=4, column=1, pady=10)

window.mainloop()
