from pathlib import Path

from cards.config import get_config_dir


def load(path: str) -> str:
    """Load content from a file."""
    notes_dir = get_config_dir()
    with (notes_dir / Path(path)).open(mode="r") as file:
        return file.read()


def save(path: str, content: str) -> None:
    """Save content to a file."""
    notes_dir = get_config_dir()
    with (notes_dir / Path(path)).open(mode="w+") as file:
        file.write(content)


def exists(path: str) -> bool:
    """Check if a file exists."""
    notes_dir = get_config_dir()
    return (notes_dir / Path(path)).is_file()
