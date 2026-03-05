from manager import ResourceTracker

def main():
    tracker = ResourceTracker()
    
    while True:
        print("\n--- 🛠️  Resource Manager Menu ---")
        print("1. Add a Resource")
        print("2. List All Resources")
        print("3. Search Resources")
        print("4. Exit")
        
        choice = input("\nChoose an option (1-4): ")

        if choice == '1':
            name = input("Enter Resource Name: ")
            category = input("Enter Category (Cloud/API/Database): ")
            tracker.add_resource(name, category)

        elif choice == '2':
            tracker.list_resources()

        elif choice == '3':
            query = input("Enter search term: ")
            tracker.search_resource(query)

        elif choice == '4':
            tracker.list_resources() # Show the list first so they see the IDs
            try:
                idx = int(input("Enter the # ID to delete: "))
                tracker.delete_resource(idx)
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == '5':
            print("👋 Goodbye!")
            break

        else:
            print("⚠️ Invalid choice, please try again.")

if __name__ == "__main__":
    main()