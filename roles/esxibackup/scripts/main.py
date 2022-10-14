import re
import yaml
import sys

filename = str(sys.argv[1])

file = open( filename )
file_content = file.read()

# Split each line on a newline
split_lines = re.split(r'\n', file_content)
line_count = len(split_lines)

# Create list which will be output
output_list = []

# Extract the required data from each line and add it to the list
for i in range(line_count):
    split_line = re.split(r'\s{2,}', split_lines[i])
#    print(split_line)
    split_san_string = split_line[2].split(' ', 1)
    dictionary = {
        'VMID': split_line[0],
        'Name': split_line[1].replace(' ', '').replace('(', '').replace(')', ''),
        'SAN': split_san_string[0].replace('[', '').replace(']', ''),
        'Folder': split_san_string[1].split('/')[0].replace(' ', '\ ').replace('(', '\(').replace(')', '\)')
    }
    output_list.append(dictionary)

# Return the list of dictionaries
print(yaml.dump(output_list))
