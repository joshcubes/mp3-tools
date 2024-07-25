global files_scanned
files_scanned = 0

def run(library_path):
    from pathlib import Path

    def process_folders(rootfolder):
        global files_scanned
        output = open("All MP3 File Locations.txt", "a")
        
        # Iterates over all mp3 files
        folder = Path(rootfolder)
        for item in folder.iterdir():
            if item.is_dir():

                process_folders(item)
            elif item.suffix == ".mp3":
                files_scanned += 1
                print(f"Working: {files_scanned} files scanned so far.", end=' '*10 + '\r')

                try:
                    output.write(str(item) + "\n")
                except UnicodeEncodeError:
                    for char in str(item):
                        try:
                            output.write(char)
                        except UnicodeEncodeError:
                            output.write(" <Unicode Encode Error> ")
                    output.write("\n")
    
    print(f"{files_scanned} files have been scanned.\n")
    print("Output file saved as: All MP3 File Locations.txt")

    
    process_folders(library_path)