import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

PROMPT = """
You will receive a file's contents as text.
Generate a code review for file. Indicate what changes should be made to improve its style, performance, readability and maintainability. If there are any reputable libraties that could be introduces to improve the code, suggest them. Be kind and constructive. For each suggested change, include line numbers to which you are referring.
"""


filecontent = """
def myster(x, y):
    return x ** y
"""

messages = [
    {"role": "system", "content": PROMPT},
    {"role": "user", "content": f"Code review the following file: {filecontent}"},
]

res = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

print(res["choices"][0]["message"]["content"])
