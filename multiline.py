import json

# Open the input text file and read the jokes
with open('data/jokes.txt', 'r', encoding='utf-8') as f:
    jokes = f.readlines()

filename = input("What should be the filename? ")

# Process each joke and convert it to a dictionary in JSON format
jokes_dict = {"jokes": []}
for i, joke in enumerate(jokes):
    joke = joke.strip()  # Remove any leading or trailing whitespace
    if '...' in joke:
        parts = joke.split("...", maxsplit=1)  # Split the joke into two parts, before and after the ellipses
    else:
        parts = joke.split("?", maxsplit=1)  # Split the joke into two parts, before and after the question mark
    if len(parts) != 2:
        continue  # Skip this joke if it doesn't have exactly one set of ellipses or question mark
    jokes_dict["jokes"].append({
        "id": str(i + 1),
        "setup": parts[0].strip(),
        "punchline": parts[1].strip()
    })

# Write the jokes to a JSON file
with open(f'{filename}.json', 'w', encoding='utf-8') as f:
    json.dump(jokes_dict, f, indent=2, ensure_ascii=False)
