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


Attributes of Book object:
    Attribute:Title
                - Title of the book
    Attribute: Author
                - Author of the book
    Attribute:Year
                - Year of the was published
    Attribute: ISBN
                - ISBN of the book

    Type:Title: String
    Type: Author: String
    Type:Year: int
    Type: ISBN: int
"""


from tkinter import *

window = Tk()

title_text = StringVar()
author_text = StringVar()
year_text = StringVar()
isbn_text = StringVar()


title_lbl =  Label(window, text = "Title")
author_lbl =  Label(window, text = "Author")
year_lbl =  Label(window, text = "Year")
isbn_lbl =  Label(window, text = "ISBN")

title_lbl.grid(row = 0, column = 0)
author_lbl.grid(row = 0, column = 2)
year_lbl.grid(row = 1, column = 0)
isbn_lbl.grid(row = 1, column = 2)


title_entry =  Entry(window, textvariable = title_text)
author_entry =  Entry(window, textvariable = author_text)
year_entry =  Entry(window, textvariable = year_text)
isbn_entry =  Entry(window, textvariable = isbn_text)

title_entry.grid(row = 0, column = 1)
author_entry.grid(row = 0, column = 3)
year_entry.grid(row = 1, column = 1)
isbn_entry.grid(row = 1, column = 3)

scroll_bar = Scrollbar(window)
scroll_bar.grid(row = 2, column = 2, rowspan = 6)

book_list = Listbox(window, height = 6, width = 35)
book_list.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

book_list.configure(yscrollcommand = scroll_bar.set)
scroll_bar.configure(command = book_list.yview)


view_all_btn = Button(window, text = "View All", width = 12)
search_entry_btn = Button(window, text = "Search entry", width = 12)
add_entry_btn = Button(window, text = "Add Entry", width = 12)
update_btn = Button(window, text = "Update", width = 12)
delete_btn = Button(window, text = "Delete", width = 12)
close_btn = Button(window, text = "Close", width = 12)

view_all_btn.grid(row = 2, column = 3)
search_entry_btn.grid(row = 3, column = 3)
add_entry_btn.grid(row = 4, column = 3)
update_btn.grid(row = 5, column = 3)
delete_btn.grid(row = 6, column = 3)
close_btn.grid(row = 7, column = 3)

window.mainloop()