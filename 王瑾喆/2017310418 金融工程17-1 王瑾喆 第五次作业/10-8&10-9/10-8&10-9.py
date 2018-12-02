files = ['cats1.txt', 'dogs.txt']
for file in files:
    try:
        with open(file, encoding='utf8') as file_res:
            content = file_res.read()
            print(content)
    except FileNotFoundError:
        pass
