from pathlib import Path

import click

from cards import crud
from cards.config import CONFIG_FILE, DEFAULT_NOTES_DIR, load_config, save_config


@click.group()
@click.version_option()
@click.pass_context
def cli(ctx: click.Context) -> None:
    """A simple CLI for managing Notes."""

    config = load_config()

    notes_directory = Path(config.get("notes_dir", str(DEFAULT_NOTES_DIR)))
    notes_directory.mkdir(exist_ok=True)

    ctx.obj = {"notes_directory": notes_directory, "config": config}


@cli.group()
def config() -> None:
    """Configuration options."""


@config.command()
def create() -> None:
    """Create a new configuration."""
    config = load_config()
    save_config(config)
    click.echo("Configuration created.")


@config.command()
def show() -> None:
    """Show the current configuration."""
    if not CONFIG_FILE.exists():
        click.echo("No configuration found.")
        return

    config = load_config()
    click.echo(f"Notes directory: {config.get('notes_directory', DEFAULT_NOTES_DIR)}")


@config.command()
@click.option("--notes_directory", "-n", type=click.Path(exists=True))
def update(notes_dir: str) -> None:
    """Setup the notes directory."""
    config = load_config()
    config.update({"notes_dir": notes_dir})

    save_config(config)
    click.echo(f"Notes directory set to '{notes_dir}'.")


cli.add_command(crud.create)
cli.add_command(crud.read)
cli.add_command(crud.update)
cli.add_command(crud.delete)
cli.add_command(crud.show)
