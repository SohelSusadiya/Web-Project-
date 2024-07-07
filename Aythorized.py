import pymongo
def state(name,document):
    name=str("['"+name+"']")
    document=str(list(onedata.values()))
    if(name==document):
       return False
# This is DataBase Connection Code
print("Hello World")
if __name__=="__main__":
    compare=True
    client= pymongo.MongoClient("mongodb://localhost:27017")
    db=client['sohel']
    Collection=db ["collections"]
    dic={"name":"A","age":1}
    chk=Collection.insert_one(dic)
    Name=input("Enter Your Name :: ")
    Age=input("Enter Your Age :: ")
    # New data and Old data comparsion
    for onedata in Collection.find({"name":Name},{"name":1,"_id":0}):
        compare=state(Name,onedata)
    if(compare):
        dic={"name":Name,"age":Age}
        chk=Collection.insert_one(dic)
        print("Successfuly")
    else:
         print("User Alredy Exist")
    print("Code Run --> Successfuly <-- ")