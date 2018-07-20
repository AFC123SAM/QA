import csv
import pandas as pd

with open('/Users/pattersons3/OneDrive - Vodafone Group/QA Apprenticeships/QA Lesson Week 2 - Introduction to Data Structure and Databases using Python and SQL/UFOGB_Details.csv',newline='') as f:
    r = csv.reader(f)
    data = [line for line in r]
with open('/Users/pattersons3/OneDrive - Vodafone Group/QA Apprenticeships/QA Lesson Week 2 - Introduction to Data Structure and Databases using Python and SQL/UFOGB_Details.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['ID','Header 2','Header 3','Header 4','Header 5','Header 6','Header 7'])
    w.writerows(data)

with open('/Users/pattersons3/OneDrive - Vodafone Group/QA Apprenticeships/QA Lesson Week 2 - Introduction to Data Structure and Databases using Python and SQL/UFOGB_Comments.csv',newline='') as f:
    r = csv.reader(f)
    data = [line for line in r]
with open('/Users/pattersons3/OneDrive - Vodafone Group/QA Apprenticeships/QA Lesson Week 2 - Introduction to Data Structure and Databases using Python and SQL/UFOGB_Comments.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['ID','Comments'])
    w.writerows(data)

df1 = pd.read_csv("/Users/pattersons3/OneDrive - Vodafone Group/QA Apprenticeships/QA Lesson Week 2 - Introduction to Data Structure and Databases using Python and SQL/UFOGB_Details.csv")
df2 = pd.read_csv("/Users/pattersons3/OneDrive - Vodafone Group/QA Apprenticeships/QA Lesson Week 2 - Introduction to Data Structure and Databases using Python and SQL/UFOGB_Comments.csv")
merged = df1.merge(df2, on="ID", how="outer")
merged.to_csv("/Users/pattersons3/OneDrive - Vodafone Group/QA Apprenticeships/QA Lesson Week 2 - Introduction to Data Structure and Databases using Python and SQL/UFOGB_Merged.csv", index=False)

