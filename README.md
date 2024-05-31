# Pokedex Open AI Assistant

Console app that allows the user to ask questions about pokemon data. This is thanks to an Open AI assistant trained and configured with pokedex data in json format.

## Run Chat

###  Open AI assistant set up
1. Create Opean AI account then get your key at https://platform.openai.com/api-keys

2. Go to your assistants and create a new one, in the title put Pokedex, and in the instructions you may input this:
Answer questions about pokemon data (from the pokedex.json).

3. In your assistant, allow file search and upload the pokedex.json file located in this repository.

4. Copy the assistant ID and also the key you generated earlier as this values will be used in your .env file.

### Clone repository

1. Clone the repository:

```bash
git clone https://github.com/molero3111/pokedex-open-ai-assistant
```

2. cd into project:
```bash
cd pokedex-open-ai-assistant/
```

### Environment set up

1. create virtualenv

```bash
virtualenv pokedex_venv
source pokedex_venv/bin/activate
```

2. Install requirements:

```bash
pip install -r requirements.txt
```

3. Create .env file from .env.example:
```bash
cp .env.example .env
```
4. Modify API_KEY, ASSISTANT_ID with your key and assistant ID you set up earlier.

### Run pokedex chat:
```bash
python pokedex_assistant.py
```