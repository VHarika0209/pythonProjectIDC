# Bookstore Inventory System

# Dictionary: key = book name, value = (copies, (author, year), [tags])
inventory = {}

# Set: to store unique tags across all books
all_tags = set()

# Function to add or update a book in the inventory
def add_book(book_name, copies, author, year, tags):
    tags = list(tags)  # ensure it's a list

    if book_name in inventory:
        # Unpack existing tuple
        old_copies, (old_author, old_year), old_tags = inventory[book_name]

        # Update copies and extend tag list
        new_copies = old_copies + copies
        updated_tags = old_tags + tags  # combine both lists

        # Replace the tuple in the dictionary with updated values
        inventory[book_name] = (new_copies, (old_author, old_year), updated_tags)
        print(f"Updated '{book_name}' with {copies} more copies and new tags.")
    else:
        inventory[book_name] = (copies, (author, year), tags)
        print(f"Added new book: '{book_name}'")

    # Update global tag set
    all_tags.update(tags)

# Function to issue a book
def issue_book(book_name, quantity):
    if book_name not in inventory:
        print(f"'{book_name}' is not available.")
        return

    current_copies, book_info, tags = inventory[book_name]
    if current_copies < quantity:
        print(f"Only {current_copies} copies available.")
    else:
        new_copies = current_copies - quantity
        inventory[book_name] = (new_copies, book_info, tags)
        print(f"Issued {quantity} copies of '{book_name}'")

# Function to view inventory
def display_inventory():
    print("\n Current Inventory:")
    for book, (copies, (author, year), tags) in inventory.items():
        print(f"- {book} ({copies} copies) by {author} ({year}) | Tags: {tags}")
    print()

# Function to show all unique tags
def display_all_tags():
    print(f"\n All Tags (Set): {all_tags}\n")

# Demo run
add_book("Python Basics", 5, "John Doe", 2020, ["Programming", "Beginner"])
add_book("Data Science 101", 3, "Jane Smith", 2021, ["Data", "AI", "ML"])
add_book("Python Basics", 2, "John Doe", 2020, ["Tech", "Coding"])
issue_book("Python Basics", 4)
display_inventory()
display_all_tags()

# Slicing example from list of tags
print("First 2 tags of 'Data Science 101':", inventory["Data Science 101"][2][:2])
