import json

def backup_data():
    with open("sorted_data.json", "r") as file:
        data = json.load(file)
    with open(f"backups/data_backup.json", "w") as backup_file:
        json.dump(data, backup_file)
    print("✅ Backup saved.")

if __name__ == "__main__":
    backup_data()
