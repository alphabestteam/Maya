import pymongo

def main():
    connection_str = "mongodb://localhost:27017/"
    client = pymongo.MongoClient(connection_str)
    avivs_db = client["Aviv's_people"]
    army_col = avivs_db["army"]
    army_data = [{"name":"Aviv", "age": 20, "role": "Backend"}, 
                    {"name":"Lihi", "age": 21, "role": "QA"},
                    {"name":"Gabi", "age": 22, "role": "DevOps"},
                    {"name":"Ori", "age": 23, "role": "Front-end"},
                    {"name":"Ido", "age": 22, "role": "developer"},
                    {"name":"Yarden", "age": 24, "role": "DevOps"}]
    friends_col = avivs_db["friends"]
    person1 = {"name":"Amit", "age": 20, "role": "waiter"} 
    person2 = {"name":"Yonatan", "age": 24, "role": "doctor"}
    person3 = {"name":"Noa", "age": 22, "role": "student"}
    person4 = {"name":"Michal", "age": 21, "role": "baker"}
    family_col = avivs_db["family"]
    family_data = [{"_id": 14, "name":"mother", "age": 45, "role": "teacher"}, 
                    {"_id": 15, "name":"father", "age": 46, "role": "engineer"},
                    {"_id": 16, "name":"brother", "age": 12, "role": "school"},
                    {"_id": 17, "name":"sister", "age": 24, "role": "student"}]
    army_col.insert_many(army_data)
    friends_col.insert_one(person1)
    friends_col.insert_one(person2)
    friends_col.insert_one(person3)
    friends_col.insert_one(person4)
    family_col.insert_many(family_data)
    army_docs = army_col.find({})
    friends_docs = friends_col.find({})
    family_docs = family_col.find({})
    for document in army_docs:
        print(document)
    for document in friends_docs:
        print(document)
    for document in family_docs:
        print(document)
    army_col.delete_one({"name" : "Lihi"})
    pdf3
    find_devops= army_col.find_one({"role" : "DevOps", "age": {"$lt": 23}})
    devops_name = find_devops["name"]
    if "role" in find_devops:
        print(f"The name is: {devops_name}")
    else:
        print("name is not found")
    for document in army_docs:
        if document["age"] == find_devops["age"] and document["name"] != devops_name:
            update_doc = {"$set": {"role": document["role"]}}
            army_col.update_one(find_devops, update_doc)
            updated_person = army_col.find_one({"name": devops_name, "role": document["role"]})
    print(updated_person)

    find_older = army_col.find({"age": {"$gt": 23}})
    for document in find_older:
        friends_col.insert_one(document)
    army_col.delete_many({"age": {"$gt": 23}})
    new_army_data = army_col.find({})
    new_friends_data = friends_col.find({})
    sorted_army_data = sorted(new_army_data, key=lambda x: x["age"])
    for document in sorted_army_data:
        print(document)
    for document in new_friends_data:
        print(document)

if __name__ == "__main__":
    main()