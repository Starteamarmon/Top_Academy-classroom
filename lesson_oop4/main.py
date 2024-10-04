from __future__ import annotations

class Item:
    def __init__(self, value: int,nxt: Item | None = None):
        self._value:int = value
        self._nxt: Item = nxt



class LinkedList:
    def __init__(self, item: Item):
        self._item: Item = item
        
b = Item(2,None)
a = Item(1, b)