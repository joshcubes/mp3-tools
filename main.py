import useful_bits, length_of_library, save_all_mp3s

from pathlib import Path


def get_library_location():

    valid_location = False
    
    while not valid_location:
        location = ""
        formatted_location = ""    
        
        location = input("Please enter the location of your library: ")
        for char in location:
            if char == "\\":
                char = "/"
            formatted_location += char
        
        
        library = Path(formatted_location)
        if library.is_dir():
            valid_location = True
        else:
            print("Please enter a valid Path.")
    
    return formatted_location


print("""Welcome to josh's mp3 tools
These are the available options:
1) Save the paths of all your MP3 Files to a text document
2) Collate the entire length of the songs in your library
""")

print("""####################
Please note at the current moment in time the program works with libraries formatted using the structure: Library/Artist/Album/Song eg. How iTunes organises it's library
####################
 """)

choice = useful_bits.intinput("Please enter your choice: ")

if choice == 1:
    library = get_library_location()
    save_all_mp3s.run(library)

if choice == 2:
    library = get_library_location()
    length_of_library.run(library)