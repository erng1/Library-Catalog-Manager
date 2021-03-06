# ACIT 2515 - Assignment 4
# multimedia.py
# Group 19

"""
This python file contains a Multimedia class
"""

from abstract_catalog import AbstractCatalog
import datetime


class Multimedia(AbstractCatalog):

    def get_details(self) -> str:
        """ Return a description of the media """
        output = f"{self.title} by {self.author} (ISBN: {self.isbn}) " \
                 f"is a {self.length} long {self.sub_type}. \n" \
                 f"Published on {datetime.datetime.strftime(self.pub_date, '%Y-%m-%d')} by {self.publisher}\n"
        if self.get_borrow_date():
            output += f"[Borrowed on {self.get_borrow_date()}] " \
                      f"[Due on {datetime.datetime.strftime(self.get_due_date(), '%Y-%m-%d')}] \n"
            if datetime.datetime.today().date() > self.get_due_date().date():
                output += f"Overdue by {(datetime.datetime.today() - self.get_due_date()).days} days. \n" \
                          f"${self.get_fee():.02f} fee receivables.\n"
        return output

    def save_item(self):
        """ Convert the length attribute before saving """
        if type(self.length) != str:
            self.length = datetime.time.strftime(self.length, "%H:%M:%S")
        self.save(force_insert=True)

    def to_dict(self) -> dict:
        """ Return a dictionary representation of a book object """
        return {
            "isbn": self.isbn,
            "author": self.author,
            "publisher": self.publisher,
            "title": self.title,
            "genre": self.genre,
            "pub_date": datetime.datetime.strftime(self.pub_date, "%Y-%m-%d"),
            "is_borrowed": bool(self.is_borrowed),
            "borrow_date": datetime.datetime.strftime(self.borrow_date, "%Y-%m-%d") if self.is_borrowed else None,
            "length": self.length,
            "sub_type": self.sub_type,
            "type_": self.type_
        }
