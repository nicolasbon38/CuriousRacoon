#!/usr/bin/env python3

from auth import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
import tweepy
import json
from requests import get

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def get_deputes_from_groupe(groupe, url):
    r = get(url)
    data_json = r.json()
    les_twitters = []
    for depute in data_json['deputes']:
        if depute['depute']['twitter']:
            les_twitters.append((depute['depute']['nom'], depute['depute']['twitter']))
        else:
            print(depute['depute']['nom'])
    for nom, twitter in les_twitters:
        f = open("data/{}/{}.json".format(groupe, nom),'w')
        json.dump(api.get_user(screen_name=twitter)._json, f)
        f.close()


# LES_GROUPES = ["ecologie-democratie-solidarite", "agir-ensemble", "gauche-democrate-et-republicaine", "la-france-insoumise", "la-republique-en-marche", "les-republicains", "libertes-et-territoires", "socialistes-et-apparentés", "udi-et-independants", "mouvement-democrate-et-apparentes"]


# for groupe in LES_GROUPES:
#     get_deputes_from_groupe(groupe, "https://www.nosdeputes.fr/organisme/{}/json".format(groupe))


# # J'AI DU LE FAIRE A LA MAIN LES BATARDS
# deputes_rn = [api.get_user(screen_name=x) for x in ['louis_aliot', 'BrunoBilde', 'sebchenu', 'MLP_officiel', 'NMeizonnet', 'ludovicpajot']]


# #après on écrit dans des json

# for depute in deputes_rn:
#     with open("data/rassemblement-national/{}.json".format(depute.name), 'w') as f:
#         json.dump(depute._json, f)
    





###deuxième passage pour récupérer ceux qui manquent


#on récupère les datas de nosdeputes.r
with open("nosdeputes.fr_deputes_2020-07-16.json", 'r') as f:
    data_nos_deputes = json.load(f)

dico_des_sigles={
    "AE":"agir-ensemble",
    "EDS":"ecologie-democratie-solidarite",
    "GDR":"gauche-democrate-et-republicaine",
    "LFI":"la-france-insoumise",
    "LREM":"la-republique-en-marche",
    "LR":"les-republicains",
    "LT":"libertes-et-territoires",
    "MODEM":"mouvement-democrate-et-apparentes",
    "SOC":"socialistes-et-apparentes",
    "UDI":"udi-et-independants"
}


def find_groupe(name):
    for depute in data_nos_deputes["deputes"]:
        if depute["depute"]["nom"].lower() == name.lower():
            return depute["depute"]["groupe_sigle"]


deputes_eds =  1262716902155210754 #les traitres (villani)
deputes_gdr =  880045706370842624 #les communistes
deputes_lrem =  876796317900648448
deputes_lr =  877812130388496384
deputes_lfi =  1071428866428858368
deputes_ps =  877869806606733314
deputes_modem =  889229408577482756
deputes_udi =  1074973716193398784
deputes_lt =  1229464536912142344

groupes = [ ('socialistes-et-apparentes', deputes_ps), ('mouvement-democrate-et-apparentes', deputes_modem), ('udi-et-independants', deputes_udi), ('libertes-et-territoires', deputes_lt)]
#('ecologie-democratie-solidarite', deputes_eds), ('gauche-democrate-et-republicaine', deputes_gdr), ('la-republique-en-marche', deputes_lrem), ('les-republicains', deputes_lr), ('la-france-insoumise', deputes_lfi),


for nom_groupe, id_liste in groupes:
    for depute in tweepy.Cursor(api.list_members, list_id=id_liste).items():
        try:
            groupe = find_groupe(depute.name)
            with open("data/{}/{}.json".format(dico_des_sigles[str(groupe)], depute.name), 'w') as f:
                json.dump(depute._json, f)
        except KeyError:
            print(depute.name)




