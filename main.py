import openai
import string
import random
import sys

openai.api_key = '###YOUR_TOKEN_GOES_HERE###'

tokens_to_spend = 10000


def generate_random_string(length: int) -> str:
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def progress_bar(progress, total, length=50):
    percent = (progress / total) * 100
    filled_length = int(length * progress // total)
    bar = '█' * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r|{bar}| {percent:.2f}% Complete')
    sys.stdout.flush()

def spend_tokens():
    messages = [
        {"role": "system", "content": "Answer to everything with OK."},
        {"role": "user", "content": generate_random_string(10000)}
    ]

    response = openai.chat.completions.create(
        model="gpt-4", 
        messages=messages,
        max_tokens=10 
    )

    return response.usage.total_tokens

def main():
