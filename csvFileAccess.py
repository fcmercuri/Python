import csv, os

with open ("rankings.csv") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        dir = os.listdir()
        keyword = row["Keyword"].title()
        print(keyword)
        if keyword not in dir:
            os.mkdir(keyword)
        visibility = row["Visibility"]
        print(row["Visibility"])
        path = os.path.join(keyword, visibility)
        f = open (path, "w")
        f.close()


