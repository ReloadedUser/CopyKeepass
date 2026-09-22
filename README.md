# CopyKeepass
# CopyKeePass

https://img.shields.io/badge/language-python-blue
https://img.shields.io/badge/status-open-purple
https://img.shields.io/badge/security level-high-red

A Python program designed to securely copy and replicate your KeePass database.

---

## 🚀 Download and Run

### For PyCharm
1. **Copy the GitHub URL:** Go to the GitHub page of the project, click the green **Code** button, and copy the HTTPS URL.
2. **Open PyCharm's VCS Menu:** 
   * If you are on the Welcome Screen, click **Clone** (or *Get from Version Control*).
   * If you already have a project open, go to the top menu and select **Git > Clone** (or *VCS > Get from Version Control*).
3. **Paste and Clone:** In the *Repository URL* tab, paste the link into the **URL** field. In the **Directory** field, choose the local folder where you want to save the project. Click **Clone**.

### For VS Code
1. **Copy the GitHub URL:** Go to the GitHub page of the project, click the green **Code** button, and copy the HTTPS URL.
2. **Open the Command Palette:** Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac), type `Git: Clone`, and press `Enter`.
   * *Alternative:* Click on the **Source Control** icon in the left Activity Bar and select **Clone Repository**.
3. **Paste and Clone:** Paste the copied GitHub repository URL into the input field at the top and press `Enter`.
4. **Select Destination:** Choose a local directory folder where you want to save the project files. Click **Select as Repository Destination**.
5. **Open Workspace:** When prompted at the bottom right, click **Open** to load the workspace.

---

## 📦 Dependencies

Open your terminal or Python console and install the required library:

```bash
pip install pykeepass
```

---

## 📥 Inputs

The program requires the following inputs to execute:

### File Paths
* **Old File Path:** The path to the file you want to copy.
  * ⚠️ **Warning:** Provide the exact path to ensure the program can locate the source file.
* **New File Path:** The path to the file you want to create.

### Passwords
* **Old File Password:** The password to the file you want to copy (old file).
* **New File Password:** The password to the file you want to create (new file).
  * ⚠️ **Warning:** Create a strong password to maintain file security.

---

## 📤 Outputs

* The program creates a `.kdbx` file at the specified new file path.
* It returns the location of the newly created file.
* It returns an exit code of `0` upon a successful operation.


## Outputs
- the program creates a .kdbx file in the
  > new file path

- it return the location of the new created file and exit code 0 if it succeed
  
