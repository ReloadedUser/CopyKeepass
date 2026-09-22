# CopyKeepass
## A python program to copy your keepass database





## Download and run
### For PyCharm
1. **Copy the GitHub URL:** Go to the GitHub page of the project, click the green **Code** button, and copy the HTTPS URL (e.g., `https://github.com`).
2. **Open PyCharm's VCS Menu:**
   * If you are on the **Welcome Screen**, click **Clone** (or **Get from Version Control**).
   * If you already have a project open, go to the top menu and select **Git > Clone** (or **VCS > Get from Version Control**).
3. **Paste and Clone:** 
   * In the **Repository URL** tab, paste the link into the **URL** field.
   * In the **Directory** field, choose the local folder where you want to save the project.
   * Click **Clone**.

### For VS Code
1. **Copy the GitHub URL:** Go to the GitHub page of the project, click the green **Code** button, and copy the HTTPS URL.
2. **Open the Command Palette:** Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac) and type **Git: Clone**, then press `Enter`.
   * *Alternative:* Click on the **Source Control** icon in the left Activity Bar and select **Clone Repository**.
3. **Paste and Clone:**
   * Paste the copied GitHub repository URL into the input field at the top and press `Enter`.
   * Select a local directory folder where you want to save the project files.
   * Click **Select as Repository Destination**. When prompted at the bottom right, click **Open** to load the workspace.
  
### Open the python console and type 'pip install pykeepass'

## Inputs

The program requires the following inputs to execute:

### File Paths
* **Old File Path:** The path to the **file you want to copy**.  
  > ⚠️ **Warning:** Provide the exact path to ensure the program can locate the source file.
* **New File Path:** The path to the **file you want to create**.

### Passwords
* **Old File Password:** The **password** to the **file you want to copy (old file)**.
* **New File Password:** The **password** to the **file you want to create (new file)**.  
  > ⚠️ **Warning:** Create a strong password to maintain file security.


## Outputs
- the program creates a .kdbx file in the
  > new file path

- it return the location of the new created file and exit code 0 if it succeed
  
