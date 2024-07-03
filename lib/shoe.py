#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        '''has the brand and size passed to __init__, and values can be set to new instance.'''
        self.brand = brand
        self.size = size
        
    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, new_brand):
        if type(new_brand) is str:
            self._brand = new_brand
        else:
            print("brand must be a string")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_size):
        if type(new_size) is int:
            self._size = new_size
        else:
            print("size must be an integer")

    def cobble(self):
        '''says that the shoe has been repaired.'''
        print("Your shoe is as good as new!")
        self.condition = "New"
        return self.condition
    
   

    