import os
import shutil
from colorama import Fore, Style, init
from tqdm import tqdm

init(autoreset=True)

def main():
    print(f"{Fore.CYAN}{Style.BRIGHT}=== File Organizer ===\n")

    cmd = input("Command (mv/rm): ").strip().lower()
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

    
    else:
        print(f"{Fore.RED}Unknown command.")


if __name__ == "__main__":
    main()
