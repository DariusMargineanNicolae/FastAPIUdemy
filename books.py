from fastapi import FastAPI
from enum import Enum
from typing import Optional

app = FastAPI()

BOOKS = {
        "book_1":{"title": "Title One", "author":"Author One"},
        "book_2":{"title": "Title Two", "author":"Author Twon"},
        "book_3":{"title": "Title Three", "author":"Author Three"},
        "book_4":{"title": "Title Four", "author":"Author Four"},
        "book_5":{"title": "Title Five", "author":"Author Five"},
        
} 

class DirecationName (str, Enum):
    north = 'North'
    south = 'South'
    east = 'East'
    west = 'West'

@app.get("/")
async def read_all_books(skip_book: Optional[str] = None): #Done using Query params
    if skip_book:
        new_books = BOOKS.copy()
        del new_books[skip_book]
        return new_books
    else:
        return BOOKS

@app.get("/books/{book_title}")
async def read_book(book_title):
    return {"book_title": book_title}


    
@app.get("/directions/{direction_name}")
async def get_direction(direction_name: DirecationName):
    if direction_name == DirecationName.north:
        return {"Direction": direction_name, 'subject':'UP'}
    elif direction_name == DirecationName.south:
        return {"Direction": direction_name, 'subject':'DOWN'}
    elif direction_name == DirecationName.west:
        return {"Direction": direction_name, 'subject':'LEFT'}
    else: 
        return {"Direction": direction_name, 'subject':'RIGHT'}
    
@app.get("/{book_name}")
async def read_book(book_name: str):
    return BOOKS[book_name]


@app.post("/")
async def create_book(book_title, book_author):
    curr_book_id = 0
    if len(BOOKS) > 0:
        for book in BOOKS:
            x = int(book.split('_')[-1])
            if x > curr_book_id:
                curr_book_id = x
    BOOKS[f'book_{curr_book_id+1}'] = {'title':book_title, 'author':book_author}
    return BOOKS[f'book_{curr_book_id+1}']        


@app.put("/{book_name}")
async def update_book(book_name: str, book_title: str, book_author: str):
    book_info = {'title':book_title, 'author':book_author}
    BOOKS[book_name] = book_info
    return book_info


@app.delete("/{book_name}")
async def delete_book(book_name:str):
    del BOOKS[book_name]
    return f'Book_{book_name} deleted'

#ASSIGNMENT

@app.get("/assignment_read_books/")
async def read_book_assignment(book_name: str):
    return BOOKS[book_name]

@app.delete("/assignment_delete/")
async def delete_book_assignment(book_name: str):
    del BOOKS[book_name]
    return f'Book_{book_name} deleted'