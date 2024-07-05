import json
import os
import sys
from datetime import datetime
from pathlib import Path

import click

from cards.file import exists, load, save


@click.command()
@click.argument("name")
@click.option("--content", prompt=True, help="Card content.")
@click.option("--tags", "-t", help="Comma-separated list of tags.")
@click.pass_context
def create(ctx: click.Context, name: str, content: str, tags: str) -> None:
    """Create a new card."""
    notes_directory = ctx.obj["notes_directory"]

    # Create a new file in the notes directory.
    note_file = f"{name}.txt"
    if (notes_directory / Path(note_file)).exists():
        click.echo(f"Note {note_file} already exists.")
        return

    note_data = {
        "name": name,
        "content": content,
        "tags": tags.split(",") if tags else [],
        "created_at": datetime.now().isoformat(),
    }

    with (notes_directory / Path(note_file)).open(mode="a+") as note:
        json.dump(note_data, note)
    click.echo(f"Note {note_file} created.")


@click.command()
@click.argument("name")
@click.pass_context
def read(ctx: click.Context, name: str) -> None:
    """Read a note."""

    notes_directory: Path = ctx.obj["notes_directory"]
    note_name = f"{name}.txt"

    if not (notes_directory / note_name).exists():
        click.echo(f"Note with name '{name}' does not exist.")
        sys.exit(1)

    with (notes_directory / note_name).open(mode="r") as file:
        note_data = json.load(file)

    click.echo(f"name: {name}")
    click.echo(f"Tags: {', '.join(note_data['tags'])}")
    click.echo(f"Created At: {note_data['created_at']}")
    click.echo(f"Content:\n{note_data['content']}")


@click.command()
@click.argument("name")
@click.option("--content", help="New content of the note")
@click.option("--tags", help="Comma-separated list of new tags")
def update(name: str, content: str, tags: str) -> None:
    """Update the note."""
    note_name = f"{name}.txt"

    if not exists(note_name):
        click.echo(f"Note with name '{name}' does not exist.")
        return

    note_data = json.loads(load(note_name))

    if not note_data:
        click.echo(f"Note '{name}' is empty.")
        return

    if content:
        note_data.update({"content": content})

    if tags:
        note_data.update(
            {"tags": tags.split(",") if tags else note_data.get("tags", [])}
        )

    note_data.update({"updated_at": datetime.now().isoformat()})

    save(note_name, json.dumps(note_data))
    click.echo(f"Note '{name}' has been updated.")


@click.command()
@click.argument("name")
@click.pass_context
def delete(ctx: click.Context, name: str) -> None:
    """Delete the note."""

    notes_directory: Path = ctx.obj["notes_directory"]
    note_name = f"{name}.txt"

    note_path = notes_directory / note_name

    if not note_path.exists():
        click.echo(f"Note with name '{name}' does not exist.")
        sys.exit(1)

    # Delete the note file.
    note_path.unlink()
    click.echo(f"Note '{name}' has been deleted.")


@click.command()
@click.option("--tag", help="Filter notes by tag")
@click.option("--keyword", help="Search notes by keyword")
@click.pass_context
def show(ctx: click.Context, tag: str, keyword: str) -> None:
    """Show notes."""
    notes_directory: Path = ctx.obj["notes_directory"]

    notes = notes_directory.glob("*.txt")

    if not tag and not keyword:
        click.echo(f"Notes:\n{', '.join([note.stem for note in notes])}")
        sys.exit(1)

    results: list[str] = []

    for note in notes:
        with note.open(mode="r") as file:
            note_data = json.load(file)

        if tag and tag not in note_data["tags"]:
            continue

        if keyword and keyword not in note_data["content"]:
            continue

        results.append(note.stem)

    click.echo("Notes:")
    for result in results:
        click.echo(f"- {result}")
