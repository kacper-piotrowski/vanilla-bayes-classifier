import sys


def open_file_and_save(file_name):
    file_data = []
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
            header = lines[0].strip().split(",")
            type_index = header.index("Type")
            type1_index = header.index("Type.1")
            eg1_index = header.index("Egg Group 1")
            eg2_index = header.index("Egg Group 2")
            for split_line in lines[1:]:
                split_line = split_line.strip().split(",")
                data_vector = [split_line[type_index], split_line[type1_index], split_line[eg1_index], split_line[eg2_index]]
                file_data.append(data_vector)
    except FileNotFoundError:
        sys.exit("File not found, exiting...")
    return file_data

