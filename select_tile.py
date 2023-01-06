# read list from a piclke file
import pickle
tiles = pickle.load(open("grid_bara_bardadih.pkl", "rb"))

# read second argument from a csv file
import csv
with open('Bara_Bardadih_tiles_cover.csv', 'r') as f:
    reader = csv.reader(f)
    content = list(reader)

class_cover = [float(i[1]) for i in content[1:]]

threshold = 0.5
selected_tiles = []
for i in range(len(tiles)):
    if class_cover[i] > threshold:
        selected_tiles.append(tiles[i])
print(len(selected_tiles))
print(selected_tiles)
with open('selected_bara_bardadih.txt', 'w') as f:
    for item in selected_tiles:
        f.write("%s" % item)