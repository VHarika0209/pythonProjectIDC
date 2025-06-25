from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4, UUID
app = FastAPI(title="📚 Library API", description="Manage a library of books", version="1.0.0")
# 🧱 Data Models
class Book(BaseModel):
    id: UUID
    title: str
    author: str
    year: int
    description: Optional[str] = None

class BookCreate(BaseModel):
    title: str
    author: str
    year: int
    description: Optional[str] = None
# 📚 In-memory "database"
library: List[Book] = []
# 🚀 Endpoints
@app.get("/books", response_model=List[Book])
def get_books():
    return library
@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: UUID):
    for book in library:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")
@app.post("/books", response_model=Book, status_code=201)
def create_book(book_data: BookCreate):
    new_book = Book(id=uuid4(), **book_data.dict())
    library.append(new_book)
    return new_book
@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: UUID, book_data: BookCreate):
    for index, book in enumerate(library):
        if book.id == book_id:
            updated_book = Book(id=book_id, **book_data.dict())
            library[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")
@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: UUID):
    for index, book in enumerate(library):
        if book.id == book_id:
            del library[index]
            return
    raise HTTPException(status_code=404, detail="Book not found")
