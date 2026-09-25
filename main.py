import re
import sys

try:
    import termios
    import tty
except ImportError:
    termios = None
    tty = None

try:
    import msvcrt
except ImportError:
    msvcrt = None

from pykeepass import PyKeePass, create_database


def prompt_hidden(prompt_text):
    """Prompt for input while showing '*' for each typed character."""
    print(prompt_text, end="", flush=True)
    password = ""

    if sys.platform.startswith("win") and msvcrt is not None:
        while True:
            ch = msvcrt.getch()
            if ch in (b"\r", b"\n"):
                print()
                return password
            if ch == b"\x08" or ch == b"\x7f":
                if password:
                    password = password[:-1]
                    print("\b \b", end="", flush=True)
                continue
            if ch in (b"\x03", b"\x04"):
                raise KeyboardInterrupt

            password += ch.decode("utf-8", errors="ignore")
            print("*", end="", flush=True)

    if termios is not None and tty is not None:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setcbreak(fd)
            while True:
                ch = sys.stdin.read(1)
                if ch in ("\n", "\r"):
                    print()
                    return password
                if ch == "\x7f" or ch == "\b":
                    if password:
                        password = password[:-1]
                        print("\b \b", end="", flush=True)
                    continue
                if ch == "\x03":
                    raise KeyboardInterrupt

                password += ch
                print("*", end="", flush=True)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    # Fallback if terminal control is unavailable
    password = input()
    print()
    return password


def user_input():
    param_dict = dict()

    # Give the path to the .kdbx file you want to copy
    print("Enter the path to the old .kdbx file:")
    param_dict["old_path"] = re.sub(r'"', "", input())

    # Give the path to download the new .kdbx file (+name-here is "keypass")
    print("Enter the path to the new .kdbx file:")
    param_dict["new_path"] = re.sub(r'"', "", input())

    # Give the password to the old .kdbx file. Each typed character is shown as *.
    param_dict["source.kp"] = PyKeePass(
        param_dict["old_path"],
        password=prompt_hidden("Enter the password (master key) to the old .kdbx file: ")
    )

    # Give the password to the new .kdbx file
    param_dict["target.kp"] = create_database(
        param_dict["new_path"],
        password=prompt_hidden("Enter the password (master key) to the new .kdbx file: ")
    )

    return param_dict


def copy_groups(param_dict):
    # Copy all Groups (skipping the root group itself)

    for group in sorted(param_dict["source.kp"].groups, key=lambda g: len(g.path)):
        if group.uuid == param_dict["source.kp"].root_group.uuid:
            continue

        # Get the parent group object in the target database
        parent_target_group = param_dict["group_mapping"].get(
            group.parentgroup.uuid, param_dict["target.kp"].root_group
        )

        # Create the subgroup directly inside the target parent
        new_group = param_dict["target.kp"].add_group(parent_target_group, group.name)
        param_dict["group_mapping"][group.uuid] = new_group


def copy_entries(param_dict):
    # Copy all Entries

    for entry in param_dict["source.kp"].entries:
        target_group = param_dict["group_mapping"].get(
            entry.parentgroup.uuid, param_dict["target.kp"].root_group
        )

        param_dict["target.kp"].add_entry(
            target_group,
            entry.title,
            entry.username,
            entry.password,
            url=entry.url,
            notes=entry.notes,
        )


def save_file(param_dict):
    # Commit and save the changes
    param_dict["target.kp"].save()


def main():
    data_dict = user_input()

    data_dict["target.kp"].root_group.name = data_dict["source.kp"].root_group.name

    # Map the source root UUID directly to the target root group object
    data_dict["group_mapping"] = {
        data_dict["source.kp"].root_group.uuid: data_dict["target.kp"].root_group
    }

    copy_groups(data_dict)
    copy_entries(data_dict)
    save_file(data_dict)


if __name__ == "__main__":
    main()
