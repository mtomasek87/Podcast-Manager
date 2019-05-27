import feedparser
import urllib.request
from tkinter import *
import random

j = feedparser.parse('http://joeroganexp.joerogan.libsynpro.com/rss')
s = feedparser.parse('http://wakingup.libsyn.com/rss')
b = feedparser.parse('http://feeds.feedburner.com/theboogiemonster')

number = str(random.randint(0, 100))

window = Tk()

window.geometry('750x300')

window.title('Podcast Manager')

jre = j.entries
sam = s.entries
boogie = b.entries

lbl = Label(window, text='JRE')
lbl1 = Label(window, text='Making Sense')
lbl2 = Label(window, text='Boogie Monster')


def clicked():
    lb.delete('0', 'end')
    for i in jre:
        lb.insert(END, i.title, i.link)


def clicked1():
    lb.delete('0', 'end')
    for i in sam:
        lb.insert(END, i.title, i.links[1]['href'])


def clicked2():
    lb.delete('0', 'end')
    for i in boogie:
        lb.insert(END, i.title, i.links[0]['href'])


lbl.grid(column=0, row=0)
lbl1.grid(column=0, row=1)
lbl2.grid(column=0, row=2)
btn = Button(window, text="Show", command=clicked)
btn.grid(column=1, row=0)
btn1 = Button(window, text='Show', command=clicked1)
btn1.grid(column=1, row=1)
btn2 = Button(window, text='Show', command=clicked2)
btn2.grid(column=1, row=2)

lb = Listbox(window)
lb.grid(column=0, row=3, rowspan=5, sticky=W+E)

window.columnconfigure(0, weight=3)
window.columnconfigure(2, weight=1)


def when_selected(event):
    index = lb.curselection()[0]
    value = lb.get(index)
    return value


def download(event):
    urllib.request.urlretrieve((when_selected('<Double-Button-1>')), number + '.mp3')


lb.bind('<Double-Button-1>', download)


scrollbar = Scrollbar(window, jump=1)
scrollbar.grid(row=3, column=1, sticky=W, ipady=55)

lb.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lb.yview)

window.mainloop()
