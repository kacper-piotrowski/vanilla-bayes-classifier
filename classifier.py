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

def train(data):
    eg1_counts = {}
    type_counts = {}
    eg2_counts = {}
    type1_counts = {}
    for row in data:
        if row[2] not in type_counts:
            type_counts[row[2]] = {}
        if row[2] not in eg2_counts:
            eg2_counts[row[2]] = {}
        if row[2] not in type1_counts:
            type1_counts[row[2]] = {}
        eg1_counts[row[2]] = eg1_counts.get(row[2], 0) + 1
        type_counts[row[2]][row[0]] = type_counts[row[2]].get(row[0], 0) + 1
        eg2_counts[row[2]][row[3]] = eg2_counts[row[2]].get(row[3], 0) + 1
        type1_counts[row[2]][row[1]] = type1_counts[row[2]].get(row[1], 0) + 1
    return eg1_counts, type_counts, eg2_counts, type1_counts

def classify(vector, eg1_counts, type_counts, eg2_counts, type1_counts):
    typeval = vector[0]
    type1val = vector[1]
    eg2val = vector[3]
    results_dict = {}
    for eg1val in eg1_counts:
        result = (eg1_counts.get(eg1val, 0) * type_counts.get(eg1val, {}).get(typeval, 0) *
                  eg2_counts.get(eg1val, {}).get(eg2val, 0) * type1_counts.get(eg1val, {}).get(type1val, 1))
        results_dict[eg1val] = result
    max_result = sorted(results_dict.items(), key=lambda item: item[1], reverse=True)
    return max_result[0][0]


