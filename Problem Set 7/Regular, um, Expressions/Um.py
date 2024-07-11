import re

def main():
    print(count(input("Text: ")))

def count(s):
    # Using regular expression to find standalone 'um' case-insensitively
    pattern = r'\bum\b'
    matches = re.findall(pattern, s, re.IGNORECASE)
    return len(matches)

if __name__ == "__main__":
    main()