#READING_A_CSV_FILE
import csv
with open('movies.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#WRITING_A_CSV_FILE
import csv
with open('movies.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Movie", "EXTRACTION"])
    writer.writerow([1, "Lord of the Rings", "avengers"])
    writer.writerow([2, "Harry Potter", "Harry Potter"])