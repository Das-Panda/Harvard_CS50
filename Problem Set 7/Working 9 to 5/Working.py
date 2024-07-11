import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Regular expression to match the allowed time formats
    match = re.match(r"^(\d{1,2}(:\d{2})?) (AM|PM) to (\d{1,2}(:\d{2})?) (AM|PM)$", s)
    if not match:
        raise ValueError("Invalid format")

    # Extract parts from the match
    start_time, _, start_period, end_time, _, end_period = match.groups()

    def to_24_hour_format(time, period):
        # Split time into hours and optional minutes
        if ':' in time:
            hours, minutes = map(int, time.split(':'))
        else:
            hours = int(time)
            minutes = 0
        
        # Convert to 24-hour format
        if period == "AM":
            if hours == 12:
                hours = 0
        elif period == "PM":
            if hours != 12:
                hours += 12
        
        return f"{hours:02}:{minutes:02}"

    start_24 = to_24_hour_format(start_time, start_period)
    end_24 = to_24_hour_format(end_time, end_period)

    return f"{start_24} to {end_24}"

if __name__ == "__main__":
    main()