# Old Version
def d(a):
    for i in range(len(a)):
        for j in range(1+1, len(a)):
            if a[i] == a[j]:
                return True
    return False

# Refactored Version
def has_duplicates(items: list) -> bool:
    """Returns True if there are any duplicates in the list."""
    seen = set()
    for item in items:
        if item in seen:
            return True
        seen.add(item)
    return False

# Usage
if __name__ == "__main__":
    sample = [1,2,3,2]
    print("Old Version:", d(sample))
    print("Refactored Version:", has_duplicates(sample))