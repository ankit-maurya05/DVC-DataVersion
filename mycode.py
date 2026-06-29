import pandas as pd
import os

data={'Name':['Ankit',"Shikha","Isha"],
      "Age":[25,22,23],
      "City":["Varanasi","Azamgarh","Allahabad"]}

df=pd.DataFrame(data)

data_dir='data'

os.makedirs(data_dir,exist_ok=True)

file_path=os.path.join(data_dir,"Sample_data.csv")

df.to_csv(file_path,index=False)

print(f'CSV file save to {file_path}')
print(df)