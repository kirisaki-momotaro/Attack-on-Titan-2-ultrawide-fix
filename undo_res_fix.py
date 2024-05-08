#PLACE INSIDE STEAM FOLDER, USUALLY IN: Steam/steamapps/common/AoT2
#Replaces corresponding bytes with the new ones given in a file.
def hex_replace(file_path, search_hex, replace_hex , res):
    try:
        # Convert hex strings to bytes
        search_bytes = bytes.fromhex(search_hex)
        replace_bytes = bytes.fromhex(replace_hex)

        # Read the original binary data
        with open(file_path, 'rb') as file:
            data = file.read()   

        # Check if the search bytes are present in the data
        if data.find(search_bytes) == -1:
            print(f'No fix required {file_path} {res}.')
        else:
            data = data.replace(search_bytes, replace_bytes)

            # Write the modified data back to the same file
            with open(file_path, 'wb') as file:
                file.write(data)   
                
            print(f'Fix undo successfull {file_path} {res}.')    

    except FileNotFoundError:
        print("Error: The file was not found. Please check the file path.")       
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
   



search_hex = ''  
replace_hex = ''
file_paths = ['AOT2_AS.exe','AOT2_EU.exe','AOT2_JP.exe']  

for file_path in file_paths:
    search_hex = '00 0A 38 04' # 2560 x 1080
    replace_hex = '80 07 38 04' # 1920 x 1080
    res = '1920 x 1080'
    hex_replace(file_path, search_hex, replace_hex,res)
    search_hex = '70 0D A0 05' # 3440 x 1440
    replace_hex = '00 0A A0 05' # 2560 x 1440
    res = '2560 x 1440'
    hex_replace(file_path, search_hex, replace_hex,res)

input('Press any key to exit.')
