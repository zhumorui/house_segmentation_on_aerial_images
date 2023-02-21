with open('data.txt', 'w') as f:

    # Write the column headers to the file
    # f.write('Column 1, Column 2\n')

    # Write the data to the file
    for i in range(10):
        f.write(f'{i}, {i*2}\n')