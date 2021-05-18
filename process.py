import csv
import os


def WriteToCSV(filename, headers, data_row):
    """Writes a row of data to a CSV file.

    Parameters
    ----------
    filename : str
        Name of the output CSV file.
    headers : list
        Header fieldnames of the data.
    data_row :csv.Dict
        List of values corresponding to the line to be exported.
    """
    if os.path.exists(filename):
        append_write = 'a'  # append if already exists
    else:
        append_write = 'w'  # make a new file if not

    f = open(filename, append_write)
    writer = csv.DictWriter(f, headers)
    writer.writeheader()
    writer.writerow(data_row)


file = "data/E288.csv"

with open(file, newline=None) as csvfile:

    lines = list()
    Writer = False
    headers = ['Date/Time', 'Infos', 'Temperature', 'C1', 'C2', 'C3', 'Consigne', 'Puissance']
    
    spamreader = csv.DictReader(csvfile, headers)
    # for i in range(11):
    #    next(spamreader)
    for row in spamreader:
        if 'Marche' in row['Infos']:
            print('Début')
            print(row['Date/Time'])
            Writer = True
             
        if 'RAZ' in row['Infos']:
            print('Fin')
            print(row['Date/Time'])
            Writer = False

        if Writer == True:
            lines.append(list(row.values())[0:2] + list(row.values())[6:])
            dicto = dict(zip(['Date/Time', 'Infos', 'Temperature', 'Consigne', 'Puissance'], lines))
            print(dict(dicto))
            WriteToCSV('data.csv', ['Date/Time', 'Infos', 'Temperature', 'Consigne', 'Puissance'], dicto)
