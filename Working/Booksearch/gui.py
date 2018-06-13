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

class Window(object):

    def __init__(self):
        """
            Create a window that displays the book database and its funtion visually though a GUI.
            :param self:
        """
        window = Tk()
        global title_text, author_text, year_text, isbn_text, database

        database = Database("books.db")
        title_text = StringVar()
        author_text = StringVar()
        year_text = StringVar()
        isbn_text = StringVar()

        self._create_labels_on_window(window)
        self._create_entries_on_window(window, title_text, author_text, year_text, isbn_text)
        self._create_and_bind_listview_with_scrollbar(window)
        self._create_buttons_on_window(window)

        window.mainloop()

    def get_selected_row(self, event):
        """
        Display the selected row's information on the text fields / entry fields.
            :param self:
            :param event: click event
        """
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

    def view_command(self):
        """
        List all the books from the DB on the list box
            :param self:
        """
        book_list.delete(0, END)
        for row in database.view():
            book_list.insert(END, row)

    def search_command(self):
        """
        Conducts a search based on the information of the extry fields that and list the result in the listbox.
            :param self:
        """   book_list.delete(0, END)
        for row in database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
            book_list.insert(END, row)

    def add_command(self):
        """
        Adds the book entry on the data base with the information provided.
            :param self:
        """
        database.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
        book_list.delete(0, END)
        book_list.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

    def delete_command(self):
        """
        Deletes the selected book on the list view from the data base.
            :param self:
        """
        database.delete(selected_tuple[0])
        self.view_command()

    def update_command(self):
        """
        Updates the information of the seleted book, based on the information provied.
            :param self:
        """
        database.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())


    def _create_buttons_on_window(self, window):
        """
        Places main CRUD and exit button on the window.
            :param self:
            :param window: the main window.
        """
        view_all_btn = Button(window, text = "View All", width = 12, command = self.view_command )
        search_entry_btn = Button(window, text = "Search entry", width = 12, command = self.search_command)
        add_entry_btn = Button(window, text = "Add Entry", width = 12, command = self.add_command)
        update_btn = Button(window, text = "Update", width = 12, command = self.update_command)
        delete_btn = Button(window, text = "Delete", width = 12, command = self.delete_command)
        close_btn = Button(window, text = "Close", width = 12, command = window.destroy)

        view_all_btn.grid(row = 2, column = 3)
        search_entry_btn.grid(row = 3, column = 3)
        add_entry_btn.grid(row = 4, column = 3)
        update_btn.grid(row = 5, column = 3)
        delete_btn.grid(row = 6, column = 3)
        close_btn.grid(row = 7, column = 3)

    def _create_and_bind_listview_with_scrollbar(self, window):
        """
        Places listbox/listview and the scrollbar on the window.
        Also bind the scrollbar with the listview to enable vertical scrolling on listview.
            :param self:
            :param window: the main window.
        """
        global book_list

        scroll_bar = Scrollbar(window)
        scroll_bar.grid(row = 2, column = 2, rowspan = 6)

        book_list = Listbox(window, height = 6, width = 35)
        book_list.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

        book_list.configure(yscrollcommand = scroll_bar.set)
        scroll_bar.configure(command = book_list.yview)

        book_list.bind('<<ListboxSelect>>', self.get_selected_row)

    def _create_entries_on_window(self, window, title_text, author_text, year_text, isbn_text):
        """
        Places text/entry fields on the window.
            :param self:
            :param window: the main window.
        """
        global title_entry, author_entry, year_entry, isbn_entry
        title_entry =  Entry(window, textvariable = title_text)
        author_entry =  Entry(window, textvariable = author_text)
        year_entry =  Entry(window, textvariable = year_text)
        isbn_entry =  Entry(window, textvariable = isbn_text)

        title_entry.grid(row = 0, column = 1)
        author_entry.grid(row = 0, column = 3)
        year_entry.grid(row = 1, column = 1)
        isbn_entry.grid(row = 1, column = 3)

    def _create_labels_on_window(self, window):
        """
        Places text/entry fields' labels on the window.
            :param self:
            :param window: the main window.
        """
        title_lbl =  Label(window, text = "Title")
        author_lbl =  Label(window, text = "Author")
        year_lbl =  Label(window, text = "Year")
        isbn_lbl =  Label(window, text = "ISBN")

        title_lbl.grid(row = 0, column = 0)
        author_lbl.grid(row = 0, column = 2)
        year_lbl.grid(row = 1, column = 0)
        isbn_lbl.grid(row = 1, column = 2)


def main():
    Window()

if __name__ == '__main__':
    main()