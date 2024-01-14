from github import Github, Auth
from openai import OpenAI

import os
from colorama import Fore as F, Style as S
from dotenv import load_dotenv

load_dotenv()

GITHUB_AUTH_TOKEN = os.getenv("GITHUB_API_KEY")

g = Github(auth=Auth.Token(GITHUB_AUTH_TOKEN))


repo = g.get_repo(input("Enter repo name (fmt. {owner}/{repo}) : "))
 
BOLD = '\033[1m'
print(F"\n{F.YELLOW+BOLD} ⬤  Fetching Sources ...{F.RESET+S.NORMAL}\n")

contents = repo.get_contents("")
files = {}

while contents:
    file_content = contents.pop(0)
    if file_content.type == "dir":
        contents.extend(repo.get_contents(file_content.path))
    elif '.' not in file_content.path.split('/')[-1]: continue
    elif file_content.path.split('/')[-1].split('.')[-1] in (
        'exe', 'bin', 'com', 'mp3', 'mp4', 'spec'
    ): continue
    else:
        print("  "+file_content.path)
        try: files[file_content.path] = file_content.decoded_content.decode()
        except: file_content.decoded_content.decode(errors='ignore') 

def create_prompts(files: dict):
    tasks = [
        "Give a brief about the repository",
        "Tell me about code quality and uses of standard practices in this repository.",
        "Give me detailed suggestions on how to improve the code quality.",
        "Give me detailed information for improving areas for efficiency and reducing time complexity",
        "Suggest additional testcases for better coverage",
        "Pinpoint bugs with possible solutions and preventive measures",
        "Give me suggestions for documentation and reports for this project"
    ]

    prompt = """
Below are all the files in the repository, with the associated code.

- the file path is presented as '> PATH : {path}'
- the file content is presented as: '> CONTENT : <newline>{content}'
- after each file, there is a space of 5 newlines

====================================================================================================

\n\n\n\n\n """

    for key, value in files.items(): prompt += f"> PATH : {key}\n> CONTENT : \n{value}\n\n\n\n\n"

    prompt += """

====================================================================================================

YOUR TASK is to:  
- """
    prompts = list(map(lambda task: prompt + task+"""
- Give your result with a proper 2-5 word title in uppercase and MARKDOWN FORMAT
- Use emojis to make the result user-friendly if necessary                       

NOW GO !!""", tasks))
    return prompts


prompts = create_prompts(files)

client = OpenAI()

MAX_TRIES = 1

def get_result(prompt, model='gpt-3.5-turbo', tries = 0):
    if tries >= MAX_TRIES: return 'Error Multiple times while trying to fetch response from GPT API'
    try:
        completion = client.chat.completions.create(
            model = model,
            messages = [
                {
                    "role":"user",
                    "content":prompt
                }
            ]
        )
        return completion.choices[0].message.content
    except: return get_result(prompt, model, tries+1)

print(f"\n {F.GREEN+BOLD}⬤  Generating Analysis Report ...{F.RESET+S.NORMAL}")
results = []
for prompt in prompts:
    result = get_result(prompt)
    results.append(result)

print("\n\n\n"+"="*140+"\n"+f"{F.RED+BOLD}  ANALYSIS REPORT  {S.NORMAL+F.RESET}".center(140,'-')+"\n"+"="*140+"\n\n\n")
for result in results: print(result)

saveChoice = input(f"\n\n\n{F.CYAN+BOLD}Would you like to save this in a file [y/N] ? {F.RESET+S.NORMAL}")
if saveChoice.lower() in 'yes':
    name = input("Enter name for report : ")

    with open(f"{name}.md","w+") as f:
        for result in results: f.write(result)
    
    print("File Saved !!")