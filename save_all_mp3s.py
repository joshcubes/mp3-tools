def run(library_path):
    from pathlib import Path
    
    print("Working")

    def process_folders(rootfolder):
        output = open("All MP3 File Locations.txt", "a")
        
        folder = Path(rootfolder)
        for item in folder.iterdir():
            if item.is_dir():
                # recursion for subfolder
                process_folders(item)
            elif item.suffix == ".mp3":
                try:
                    output.write(str(item) + "\n")
                except UnicodeEncodeError:
                    for char in str(item):
                        try:
                            output.write(char)
                        except UnicodeEncodeError:
                            output.write(" <Unicode Encode Error> ")
                    output.write("\n")
        
    print("Output file saved as: All MP3 File Locations.txt")

    
    process_folders(library_path)