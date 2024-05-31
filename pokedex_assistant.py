import time

from colorama import Fore, Style, init
from decouple import config
from openai import OpenAI

print(f"{Fore.YELLOW}Starting...{Style.RESET_ALL}")

# Initialize colorama
init(autoreset=True)

# Load environment variables
API_KEY = config('API_KEY', default=None, cast=str)
ASSISTANT_ID = config('ASSISTANT_ID', default=None, cast=str)
DEBUG = config('DEBUG', default=False, cast=bool)


def print_debug_message(output):
    if DEBUG:
        print(output)


client = OpenAI(api_key=API_KEY)
# Create a new thread
welcome = "Welcome to your Pokedex Assistant!"
thread = client.beta.threads.create(
    messages=[
        {
            "role": "assistant",
            "content": welcome
        }
    ]
)
print_debug_message(f"{Fore.GREEN}Thread created: {thread.id}\n")
print(f"{Fore.CYAN}{welcome}")
while True:
    user_input = input(f"{Fore.CYAN}What would you like to know about Pokemon? (type 'q' to quit)\n{Style.RESET_ALL}")
    if user_input.lower() == "q":
        print(f"{Fore.RED}Quitting Pokedex...")
        break
    print(f"{Fore.YELLOW}Processing... Please wait.")
    # Add user message to the thread
    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=user_input
    )

    # Submit the thread to the assistant as a new run
    run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=ASSISTANT_ID)
    print_debug_message(f"{Fore.GREEN}Run created: {run.id}")

    attempt = 1
    while run.status != 'completed':
        run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
        print_debug_message(f'{Fore.YELLOW}Run status: {run.status}, attempt #{attempt}')

        attempt += 1
        time.sleep(1)

    print_debug_message(f"{Fore.GREEN}Run completed, status: {run.status}")

    # Get the latest messages from the thread
    message_response = client.beta.threads.messages.list(thread_id=thread.id)
    messages = message_response.data

    #     # Print the latest response from the assistant
    if messages:
        print(f"{Fore.BLUE}{messages[0].content[0].text.value}\n")
