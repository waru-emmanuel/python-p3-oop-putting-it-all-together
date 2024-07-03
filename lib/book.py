#!/usr/bin/env python3

class Book:

    def __init__(self, title, page_count):
        '''has the title and page_count passed into __init__, and values can be set to new instance.'''
        self.title = title
        self.page_count = page_count
        

    #property and setter
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if type(new_title) is str:
            self._title = new_title
        else:
            print("title must be a string")
    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, new_page_count):
        if type(new_page_count) is int:
            self._page_count = new_page_count
        else:
            print("page_count must be an integer")

    def turn_page(self):
        '''outputs "Flipping the page...wow, you read fast!" when method turn_page() is called'''
        print("Flipping the page...wow, you read fast!")


    
    
        