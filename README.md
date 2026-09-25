# CopyKeepass

CopyKeepass is a lightweight Python script that helps you duplicate one KeePass database into a new `.kdbx` file while preserving the folder structure and entries.

It is useful when you want to create a copy of an existing KeePass database with a new file name or new master password, without manually recreating the database structure.

## Features

- Copies KeePass groups and subgroups
- Copies entries and preserves:
  - title
  - username
  - password
  - URL
  - notes
- Creates a new target KeePass database from a source database
- Runs from the command line with simple prompts

## Requirements

- Python 3
- `pykeepass`

Install the dependency:

```bash
pip install pykeepass
```

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/ReloadedUser/CopyKeepass.git
cd CopyKeepass
```

2. Install the dependencies:

```bash
pip install pykeepass
```

3. Run the script:

```bash
python main.py
```

4. When prompted, provide:
   - the path to the source `.kdbx` file
   - the path to the new `.kdbx` file to create
   - the source database master password
   - the new database master password

## How It Works

The script:

1. Loads the source KeePass database using `PyKeePass`
2. Creates a new database at the target path
3. Copies the root group name and hierarchy from the source database
4. Recreates sibling and nested groups in the target database
5. Adds each entry into the appropriate target group
6. Saves the new database

## Notes

- Always keep backups of your KeePass files before making copies.
- Use a strong password for the newly created database.
- This script is intended for terminal use and uses interactive prompts.

## Example

```bash
python main.py
```

Example prompts:

```text
Enter the path to the new .kdbx file:
/path/to/new_database.kdbx

Enter the path to the old .kdbx file:
/path/to/source_database.kdbx

Enter the password (master key) to the old .kdbx file:
********

Enter the password (master key) to the new .kdbx file:
********
```

## Contributing

Pull requests and suggestions are welcome. If you would like to improve the tool, please fork the repository and submit your changes.
