# 3. A list contains sublist with Emp information as follows :
# Data = [[101,”Seema”,45000],[340,”Rajani”,13000],
# [210,”Tannu”,14000],[320,”Suresh”,35000]]

data = [
    [101,"Seema",45000],[340,"Rajani",13000],[210,"Tannu",14000],[320,"Suresh",35000]
    ]


for pass1 in range(1,len(data)):
    for i in range(len(data)-pass1):
        if(data[i][2]<data[i+1][2]):
            data[i],data[i+1]=data[i+1],data[i]
print(data)