from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import uuid

# Database setup
DATABASE_URL = "sqlite:///./books.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False)
Base = declarative_base()

# SQLAlchemy Book model
class BookModel(Base):
    __tablename__ = "books"

    id = Column(String, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    description = Column(String, nullable=True)

# Create tables
Base.metadata.create_all(bind=engine)

# Pydantic Schemas
class BookBase(BaseModel):
    title: str
    author: str
    year: int
    description: Optional[str] = None

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: str

    class Config:
        orm_mode = True

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# FastAPI app
app = FastAPI(title="📚 Library API with SQLAlchemy", version="1.0.0")

# Endpoints

@app.post("/books", response_model=Book, status_code=201)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    book_id = str(uuid.uuid4())
    db_book = BookModel(id=book_id, **book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.get("/books", response_model=List[Book])
def get_books(db: Session = Depends(get_db)):
    return db.query(BookModel).all()

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: str, db: Session = Depends(get_db)):
    book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: str, updated: BookCreate, db: Session = Depends(get_db)):
    book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    for key, value in updated.dict().items():
        setattr(book, key, value)
    db.commit()
    db.refresh(book)
    return book

@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: str, db: Session = Depends(get_db)):
    book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
