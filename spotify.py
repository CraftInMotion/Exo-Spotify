import csv

def read_spotify_data(file_path, debug=True):
    spotify_data = []
    
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            spotify_data.append(row)

    if debug: 
        for record in spotify_data[:5]:
            print(record)

    return spotify_data

dataset = read_spotify_data(file_path="spotify_churn_dataset.csv", debug=False)