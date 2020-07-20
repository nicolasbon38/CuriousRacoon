import tweepy
from os import listdir
import json
from time import sleep
from datetime import datetime
from auth import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET




auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)




#trouver une combine pour le rn, ils ont pas de listes twitter de députés les batards

deputes_json = []
parti_correspondant = []

dico = dict()


for parti in listdir("data"):
    for nom_json_deputes in listdir("data/" + parti):
        f = open("data/" + parti + "/" + nom_json_deputes, 'r')
        json_data = json.load(f)
        deputes_json.append(json_data)
        parti_correspondant.append(parti)
        f.close()
 

deputes_id = [d_json['id'] for d_json in deputes_json]
print("nombre de députés traités: ", len(deputes_id))

for i, d_json in enumerate(deputes_json):
    try:
        liked = api.favorites(id=d_json['id'], count=199)
        dico[d_json['id']] = [like for like in liked if like.user.id in deputes_id]

    except tweepy.error.RateLimitError:
        print("Je fais une petite pause de 15 minutes parce que j'ai dépassé 180 requêtes (je crois)")
        print(datetime.now())
        sleep(15 * 60 + 10)
    except tweepy.error.TweepError:
        print("Not authorized")
        print(str(d_json['name']) + "est un malin")
    print("{}/{}".format(i, len(deputes_id)))

######################################################################################
#oui j e sais c'est moche de définir la classe en plein milieu mais c'est la vie que j'ai choisi

class Edge:
    def __init__(self, id, source, target):
        self.id = str(id) + ".0"
        self.source = str(source) + ".0"
        self.target = str(target) + ".0"

    def writable(self):
        #sans les poids pour l'instant
        return """<edge id="{}" source="{}" target="{}"/>\n""".format(self.id, self.source, self.target)

########################################################################################################

les_edges= []
i = 0
for key in dico.keys():
    for like in dico[key]:
        try:
            les_edges.append(Edge(i, list(dico.keys()).index(key), list(dico.keys()).index(like.user.id)))
            i += 1
        except ValueError:
            print("là ça a fait de la merde, il trouve pas l'indice dans la liste, c'est chelou")


f = open("data_graph.gexf", 'w')
f.write("""<?xml version="1.0" encoding="UTF-8"?><gexf xmlns:viz="http:///www.gexf.net/1.1draft/viz" version="1.1" xmlns="http://www.gexf.net/1.1draft">
<graph defaultedgetype="undirected" idtype="string" type="static">\n""")

f.write("""<attributes class="node" mode="static">\n<attribute id="groupe" title="groupe" type="string"/></attributes>\n""")


f.write("""<nodes count="{}">""".format(len(deputes_id)))

for i, depute in enumerate(deputes_json):
    f.write("""<node id="{}.0" label="{}">\n""".format(i, depute['name']))
    f.write("""<attvalues><attvalue for="groupe" value="{}"></attvalue></attvalues>\n""".format(parti_correspondant[i]))
    f.write("</node>\n")

f.write("</nodes>\n")

f.write("""<edges count="{}">\n""".format(len(les_edges)))
for edge in les_edges:
    f.write(edge.writable())
f.write("</edges>\n</graph></gexf>")
f.close()



    