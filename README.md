<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/b02d0e17-4424-4b77-8e13-35a12f8f8314" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/7cb0a8e7-b062-4729-93ec-ab67e3cbf8a1" />




#  Python File Organizer for Linux
A Python program
for working with large numbers of files by extension.


## Commands
- **rm** - Deletes all files of the specified extension.
- **mv** - Moves files with the specified extension to the user-specified folder
- **distr** - Automatically sort files into folders(Pictures-jpg,png),You can also make your own config(down) 
- **exit** - Exit script
- **rn** - Renames all files with the specified extension.
- **cd** - goes to the main directory
- **cdup** - goes to a higher level
- **cdpath** - goes to the directory at the specified path
- **help** - all commands
- **ls** - all files in directory
##  Installation
Clone the repository and run the setup script:
```bash
git clone https://github.com/semenpro22gaempro-beep/file-organizer-linux.git
```
```bash
cd file-organizer-linux
```
```bash
python3 setup.py
```
**bash:*
```bash
source ~/.bashrc
```
**zsh:*
```bash
source ~/.zshrc
```




##  YOUR OWN AUTO-SORTING CONFIG
To create your own configuration for sorting files into folders:

**open folder:*
```bash
cd file-organizer-linux
```
**edit config:*
```bash
nano sortconfig.json
```
**Sample and default config:*
}**
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Docs": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Python": [".py", ".pyw"],
    "java": [".java"],
    "с++": [".cpp"],
    "rust": [".rs"]
}**
