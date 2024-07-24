global files_scanned
files_scanned = 0

def run(library_path):
    from pathlib import Path
    
    # Iterates over all subfolders looking for mp3 files
    def process_folders(rootfolder):
        global files_scanned
        folder = Path(rootfolder)
        
        print()
        
        for item in folder.iterdir():
            if item.is_dir():
                # recursion for subfolder
                process_folders(item)
            elif item.suffix == ".mp3":
                # Process File Here as item

                files_scanned += 1
                print(f"Working: {files_scanned} files scanned so far.", end=' '*10 + '\r')

    
    
    process_folders(library_path)
    print(f"{files_scanned} files have been scanned.\n")
