history = []


def add_user_message(text):
    history.append({"role": "user", "content": text})


def add_assistant_message(text):
    history.append({"role": "assistant", "content": text})


def get_history() -> list:
    return history


def trim_history(max_pairs: int = 5) -> None:
    max_messages = max_pairs * 2
    while len(history) > max_messages:
        history.pop(0)  # drop oldest user message
        history.pop(0)  # drop its paired assistant message