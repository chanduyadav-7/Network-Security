from pymongo import MongoClient
uri = "mongodb+srv://chandugodugu2006_db_user:<passwordhere>@cluster0.t4qyfpq.mongodb.net/"
client = MongoClient(uri)
try:
    client.admin.command("ping")
    print("Connected successfully")
    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)