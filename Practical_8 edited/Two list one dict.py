L_Key=[1,2,3,4]
L_Values=["One","Two","Three","Four"]
print("Keys in list are:",*L_Key)
print("Values in list are:",*L_Values)
res={}
for key in L_Key:
    for value in L_Values:
        res[key]= value
        L_Values.remove(value) #To Place ever Key values
        break
print(res)