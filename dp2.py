# !/usr/bin/python

from pymongo import MongoClient, errors
from bson.json_util import dumps
import os
import json

MONGOPASS = os.getenv('MONGOPASS')
uri = "mongodb+srv://cluster0.pnxzwgz.mongodb.net/"
client = MongoClient(uri, username='nmagee', password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)
#specify a database
db = client.rde6mn
# specify a collection
collection = db.dp2
directory = "/workspace/ds2002-dp2/data"



#file reading

success_imports = 0
corrupted_imports = 0
no_imports = 0

for filename in os.listdir(directory):
    with open(os.path.join(directory, filename)) as f:
                # assuming you have defined a connection to your db and collection already:

                # Loading or Opening the json file
        try:
            try:
                file_data = json.load(f)
            except Exception as e:
                print(e, "file couldn't be loaded", filename)
                                
            # Inserting the loaded data in the collection
            # if JSON contains data more than one entry
            # insert_many is used else insert_one is used
            if isinstance(file_data, list):
                for list_file in file_data:
                    try:            
                        results = collection.insert_one(list_file)
                    except Exception as e:
                        print(e, "when importing into Mongo", filename)
                        corrupted_imports +=1
                        #continue
            else:
                try:
                    collection.insert_one(file_data)
                    success_imports += 1
                except Exception as e:
                    print(e, "when importing into Mongo", f)
                    corrupted_imports +=1
                    #continue
                #print(e)
                # assuming you have defined a connection to your db and collection already:

                # Loading or Opening the json file
                #with open('data.json') as file:
                #    file_data = json.load(file)
                
                # Inserting the loaded data in the collection
                # if JSON contains data more than one entry
                # insert_many is used else insert_one is used
                #if isinstance(file_data, list):
                #    collection.insert_many(file_data)  
                #else:
                #    collection.insert_one(file_data)

        except Exception as e:
            print(e)
               
           

print("Corrupt Number =" + str(corrupted_imports))
print("No Import =" + str(no_imports))
print("Successful Import =" + str(success_imports))

