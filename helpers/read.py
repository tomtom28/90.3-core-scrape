import csv

# Read the CSV file of music and return all the entries
def read_csv_file():
    # List of dictionaries to store artists and songs
    list_of_music = []

    # Open CSV File and Read in Existing entries
    with open('artist_song.csv',  newline='\n') as csv_file:
        file_reader = csv.reader(csv_file)
        for row in file_reader:
            current_entry = {"artist": row[0], "song": row[1]}
            list_of_music.append(current_entry)

    # Return music entries read from file
    return list_of_music
