import os
import shutil
from colorama import Fore, Style, init
from tqdm import tqdm

init(autoreset=True)

def main():
    print(f"{Fore.CYAN}{Style.BRIGHT}=== File Organizer ===\n")
    
    home = os.path.expanduser("~")
    
    src_input = input(f"{Fore.YELLOW}Source folder: ")
    dst_input = input(f"{Fore.YELLOW}Target folder: ")
    ext_input = input(f"{Fore.YELLOW}Extension (e.g. png): ").lstrip('.')
    
    src_dir = os.path.join(home, src_input)
    dst_dir = os.path.join(home, dst_input)
    
    if not os.path.exists(src_dir):
        print(f"\n{Fore.RED}[Error] Source directory not found: {src_dir}")
        return

    files = [f for f in os.listdir(src_dir) 
             if f.lower().endswith(f".{ext_input.lower()}")]
    
    if not files:
        print(f"\n{Fore.MAGENTA}No .{ext_input} files found in {src_input}.")
        return

    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
        print(f"{Fore.GREEN}[Created] Target directory: {dst_input}")

    print(f"\n{Fore.BLUE}Moving {len(files)} files...")
    
    for filename in tqdm(files, desc="Processing", unit="file", colour="green"):
        shutil.move(os.path.join(src_dir, filename), 
                    os.path.join(dst_dir, filename))

    print(f"\n{Fore.GREEN}{Style.BRIGHT}Success! All files moved to {dst_input}.")

if __name__ == "__main__":
    main()

