import pandas as pd
import csv

dataset_1=[]
dataset_2=[]
with open("dwarfStars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        dataset_1.append(row)

with open("stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        dataset_2.append(row)

headers = dataset_1[0]
headers2 = dataset_2[0]
data1 = dataset_1[1:]
data2 = dataset_2[1:]
for row in data1:
    try:
        row[3] = float(row[3])
        row[4]=float(row[4])
        row[4]*=0.102763
        row[3]*=0.000954588
    except:
        pass

rows = []    
with open("mergedStars.csv",mode = "w") as f:
    writer = csv.writer(f)
    writer.writerow(headers2 + headers)
    writer.writerows(data2 + data1)
with open("mergedStars.csv", "r") as f:
  csvreader = csv.reader(f)
  for row in csvreader: 
    rows.append(row)
print(rows[0])
df = pd.read_csv("mergedStars.csv")
df.drop(['Unnamed: 0','Unnamed: 6', 'Star_name.1', 'Distance.1', 'Mass.1', 'Radius.1','Luminosity'],axis=1,inplace=True)
print(df)
dfFinal=df.dropna()
dfFinal.to_csv("mergedStars.csv")
