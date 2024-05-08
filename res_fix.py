#PLACE INSIDE STEAM FOLDER USUALLY IN: Steam/steamapps/common/AoT2
#Replaces corresponding bytes with the new ones given in a file.
def hex_replace(file_path, search_hex, replace_hex):
    try:
        # Convert hex strings to bytes
        search_bytes = bytes.fromhex(search_hex)
        replace_bytes = bytes.fromhex(replace_hex)

        # Read the original binary data
        with open(file_path, 'rb') as file:
            data = file.read()

        # Check if file exists
        if data.find(search_bytes) == -1:
            raise ValueError("Search pattern not found in the file.")

        # Replace the sequence
        data = data.replace(search_bytes, replace_bytes)

        # Write the modified data back to the same file
        with open(file_path, 'wb') as file:
            file.write(data)
        print("File updated successfully.")

    except FileNotFoundError:
        print("Error: The file was not found. Please check the file path.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



search_hex = ''  
replace_hex = ''

while True:    
    print('Please select resolution by inputing the corresponding letter:')
    print('a) 2560 x 1080')
    print('b) 3440 x 1440')
    target_resolution = input('Enter corresponding letter and press enter: ')
    if target_resolution == 'a':
        search_hex = '80 07 38 04' # 1920 x 1080
        replace_hex = '00 0A 38 04' # 2560 x 1080
        break
    if target_resolution == 'b':
        search_hex = '00 0A A0 05' # 2560 x 1440
        replace_hex = '70 0D A0 05' # 3440 x 1440
        break


file_paths = ['AOT2_AS.exe','AOT2_EU.exe','AOT2_JP.exe']
  # Example replacement pattern
for file_path in file_paths:
    hex_replace(file_path, search_hex, replace_hex)
print('Fix applied successfully.')
