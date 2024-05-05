def down_file(content, file_name):
    with open('./data/' + file_name, 'w') as w:
        w.write(content)
    return f'Successfully written {file_name}'
