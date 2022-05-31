import csv


with open("test.csv", "r") as f:
    csv_reader = csv.DictReader(f)
    name_records = list(csv_reader)

##print(name_records[3].keys())



def show(test):
    temp = list(name_records[test].values())
    temp2 = list(name_records[test].keys())
    for i in range(0,7,1):
        print(temp2[i],": ", end = "")
        print(temp[i])
while True:
        test = int(input("what number? "))
        show(test)
