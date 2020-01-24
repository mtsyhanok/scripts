from initial_table import table

if __name__ == '__main__':
    result_list = []
    for line in table.split('\n')[1:-1]:
        b = (line.split('|')[1].strip(), line.split('|')[2].strip())
        result_list.append(b)

    result_list.sort()

    result = '|' + '\n|'.join('|'.join(i for i in t) + '|' for t in result_list)
    print(result)
