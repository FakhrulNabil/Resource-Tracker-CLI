🛠️ Resource Tracker CLI
A lightweight, object-oriented Python command-line interface (CLI) designed to manage developer assets, API keys, and server metadata. This project demonstrates core software engineering principles: CRUD operations, Data Persistence, and Defensive Programming.

🌟 Features
Data Persistence: Uses JSON for local storage, ensuring data remains after the app closes.

Duplicate Prevention: Logic to prevent accidental creation of identical resource names.

Search Engine: Case-insensitive search to find resources by keyword.

Input Validation: Robust error handling for invalid IDs and file corruption.

Clean Architecture: Separates User Interface (main.py) from Business Logic (manager.py).

🚀 Tech Stack
Language: Python 3.x

Data Format: JSON

Core Modules: os, json, typing

📂 Project Structure
Plaintext
resource-tracker/
├── data/               # Local data storage (ignored by git)
├── src/
│   ├── manager.py      # ResourceTracker class & logic
│   └── main.py         # CLI Menu & User interaction
├── .gitignore          # Prevents tracking personal JSON data
└── README.md           # Project documentation
🛠️ Installation & Usage
Clone the repository:

Bash
git clone https://github.com/yourusername/resource-tracker.git
cd resource-tracker
Run the application:

Bash
python src/main.py