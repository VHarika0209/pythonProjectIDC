from dataclasses import dataclass

@dataclass()
class LibraryBook:
    title: str
    author: str
    publication_year: int
    isbn: str

    def display_details(self) -> None:
        print(f"📚 Title: {self.title}")
        print(f"✍️ Author: {self.author}")
        print(f"🔢 ISBN: {self.isbn}")
        print(f"🗓️ Publication Year: {self.publication_year}")

book = LibraryBook(
    title="The White Tiger",
    author="Aravind Adiga",
    isbn="978-1-4165-8733-1",
    publication_year=2008
)

book.display_details()