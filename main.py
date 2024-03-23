from tkinter import *
import os

selectedBook = 1


def setBook(number):
    global selectedBook
    global text1, text2, text3
    selectedBook = number
    
    if number == 1:
        if os.path.exists("book1.txt"):
            txtscreen.delete('1.0', END)
            bookfile = open("book1.txt", "r")
            content = bookfile.read()
            txtscreen.insert(END, content)
            bookfile.close()
            text1.destroy()
            text2.destroy()
            text3.destroy()

            text1 = Button(scrn, width= 21, height= 5, text= "Book #1", background= "Red", command =lambda:setBook(1))
            text1.place(x=155, y=485)
            text2 = Button(scrn, width= 21, height= 5, text= "Book #2", background= "Light Blue", command =lambda:setBook(2))
            text2.place(x=310, y=485)
            text3 = Button(scrn, width= 21, height= 5, text= "Book #3", background= "Light Blue", command =lambda:setBook(3))
            text3.place(x=465, y=485)

            scrn.update()
        else:
            bookfile = open("book1.txt", "w")
        bookfile.close()

    elif number == 2:
        if os.path.exists("book2.txt"):
            txtscreen.delete('1.0', END)
            bookfile = open("book2.txt", "r")
            content = bookfile.read()
            txtscreen.insert(END, content)
            bookfile.close()
            text1.destroy()
            text2.destroy()
            text3.destroy()

            text1 = Button(scrn, width= 21, height= 5, text= "Book #1", background= "Light Blue", command =lambda:setBook(1))
            text1.place(x=155, y=485)
            text2 = Button(scrn, width= 21, height= 5, text= "Book #2", background= "Red", command =lambda:setBook(2))
            text2.place(x=310, y=485)
            text3 = Button(scrn, width= 21, height= 5, text= "Book #3", background= "Light Blue", command =lambda:setBook(3))
            text3.place(x=465, y=485)
            scrn.update()
        else:
            bookfile = open("book2.txt", "w")
        bookfile.close()
    elif number == 3:
        if os.path.exists("book3.txt"):
            txtscreen.delete('1.0', END)
            bookfile = open("book3.txt", "r")
            content = bookfile.read()
            txtscreen.insert(END, content)
            bookfile.close()
            text1.destroy()
            text2.destroy()
            text3.destroy()

            text1 = Button(scrn, width= 21, height= 5, text= "Book #1", background= "Light Blue", command =lambda:setBook(1))
            text1.place(x=155, y=485)
            text2 = Button(scrn, width= 21, height= 5, text= "Book #2", background= "Light Blue", command =lambda:setBook(2))
            text2.place(x=310, y=485)
            text3 = Button(scrn, width= 21, height= 5, text= "Book #3", background= "Red", command =lambda:setBook(3))
            text3.place(x=465, y=485)
            scrn.update()
        else:
            bookfile = open("book3.txt", "w")
        bookfile.close()

def saveBook(number):
    if number == 1:
        bookfile = open("book1.txt", "w")
        INPUT = txtscreen.get("1.0", "end-1c")
        bookfile.write(INPUT)
        bookfile.close()
        scrn.update()
    elif number == 2:
        bookfile = open("book2.txt", "w")
        INPUT = txtscreen.get("1.0", "end-1c")
        bookfile.write(INPUT)
        bookfile.close()
        scrn.update()
    elif number == 3:
        bookfile = open("book3.txt", "w")
        INPUT = txtscreen.get("1.0", "end-1c")
        bookfile.write(INPUT)
        bookfile.close()
        scrn.update()


scrn = Tk()

scrn.title("Bookpad")
scrn.geometry("620x570")

txtscreen = Text(scrn, width= 77, height= 30)
txtscreen.place(x=0,y=0)

savebutton = Button(scrn, width= 21, height= 5,text= "Save", background= "Light Green", command =lambda:saveBook(selectedBook))
savebutton.place(x=0,y=485)

text1 = Button(scrn, width= 21, height= 5, text= "Book #1", background= "Light Blue", command =lambda:setBook(1))
text1.place(x=155, y=485)
text2 = Button(scrn, width= 21, height= 5, text= "Book #2", background= "Light Blue", command =lambda:setBook(2))
text2.place(x=310, y=485)
text3 = Button(scrn, width= 21, height= 5, text= "Book #3", background= "Light Blue", command =lambda:setBook(3))
text3.place(x=465, y=485)

scrn.mainloop()