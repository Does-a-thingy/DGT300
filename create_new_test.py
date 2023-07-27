def fil_fch(file):
    fetched_lst = []
    final = []
    try:
        with open(file) as f:
            print(f.readlines())
    except:
        with open(file, 'w') as f:
            print('new file')
            f.write('This is a new file')

drab = fil_fch('test_txt_file.txt')