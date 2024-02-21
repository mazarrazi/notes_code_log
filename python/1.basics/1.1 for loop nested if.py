squad=("saka",'gabi','esr','gabij','gabig',"ben")  
find="esr"  
founded=None  
a=len(squad)  
print (a)  
  
for index in range(len(squad)):  
    if squad[index]==find:  
        founded=index  
  
print(f"position\t{founded}")
