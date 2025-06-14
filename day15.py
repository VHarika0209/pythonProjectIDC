import time
def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} took {(end - start)*1000:.4f} milli seconds.")
        return result
    return wrapper

raw_products = [
    " Samsung Galaxy S21  ",
    "apple iPhone 13",
    " APPLE IPHONE 13  ",
    "  OnePlus Nord CE",
    "samsung galaxy s21",
    "Nokia 3310\n",
    "oneplus NORD ce",
    " Realme Narzo",
    "",
    "   "
]

def cleaning_data(raw_products):
    cleaned_raw_products = []
    seen = set()
    for product in raw_products:
        cleaned = product.strip()
        cleaned = cleaned.lower()
        cleaned = cleaned.replace("  ","")
        cleaned = cleaned.replace("\n","")

        if not cleaned:
            continue

        if cleaned not in seen:
            cleaned_raw_products.append(cleaned)
            seen.add(cleaned)

    return cleaned_raw_products

@time_it
def print_cleaned_products(cleaned_raw_products):
    print("Cleaned Products:")
    print(cleaned_raw_products)

cleaned_data = cleaning_data(raw_products)
print_cleaned_products(cleaned_data)









