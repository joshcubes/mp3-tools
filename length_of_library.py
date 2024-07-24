def run(library_path):
    from pathlib import Path
    
    print("Working")

    def process_folders(rootfolder):
        folder = Path(rootfolder)
        for item in folder.iterdir():
            if item.is_dir():
                # recursion for subfolder
                process_folders(item)
            elif item.suffix == ".mp3":
                process_file(item)
    
    def process_file(file):
        print(file)
    
    process_folders(library_path)