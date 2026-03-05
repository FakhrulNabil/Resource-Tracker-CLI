import json
import os

class ResourceTracker:
    def __init__(self, storage_file="resources.json"):
        self.storage_file = storage_file
        self.resources = self._load_data()

    def _load_data(self):
        if not os.path.exists(self.storage_file):
            return []
        try:
            with open(self.storage_file, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def _save_data(self):
        with open(self.storage_file, 'w') as f:
            json.dump(self.resources, f, indent=4)

    def delete_resource(self, index: int):
        """Removes a resource by its list index."""
        try:
            # Adjust for 0-based indexing (User enters 1, we use 0)
            removed_item = self.resources.pop(index - 1)
            self._save_data()
            print(f"🗑️  Successfully deleted: {removed_item['name']}")
        except (IndexError, ValueError):
            print("❌ Error: Invalid ID. Please check the list and try again.")

    # --- NEW: Check for Duplicates ---
    def add_resource(self, name: str, category: str):
        # Check if name already exists (Case-insensitive)
        if any(item['name'].lower() == name.lower() for item in self.resources):
            print(f"❌ Error: A resource named '{name}' already exists!")
            return 

        new_item = {"name": name, "category": category}
        self.resources.append(new_item)
        self._save_data()
        print(f"✅ Added {name} to {category}!")

    # --- NEW: Search Feature ---
    def search_resource(self, query: str):
        print(f"\n🔍 Searching for: '{query}'...")
        results = [item for item in self.resources if query.lower() in item['name'].lower()]
        
        if not results:
            print("No matches found.")
        else:
            for idx, item in enumerate(results, 1):
                print(f"Found: {item['name']} ({item['category']})")

    def list_resources(self):
        if not self.resources:
            print("📭 No resources found.")
            return
        print("\n--- Current Resources ---")
        for idx, item in enumerate(self.resources, 1):
            print(f"{idx}. {item['name']} [{item['category']}]")

# --- Interactive Test Loop ---
if __name__ == "__main__":
    tracker = ResourceTracker()
    
    # Try adding a duplicate to see the error handling in action
    tracker.add_resource("AWS_PROD_KEY", "Cloud")
    tracker.add_resource("AWS_PROD_KEY", "Cloud") # This should fail!
    
    # Try searching
    tracker.search_resource("AWS")
    tracker.list_resources()