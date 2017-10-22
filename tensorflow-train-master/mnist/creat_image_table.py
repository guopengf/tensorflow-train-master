from cassandra.cluster import Cluster

cluster = Cluster(["127.0.0.1"])
session = cluster.connect()
keyspacename = "space_image"
#session.execute("create keyspace %s with replication = {'class': 'SimpleStrategy', 'replication_factor':3 };" % keyspacename)
# use keyspace; create a sample table
session.set_keyspace(keyspacename)
session.execute("use space_image;")
session.execute("create table inputimages(image_name text , pridect_number int, image_time text PRIMARY KEY);")

print("create success!")

