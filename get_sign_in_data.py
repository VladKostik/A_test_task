with open('../data', 'r') as file:
    lines = file.readlines()
    login = lines[0]
    password = lines[1]

file.close()