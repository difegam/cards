
# Cards

Cards is a personal notes taking app that allows you to create, read, update, and delete notes from the command line. It is built using Python and the Click library for creating command line interfaces.

> This is a dummy project to learn how to build command line interfaces with Click.


## Features

- **Create Notes:** Quickly add new notes with optional tags for easy organization.
- **Read Notes:** Access your notes anytime with a simple command.
- **Update Notes:** Modify the content or tags of your existing notes.
- **Delete Notes:** Remove notes that you no longer need.
- **Search and Filter:** Look up notes by keywords or filter them by tags.

## Installation

Ensure you have Python 3.10 or higher installed on your system. This project uses Poetry for dependency management and package installation.

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the project in editable mode to reflect changes immediately:

```bash
pip install --editable .
```

# Install packages in editable mode
This command will install the package in the current directory in editable mode. This means that you can modify the code and the changes will be reflected in the installed package.

# Usage

To get started, run the `cards` command in your terminal. This will display the available options and subcommands:

```bash
cards
```


# Future Improvements
- Add Tests
- Pydantic Models for Notes, Tags and Configurations

# Resources
- [Click Documentation](https://click.palletsprojects.com/en/8.1.x/)
- [Command Line Interface Guidelines](https://clig.dev/#introduction)
- [Click: Build Your Own Command Line Interface Tool](https://www.youtube.com/watch?v=FWacanslfFM)