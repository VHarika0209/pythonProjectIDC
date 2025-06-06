from pathlib import Path

file_path = Path("day10InputFile.txt")
print(f"Reading from file")
try:
    with file_path.open('r', encoding='utf-8') as file:
        content = file.readlines()
        print(f"Raw Content: {content}")
        for line in content:
            line = line.strip()
            try:
                num = int(line)
                print(f"Valid Number: {num}")
            except ValueError:
                print(f"Invalid number found: '{line}' -- Skipping.")
except FileNotFoundError:
    print(f"File Not Found: {file_path}")
except Exception as e:
    print(f"An unexpected error occurred : {e}")
finally:
    print("Execution Completed.")
