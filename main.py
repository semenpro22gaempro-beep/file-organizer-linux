import os
import shutil
from colorama import Fore, Style, init
from tqdm import tqdm

init(autoreset=True)

def main():


    organizer_art = rf"""
    {Fore.BLUE}░░▒▒▓▓██████████████████████████████████████████████▓▓▒▒░░
    {Fore.BLUE}░▒▓████████████████████████████████████████████████████▓▒░
    {Fore.BLUE}▒▓██   {Fore.GREEN}{Style.BRIGHT}____  _____   ____    _    _   _ ___ _____ _____  {Fore.BLUE}██▓▒
    {Fore.BLUE}▓██   {Fore.GREEN}{Style.BRIGHT}/ __ \|  __ \ / ___|  / \  | \ | |_ _|__  /| ____|  {Fore.BLUE}██▓
    {Fore.BLUE}▓██  {Fore.GREEN}{Style.BRIGHT}| |  | | |__) | |  _  / _ \ |  \| || |  / / |  _|    {Fore.BLUE}██▓
    {Fore.BLUE}▒▓██ {Fore.GREEN}{Style.BRIGHT}| |__| |  _  /| |_| |/ ___ \| |\  || | / /_ | |___   {Fore.BLUE}██▓▒
    {Fore.BLUE}░▒▓██ {Fore.GREEN}{Style.BRIGHT}\____/|_| \_\ \____/_/   \_\_| \_|___/____||_____| {Fore.BLUE}██▓▒░
    {Fore.BLUE}░░▒▒▓▓██████████████████████████████████████████████▓▓▒▒░░
    """

    print(organizer_art)
    g = "\033[32m"
    y = "\033[35m"
    print(f" {y}[1]{y}{g}rm{g}\n {y}[2]{y}{g}mv{g}\n {y}[3]{y}{g}rn{g}\n {y}[4]{y}{g}distr{g}\n {y}[5]{y}{g}ls{g}\n {y}[6]{y}{g}cd{g}\n {y}[7]{y}{g}cdup{g}\n {y}[8]{y}{g}cdpath{g}\n {y}[9]{y}{g}exit{g}")

    while True:

        cmd = input("Command: ").strip().lower()
        home = os.path.expanduser("~")

        if cmd == "mv":
            src_input = input(f"{Fore.YELLOW}Source folder: ")
            dst_input = input(f"{Fore.YELLOW}Target folder: ")
            ext_input = input(f"{Fore.YELLOW}Extension (e.g. png): ").lstrip('.')


            src_dir = os.path.join(home, src_input)
            dst_dir = os.path.join(home, dst_input)

            if not os.path.exists(src_dir):
                print(f"\n{Fore.RED}[Error] Source directory not found: {src_dir}")
                return


            files = [f for f in os.listdir(src_dir)
                    if f.lower().endswith(f".{ext_input.lower()}") and os.path.isfile(os.path.join(src_dir, f))]

            if not files:
                print(f"\n{Fore.MAGENTA}No .{ext_input} files found.")
                return

            if not os.path.exists(dst_dir):
                os.makedirs(dst_dir)
                print(f"{Fore.GREEN}[Created] Target directory: {dst_input}")

            print(f"\n{Fore.BLUE}Moving {len(files)} files...")
            for filename in tqdm(files, desc="Moving", unit="file", colour="green"):
                shutil.move(os.path.join(src_dir, filename), os.path.join(dst_dir, filename))

            print(f"\n{Fore.GREEN}{Style.BRIGHT}Success! All files moved.")

        elif cmd == "rm":
            src_input = input(f"{Fore.YELLOW}Source folder: ")
            ext_input = input(f"{Fore.YELLOW}Extension (e.g. png): ").lstrip('.')

            src_dir = os.path.join(home, src_input)

            if not os.path.exists(src_dir):
                print(f"\n{Fore.RED}[Error] Source directory not found.")
                return

            files = [f for f in os.listdir(src_dir)
                    if f.lower().endswith(f".{ext_input.lower()}") and os.path.isfile(os.path.join(src_dir, f))]

            if not files:
                print(f"\n{Fore.MAGENTA}No .{ext_input} files found.")
                return

            print(f"\n{Fore.RED}Deleting {len(files)} files...")
            for filename in tqdm(files, desc="Removing", unit="file", colour="red"):
                os.remove(os.path.join(src_dir, filename))

            print(f"\n{Fore.GREEN}{Style.BRIGHT}Success! All files removed.")

        elif cmd == "rn":
            src_input = input(f"{Fore.YELLOW}Source folder: ")
            ext_input = input(f"{Fore.YELLOW}Extension (e.g. png): ").lstrip('.')
            nam_input = input(f"{Fore.YELLOW}Future name: ")


            src_dir = os.path.join(home, src_input)

            if not os.path.exists(src_dir):
                print(f"\n[Error] Source directory not found: {src_dir}")
                return


            files = [f for f in os.listdir(src_dir)
                    if f.lower().endswith(f".{ext_input.lower()}") and os.path.isfile(os.path.join(src_dir, f))]

            if not files:
                print(f"\nNo .{ext_input} files found in directory.")
                return

            print(f"\nRenaming {len(files)} files...")


            for i, filename in enumerate(tqdm(files, desc="Processing", unit="file"), start=1):
                old_path = os.path.join(src_dir, filename)


                new_name = f"{nam_input}_{i}.{ext_input}"
                new_path = os.path.join(src_dir, new_name)

                try:
                    os.rename(old_path, new_path)
                except FileExistsError:
                    print(f"\n[Skip] File {new_name} already exists.")
                except Exception as e:
                    print(f"\n[Error] Could not rename {filename}: {e}")

            print(f"\nDone! Successfully processed {len(files)} files.")

        elif cmd == "exit":
            break

        elif cmd == "distr":
            CATEGORIES = {
            'Images': ['.jpg', '.jpeg', '.png', '.gif', '.webp'],
            'Videos': ['.mp4', '.mkv', '.mov', '.avi'],
            'Docs': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
            'Music': ['.mp3', '.wav', '.flac'],
            'Archives': ['.zip', '.rar', '.tar', '.gz']
            }
            src_input = input(f"Folder to sort (inside ~): ")
            src_dir = os.path.join(home, src_input)

            if not os.path.exists(src_dir):
                print(f"{Fore.RED}[Error] Folder not found!")
                return

            files = [f for f in os.listdir(src_dir) if os.path.isfile(os.path.join(src_dir, f))]

            if not files:
                print(f"{Fore.MAGENTA}No files to sort.")
                return

            for filename in tqdm(files, desc="Sorting", unit="file", colour="cyan"):
                file_path = os.path.join(src_dir, filename)
                _, ext = os.path.splitext(filename)
                ext = ext.lower()

                target_folder = "Others"
                for category, extensions in CATEGORIES.items():
                    if ext in extensions:
                        target_folder = category
                        break

                target_path = os.path.join(src_dir, target_folder)
                os.makedirs(target_path, exist_ok=True)
                shutil.move(file_path, os.path.join(target_path, filename))

            print(f"\n{Fore.GREEN}{Style.BRIGHT}Organization complete!")
        elif cmd == "cdpath":
            current_path = os.getcwd()
            path = input("Enter the absolute path:")
            os.chdir(f"{path}")
            print(f"main directory:{current_path}")
        elif cmd == "cdup": 
            current_path = os.getcwd()
            os.chdir('..')
            print(f"main directory:{current_path}") 
        elif cmd == "cd":
            current_path = os.getcwd() 
            os.chdir(f"{home}") 
            print(f"main directory: {current_path}")			
        elif cmd == "ls":
            ls = os.listdir('.') 
            print(ls) 
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()
