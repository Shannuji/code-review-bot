 🚀 Code Review Bot
 📌 Overview
This project fetches Python files from a GitHub repository, runs Pylint analysis, and suggests improvements using OpenAI.
 🔹 Features
1) Fetches Python files from GitHub.
2) Analyzes code quality using Pylint.
3) Suggests improvements using OpenAI GPT.
 🔹 Installation & Setup
 1️⃣ Clone the Repository

git clone https://github.com/Shannuji/code-review-bot.git
cd code-review-bot


 2️⃣ Install Dependencies

pip install -r requirements.txt


 3️⃣ Set API Keys

$env:OPENAI_API_KEY="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"
$env:GITHUB_TOKEN="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"


 4️⃣ Run the Script

python main.py
![Screenshot 2025-03-04 203738](https://github.com/user-attachments/assets/ac79e50a-9d01-41b9-b83a-324edbd09258)
Fetching repo contents from: https://api.github.com/repos/Shannuji/code-review-bot/contents/
Processing file: main.py
✅ Pylint Score: 8/10
💡 Suggestions:
- Use better variable names
- Improve error handling


 📝 Contributors
- SHANMATHI VENKTESAN .





