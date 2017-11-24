import csv

# Write to the CSV file of music
def write_csv_file(list_of_new_music):

    # Parse Entries for proper formatting
    list_of_csv_entries = []
    for row in list_of_new_music:
        list_of_csv_entries.append([row["artist"],row["song"]])

    # Open CSV File and Write in any new entries
    with open('logs/artist_song.csv', 'a') as csv_file:
        file_writer = csv.writer(csv_file)
        file_writer.writerows(list_of_csv_entries)
