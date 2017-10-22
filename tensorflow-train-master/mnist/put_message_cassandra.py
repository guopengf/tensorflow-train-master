from cassandra.cluster import Cluster

def put_message(image_name,pridect_number,image_time):
   cluster = Cluster(["127.0.0.1"])
   session = cluster.connect()
   session.execute("use space_image;")
   session.execute("insert into inputimages(image_name, pridect_number,image_time) values('%s',%d,'%s');"%(image_name, pridect_number, image_time))
   print("successful put message!")
