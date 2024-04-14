# Data Cleaning using pandas

import pandas as pd

df = pd.read_excel(r'Customer Call List.xlsx')
# print(df)

# drop duplicates

df = df.drop_duplicates()
# print(df)

# dropping the whole column
df = df.drop(columns = "Not_Useful_Column")
# print(df)

# cleaning in last name column

# df["Last_Name"] = df["Last_Name"].str.lstrip('...')
# df["Last_Name"] = df["Last_Name"].str.lstrip('/')
df["Last_Name"] = df["Last_Name"].str.rstrip('_')

df["Last_Name"] = df["Last_Name"].str.lstrip('123._/') #it will remove all the characters at one code
# print(df)


# cleaning phone number column

# df['Phone_Number']=df['Phone_Number'].str.replace('[^a-zA-Z0-9]','')
df['Phone_Number']=df['Phone_Number'].apply(lambda x: str(x))
df['Phone_Number'].apply(lambda x: x[0:3]+ '-' + x[3:6]+ '-' + x[6:10])
# df['Phone_Number'] = df['Phone_Number'].replace(r'[\-|/]', '')

def clean_phone(phone):
    return ''.join(filter(str.isdigit, phone))

# Apply the clean_phone function to the Phone column
df['Phone_Number'] = df['Phone_Number'].apply(clean_phone)

df['Phone_Number'] = df['Phone_Number'].replace('nan--','')
df['Phone_Number'] = df['Phone_Number'].replace('Na--','')
# print(df)


# cleaning address column

# df[["Street Address", "State", "ZipCode"]] = df['Address'].str.split(',',2,expand=True)
# print(df)

df["Paying Customer"]=df["Paying Customer"].str.replace('Yes','Y')
df["Paying Customer"]=df["Paying Customer"].str.replace('No','N')
# print(df)

# cleaning do not contact column

df["Do_Not_Contact"]=df["Do_Not_Contact"].str.replace('Yes','Y')
df["Do_Not_Contact"]=df["Do_Not_Contact"].str.replace('No','N')
# print(df)

# df = df.replace('N/a','')
# df = df.replace('NaN','')
df = df.fillna('')
# print(df)

# if do not contact = yes
# then clean that data

for x in df.index:
    if df.loc[x,"Do_Not_Contact"] == 'Y':
        df.drop(x, inplace = True)
        
# print(df)

for x in df.index:
    if df.loc[x,"Phone_Number"] == '':
        df.drop(x, inplace = True)
        
# Another way to drop null values
df.dropna(subset=["Phone_Number"], inplace=True)


# reset the index

df = df.reset_index(drop=True)
print(df)