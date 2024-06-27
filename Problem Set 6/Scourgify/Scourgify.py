import sys
import csv

def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        sys.exit("Usage: python Scourgify.py input.csv output.csv")
    
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    
    # Try to open the input file
    try:
        with open(input_filename, mode='r') as infile:
            reader = csv.DictReader(infile)
            # Define the output fieldnames
            fieldnames = ["first", "last", "house"]
            
            # Open the output file
            with open(output_filename, mode='w', newline='') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()
                
                # Process each row from the input file
                for row in reader:
                    # Split the name into first and last
                    last, first = row["name"].split(", ")
                    # Write the new row to the output file
                    writer.writerow({"first": first, "last": last, "house": row["house"]})
    except FileNotFoundError:
        sys.exit(f"Error: The file '{input_filename}' does not exist.")
    except Exception as e:
        sys.exit(f"Error: {e}")

if __name__ == "__main__":
    main()