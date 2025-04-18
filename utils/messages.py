import json
from pathlib import Path


def load_messages() -> dict:
    """Util for loading json file, which stores messages.

        Returns:
            dict: file data.
    """
    file_path = Path(__file__).parent.parent / "data/text/messages.json"
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


messages = load_messages()


def get_message(key: str, **kwargs) -> str:
    """Text getter from the dict type storage variable - "messages".
        Args:
            key (str): special name for the message section in the base json file.
            **kwargs: arguments with needed value which can be inserted into the message string.

        Returns:
            str: filled in message string.
    """
    return messages.get(key, "").format(**kwargs)
