import json

# Load the JSON data
with open('data/data.json', 'r') as file:
    data = json.load(file)

# Sort the recipes based on the category
sorted_data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1]['category'])}

# Save the sorted data back to a JSON file
with open('data/sorted_data.json', 'w') as file:
    json.dump(sorted_data, file, indent=4)

print("Recipes sorted by category and saved to sorted_data.json")