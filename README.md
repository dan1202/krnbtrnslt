python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

Create a `src/credentials.json` file with your Telegram API credentials and
DeepL API key in the following format:

```json
{
  "telegram_api": [
    {"api_id": "<API_ID>", "api_hash": "<API_HASH>"}
  ],
  "deepl_api_key": "<DEEPL_KEY>"
}
```
