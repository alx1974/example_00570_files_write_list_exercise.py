# erstelle eine liste mit folgenden elementen: "protons", "neutronen", "elektronen"


# oeffne die datei particles.txt und speichere die element ab mit einem komma als ternnzeichen
import csv

list = ["protons", "neutronen", "elektronen"]
print(list)
myfilename = "particles.txt"
with open(myfilename, "w") as File:
    try:
        File.write(str(list))
    except:
        print("File could not be written !!")

myfilename = "particles.csv"
with open(myfilename, "w", newline="") as csvfile:
    filewriter = csv.writer(csvfile, delimiter=",")
    try:
        filewriter.writerow(list)
    except:
        print("File could not be written !!")

