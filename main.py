import os
import requests
import openai
from pylint.lint import Run

# Load OpenAI API Key Securely
openai.api_key = os.getenv("OPENAI_API_KEY")  # Set this in your environment variables

def analyze_code(file_path):
    """ Runs Pylint on the given Python file & returns analysis report """
    results = Run([file_path], do_exit=False)
    score = results.linter.stats.get('global_note', 0)  # Avoid KeyError
    return score

def suggest_improvements(code_snippet):
    """ Uses OpenAI GPT to generate improvements for the given code snippet """
    prompt = f"Analyze this Python code and suggest improvements:\n\n{code_snippet}"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"OpenAI API Error: {str(e)}"

def scan_repository(repo_url):
    """ Fetches Python files from GitHub repo (including subdirectories) & analyzes them """
    print(f"Fetching repo contents from: {repo_url}")  

    response = requests.get(repo_url)
    
    if response.status_code != 200:
        print(f"Failed to fetch repository contents: {response.status_code}")
        return

    files = response.json()

    for file in files:
        print(f"Processing file: {file['name']}")  

        # If it's a folder, fetch its contents recursively
        if file['type'] == 'dir':
            scan_repository(file['url'])  # Recursive call for subdirectories

        elif file['name'].endswith('.py'):
            raw_url = file['download_url']
            print(f"Fetching file from: {raw_url}")  

            code = requests.get(raw_url).text

            # Save the file locally for analysis
            local_file_path = f"temp_{file['name']}"
            with open(local_file_path, 'w', encoding='utf-8') as f:
                f.write(code)

            score = analyze_code(local_file_path)
            suggestions = suggest_improvements(code)

            print(f"\n📂 **File:** {file['name']}")
            print(f"✅ **Pylint Score:** {score}/10")
            print(f"💡 **Suggestions:**\n{suggestions}\n")

            # Clean up temp file
            os.remove(local_file_path)

    print("Script finished.")


# Example: Call the function with your GitHub repo URL
scan_repository("https://api.github.com/repos/Shannuji/code-review-bot/contents/")
