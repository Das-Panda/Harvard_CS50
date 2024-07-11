import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # Regular expression to match the src attribute of the iframe with YouTube URLs
    match = re.search(r'src="(https?://(?:www\.)?youtube\.com/embed/([^"]+))"', s)
    if match:
        video_id = match.group(2)
        return f"https://youtu.be/{video_id}"
    return None

if __name__ == "__main__":
    main()