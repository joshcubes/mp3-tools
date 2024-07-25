global total_length
global files_scanned
total_length = 0.0
files_scanned = 0

def run(library_path):
    from pathlib import Path
    from mutagen.mp3 import MP3

    # Iterates over all subfolders looking for mp3 files
    def process_folders(rootfolder):
        global total_length
        global files_scanned
        folder = Path(rootfolder)
        
        
        for item in folder.iterdir():
            if item.is_dir():
                # recursion for subfolder
                process_folders(item)
            elif item.suffix == ".mp3":
                # opens the file and gets the length
                audio = MP3(item)
                total_length += audio.info.length
                files_scanned += 1
                print(f"Working: {files_scanned} files scanned so far.", end="\r")

    
    
    process_folders(library_path)
    print(f"{files_scanned} files have been scanned.\n")
    print(f"Your library has a total length of {total_length} Secconds.\n")
    
    print("Which is:")
    remainder_length = total_length
    time_days = 0
    time_hours = 0
    time_minutes = 0
    time_secconds = 0.0
    #Days
    if total_length >= 86400:
        time_days = remainder_length // 86400
        remainder_length -= (time_days * 86400)

        time_hours = remainder_length // 3600
        remainder_length -= (time_hours * 3600)
        
        time_minutes = remainder_length // 60
        remainder_length -= (time_minutes * 60)
        
        time_secconds = remainder_length
        
        print(int(time_days), "Days")
        print(int(time_hours), "Hours")
        print(int(time_minutes), "Minutes")
        print(round(time_secconds,2), "Secconds")
    # Hours
    elif total_length >= 3600:
        time_hours = remainder_length // 3600
        remainder_length -= (time_hours * 3600)
        
        time_minutes = remainder_length // 60
        remainder_length -= (time_minutes * 60)
        
        time_secconds = remainder_length
    
        print(int(time_hours), "Hours")
        print(int(time_minutes), "Minutes")
        print(round(time_secconds,2), "Secconds")
    # Minutes
    elif total_length >= 60:
        time_minutes = remainder_length // 60
        remainder_length -= (time_minutes * 60)
        
        time_secconds = remainder_length
        
        print(int(time_minutes), "Minutes")
        print(round(time_secconds,2), "Secconds") 
    # Secconds
    else:
        time_secconds = remainder_length

        print(round(time_secconds,2), "Secconds")