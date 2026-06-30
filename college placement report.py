import pandas as pd
#Read file
df=pd.read_excel("C:\\Users\\nandu\\Downloads\\college placement report.xlsx")
#Enter  college details
college_code=input("Enter College Code:")
college_name=input("Enter College Name:")
year=int(input(    "Enter year:"))
#Search College Details matched or not
result=df[
    (df["College Code"].astype(str).str.strip().str.lower()==college_code.strip().lower())&
    (df["College Name"].astype(str).str.strip().str.lower()==college_name.strip().lower())&
    (df["Year"]==year)
]
if result.empty:
    print("TRY AGAIN")
else:
    print("CONGRATULATIONS")
    print("Here You Can View Your")
    print("*"*20)
    print("====COLLEGE PLACEMENT DETAILS====")
    print("*"*20)
    print("College Name:",college_name)
    print("College Code:",college_code)
    print("Academic Year:",year)
    print(result.to_string(index=False))
    print("*"*20)
    print("THANK YOU")
    print("*"*20)