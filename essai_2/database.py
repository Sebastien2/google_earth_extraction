from pymongo import MongoClient
import pandas
import csv

client = MongoClient('mongodb://localhost:27017')
db = client.map
satellite = db.satellite


def clear_database(latitude, longitude):
    #et on vide la bdd
    x = satellite.delete_many({})
    print("{} deleted in the db in position {}, {}".format(x.deleted_count, latitude, longitude))
    return


clear_database(0, 0)


def save_in_database(alt, color, latitude, longitude):
    post_data = {
        'altitude': alt,
        'latitude': latitude,
        'longitude': longitude,
        'color_R': color[0],
        'color_G': color[1],
        'color_B': color[2]
    }
    result = satellite.insert_one(post_data)
    #print('One post: {0}, {1}'.format(result.inserted_id, result))

    return



def send_into_csv_file(latitude, longitude, precision):
    #on enregistre toutes les données de cette image dans un fichier csv
    cursor=satellite.find()
    mongo_docs = list(cursor)
    docs = pandas.DataFrame(columns=[])
    for num, doc in enumerate( mongo_docs ):
        doc["_id"] = str(doc["_id"])

        # get document _id from dict
        doc_id = doc["_id"]
        series_obj = pandas.Series( doc, name=doc_id )

        # append the MongoDB Series obj to the DataFrame obj
        docs = docs.append( series_obj )
    json_export = docs.to_json() # return JSON data
    csv_export = docs.to_csv(sep=",")

    with open("data/"+str(latitude)+"_"+str(longitude)+"_"+str(precision)+".csv", "w") as f:
        f.write(csv_export)
        f.close()

    return
