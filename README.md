import json

def count_items_from_json_file(file_path, item_label):
    """
    Reads a JSON file, counts the occurrences of a specific item label
    within the 'shapes' array, and returns the total.

    This function is designed to work with annotation files where
    the objects to be counted are listed in a 'shapes' key.

    Args:
        file_path (str): The path to the JSON file.
        item_label (str): The label of the item to count (e.g., 'chicken').

    Returns:
        int: The total count of the specified item, or 0 if an error occurs.
    """
    count = 0
    try:
        # Open and load the JSON file
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Check for the 'shapes' key in the loaded data
        if 'shapes' in data and isinstance(data['shapes'], list):
            # Iterate through each shape object in the list
            for shape in data['shapes']:
                # Check if the shape is a dictionary and has a 'label' key
                if isinstance(shape, dict) and shape.get('label') == item_label:
                    count += 1
            return count
        else:
            print("Error: The JSON file does not contain a valid 'shapes' array.")
            return 0
            
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return 0
    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}' is not a valid JSON file.")
        return 0

# --- Main execution block ---
if __name__ == "__main__":
    # The path to the JSON file you provided
    json_file = "496.json"
    
    # The label we are looking for
    item_to_count = "chicken"
    
    # Get the count
    chicken_count = count_items_from_json_file(json_file, item_to_count)
    
    if chicken_count > 0:
        print(f"Found {chicken_count} '{item_to_count}' items in the JSON file.")
    else:
        print(f"No '{item_to_count}' items were found or an error occurred.")

