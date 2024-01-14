# GitHub Repository Analysis Script

🚀 Welcome to the GitHub Repository Analysis Script! 🚀

This script interacts with the GitHub API and OpenAI's GPT model to generate an analysis report for a given repository. It fetches source code files, creates prompts, and generates insights on various aspects of the codebase.

## Prerequisites

Before running the script, make sure you have the following:

- Python installed
- GitHub API token (set as GITHUB_API_KEY in your .env file) 
  [Click here to Generate Token](https://github.com/settings/tokens)
- OpenAI API key (set as OPENAI_API_KEY in your .env file) 
  [Click here to Generate Token](https://platform.openai.com/api-keys)

.env
```
GITHUB_API_KEY="<YOUR API KEY HERE>"
OPENAI_API_KEY="<YOUR API KEY HERE>"
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/amans584/Code_Analysis.git
cd your-repo
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the script:

```bash
python main.py
```

Follow the prompts to enter the repository name.

4. Enjoy the generated analysis report!

## Analysis Report

The script generates a detailed analysis report covering various aspects of the repository:

- Brief repository overview
- Code quality and usage of standard practices
- Suggestions for code quality improvement
- Recommendations for efficiency and time complexity
- Additional test cases for better coverage
- Bug identification with solutions and preventive measures
- Documentation and report suggestions

## Results

The analysis results can be saved in a Markdown file with a custom name.

## Author

- Aman Singh
- GitHub: [Aman Singh](https://github.com/amans584)