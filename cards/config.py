import json
from pathlib import Path
from typing import TypedDict

CONFIG_DIR = Path.home() / ".config" / "notes"
CONFIG_FILE = CONFIG_DIR / "config.json"
DEFAULT_NOTES_DIR = Path.home() / ".notes"


class Config(TypedDict):
    notes_dir: str


def load_config(config_path: Path = CONFIG_FILE) -> Config:
    """Load the configuration from a file."""
    if not config_path.exists():
        return {"notes_dir": str(DEFAULT_NOTES_DIR)}

    with config_path.open(mode="r") as app_config:
        return json.load(app_config)


def save_config(config: Config) -> None:
    """Save the configuration to a file."""
    if not CONFIG_DIR.exists():
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    with CONFIG_FILE.open(mode="w") as app_config:
        json.dump(config, app_config, indent=4)


def get_config_dir() -> Path:
    """Return the path to the configuration directory."""
    config = load_config()
    config_dir = config.get("notes_dir")

    if config_dir is None or not Path(config_dir).exists():
        raise ValueError("Notes directory not configured.")

    return Path(config_dir)
