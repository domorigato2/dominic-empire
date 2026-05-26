import os

def analyze_log_file(file_name):
    if not os.path.exists(file_name):
        print(f"Error: The file '{file_name}' was not found.")
        return

    print("========================================")
    print(f"🔍 ANALYZING FILE: {file_name}")
    print("========================================")

    # Dictionary mapping clean categories to lists of possible variations and typos
    categories = {
        "coffee": ["coffee", "cofffee", "coffe"],
        "standing": ["standing", "standinf", "stansing", "dtanding", "atansing"],
        "computer": ["computer", "compiter", "pc", "terminal"],
        "silence": ["silence", "silende", "sielnce"],
        "mow": ["mow", "mowing", "grass"]
    }

    # Initialize counters for each category
    counts = {category: 0 for category in categories}
    total_lines = 0

    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            total_lines += 1
            lowercase_line = line.lower()
            
            # Check each category's list of variations
            for category, variations in categories.items():
                for var in variations:
                    if var in lowercase_line:
                        counts[category] += 1
                        break # Stop checking variations for this category on this line

    # Print the updated results
    print(f"Total lines processed: {total_lines}")
    print("----------------------------------------")
    print("Keyword Occurrences (with typo correction):")
    for category, count in counts.items():
        print(f"  - '{category}': {count} times")
    print("========================================")

if __name__ == "__main__":
    target_file = "sample_data.txt"
    analyze_log_file(target_file)