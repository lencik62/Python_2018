"""
Program that stores book information.
This was created as a prototype for my MC internship.


Funtionaily of the program:

    * CRUD actions:
        > Create new enteries.
        > Read a pre existing entiry by doing a search query.
        > Update a entry.
        > Delete an entey.
    * View all books
    * Close the program safely

"""


from tkinter import *

from backend import Database


def main():
    window = Tk()
    global title_text,author_text,year_text,isbn_text,database

    database=Database("books.db")
    title_text = StringVar()
    author_text = StringVar()
    year_text = StringVar()
    isbn_text = StringVar()

    create_labels_on_window(window)


    create_entries_on_window(window, title_text, author_text, year_text, isbn_text)

    create_and_bind_listview_with_scrollbar(window)


    create_buttons_on_window(window)

    window.mainloop()

def get_selected_row(event):
    global selected_tuple
    index = book_list.curselection()[0]
    selected_tuple = book_list.get(index)
    title_entry.delete(0, END)
    title_entry.insert(END, selected_tuple[0])
    author_entry.delete(0, END)
    author_entry.insert(END, selected_tuple[1])
    year_entry.delete(0, END)
    year_entry.insert(END, selected_tuple[2])
    isbn_entry.delete(0, END)
    isbn_entry.insert(END, selected_tuple[3])

def view_command():
    book_list.delete(0, END)
    for row in database.view():
        book_list.insert(END, row)

def search_command():
    book_list.delete(0, END)
    for row in database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        book_list.insert(END, row)

def add_command():
    database.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    book_list.delete(0, END)
    book_list.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def delete_command():
    database.delete(selected_tuple[0])
    view_command()

def update_command():
    database.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())


def create_buttons_on_window(window):
    view_all_btn = Button(window, text = "View All", width = 12, command = view_command )
    search_entry_btn = Button(window, text = "Search entry", width = 12, command = search_command)
    add_entry_btn = Button(window, text = "Add Entry", width = 12, command = add_command)
    update_btn = Button(window, text = "Update", width = 12, command = update_command)
    delete_btn = Button(window, text = "Delete", width = 12, command = delete_command)
    close_btn = Button(window, text = "Close", width = 12, command = window.destroy)

    view_all_btn.grid(row = 2, column = 3)
    search_entry_btn.grid(row = 3, column = 3)
    add_entry_btn.grid(row = 4, column = 3)
    update_btn.grid(row = 5, column = 3)
    delete_btn.grid(row = 6, column = 3)
    close_btn.grid(row = 7, column = 3)

def create_and_bind_listview_with_scrollbar(window):
    global book_list

    scroll_bar = Scrollbar(window)
    scroll_bar.grid(row = 2, column = 2, rowspan = 6)

    book_list = Listbox(window, height = 6, width = 35)
    book_list.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

    book_list.configure(yscrollcommand = scroll_bar.set)
    scroll_bar.configure(command = book_list.yview)

    book_list.bind('<<ListboxSelect>>', get_selected_row)

def create_entries_on_window(window, title_text, author_text, year_text, isbn_text):
    global title_entry,author_entry,year_entry,isbn_entry
    title_entry =  Entry(window, textvariable = title_text)
    author_entry =  Entry(window, textvariable = author_text)
    year_entry =  Entry(window, textvariable = year_text)
    isbn_entry =  Entry(window, textvariable = isbn_text)

    title_entry.grid(row = 0, column = 1)
    author_entry.grid(row = 0, column = 3)
    year_entry.grid(row = 1, column = 1)
    isbn_entry.grid(row = 1, column = 3)

def create_labels_on_window(window):
    title_lbl =  Label(window, text = "Title")
    author_lbl =  Label(window, text = "Author")
    year_lbl =  Label(window, text = "Year")
    isbn_lbl =  Label(window, text = "ISBN")

    title_lbl.grid(row = 0, column = 0)
    author_lbl.grid(row = 0, column = 2)
    year_lbl.grid(row = 1, column = 0)
    isbn_lbl.grid(row = 1, column = 2)


if __name__ == '__main__':
    main()