import csv
import pandas as pd

with open(' ## ENTER UFOGB_DETAILS FILE PATH ## .csv',newline='') as f:
    r = csv.reader(f)
    data = [line for line in r]
with open(' ## ENTER UFOGB_DETAILS FILE PATH ## .csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['ID','Header 2','Header 3','Header 4','Header 5','Header 6','Header 7'])
    w.writerows(data)

with open(' ## ENTER UFOGB_COMMENTS FILE PATH ## .csv',newline='') as f:
    r = csv.reader(f)
    data = [line for line in r]
with open(' ## ENTER UFOGB_COMMENTS FILE PATH ## .csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['ID','Comments'])
    w.writerows(data)

df1 = pd.read_csv(" ## ENTER UFOGB_DETAILS FILE PATH ## .csv")
df2 = pd.read_csv(" ## ENTER UFOGB_COMMENTS FILE PATH ## .csv")
merged = df1.merge(df2, on="ID", how="outer")
merged.to_csv(" ## CREATE A BLANK CSV FILE AND PUT ITS LOCATION HERE ## .csv", index=False)

