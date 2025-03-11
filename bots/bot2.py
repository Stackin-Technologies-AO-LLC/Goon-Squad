import json

def filter_data(data):
    filtered = [item for item in data if "important_key" in item]
    print(f"✅ Sorted {len(filtered)} important items.")
    return filtered

if __name__ == "__main__":
    with open("raw_data.json", "r") as file:
        raw_data = json.load(file)
    sorted_data = filter_data(raw_data)
    with open("sorted_data.json", "w") as file:
        json.dump(sorted_data, file)
