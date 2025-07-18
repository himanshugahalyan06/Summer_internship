# to write data into cvs use writer.csv 

import csv 
header=['student Name','Roll No','Course']
data={1001:{'Name':'Himanshu','Course':'B.tech AI/Ml'},
    1002:{'Name':'Alisha','Course':'B.tech AI/ML'},
    1003:{'Name':'Muskan','Course':'B.tech AI/ML'},
    1004:{'Name':'Sahil','Course':'B.tech AI/ML'}
}

# with open("Files\\student.csv",mode="a",newline='') as file:
#     value=csv.writer(file)
#     value.writerow(header)

#     for Roll,info in data.items():
#         value.writerow([info['Name'], Roll, info['Course']])

# with open("Files\\student.csv",mode="w",newline='') as file:
#     values=csv.writer(file)
#     values.writerow(header)  # write header 
#     values.writerows(data) # write mutiple row 
    

# file.close()
# print("Data Added Successfully !!")

with open("Files\\student.csv",mode='r') as file:
    data=csv.reader(file)
    for row in data:
        print(row)


