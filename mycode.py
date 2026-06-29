import pandas as pd
import os

data={'Name':['Ankit',"Shikha","Isha"],
      "Age":[25,22,23],
      "City":["Varanasi","Azamgarh","Allahabad"]}



df=pd.DataFrame(data)

new_row={"Name":"abc","Age":123,"City":"c1"}
df.loc[len(df.index)]=new_row
print(f"After new_row: {len(df.index)} rows")
print(df)

new_row2={"Name":"abcd","Age":1234,"City":"c2"}
df.loc[len(df.index)]=new_row2
print(f"After new_row2: {len(df.index)} rows")
print(df)

data_dir='data'

os.makedirs(data_dir,exist_ok=True)

file_path=os.path.join(data_dir,"Sample_data.csv")

df.to_csv(file_path,index=False)

print(f'CSV file save to {file_path}')