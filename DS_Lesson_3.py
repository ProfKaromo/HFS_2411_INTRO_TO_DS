# #Lists , Tuples and Dictionary
# names = ["Jane","John","Mike"]
# print(names)
# names.insert(2,"Enice")
# print(names)
# names.append("John")
# print(names)
# names.append("kk")
# print(names)
# print(names)

counties = ["EMBU","THARAKA NITHI","Nyeri","NAKURU","TRANS NZOIA","BOMET","ELGEYO MARAKWET"]
counties_2 = []
counties_1 = []
c_one = c_two = 0
for county in range(0,len(counties)):
    if " " in counties[county]:
        counties_2.append(counties[county])
        c_one +=1
    else:
        counties_1.append(counties[county])
        c_two +=1
print(counties_2)
print(counties_1)
print("There are ",c_one," counties with one name and ",c_two," counties with two names")

#Tuple
mytuple = (counties_1,counties_2)
print(mytuple)

#dictionary
mydict = {
    "Name" : "Jane",
    "Age" : 23,
    "County" : "Embu"
}
print(mydict)

print(mydict.get("Name"))
print(mydict.get("Age"))
print(mydict.get("County"))

mydict.update({"County":"Nyeri"})
print(mydict)

