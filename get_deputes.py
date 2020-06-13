#!/usr/bin/env python3

from auth import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
import tweepy
import json

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


deputes_eds = api.list_members(list_id=1262716902155210754) #les traitres (villani)
deputes_gdr = api.list_members(list_id=880045706370842624) #les communistes
#deputes_lrem = api.list_members(list_id=876796317900648448)
#deputes_lr = api.list_members(list_id=877812130388496384)
#deputes_lfi = api.list_members(list_id=1071428866428858368)
#deputes_ps = api.list_members(list_id=877869806606733314)
#deputes_modem = api.list_members(list_id=889229408577482756)
#deputes_udi = api.list_members(list_id=1074973716193398784)
#deputes_lt = api.list_members(list_id=1229464536912142344)

#il manque AE

# J'AI DU LE FAIRE A LA MAIN LES BATARDS
#deputes_rn = [api.get_user(screen_name=x) for x in ['louis_aliot', 'BrunoBilde', 'sebchenu', 'MLP_officiel', 'NMeizonnet', 'menard2017', 'ludovicpajot']]


#après on écrit dans des json

i=0
for depute in tweepy.Cursor(deputes_communistes).items():
    with open("data/gdr/{}.json".format(depute.name), 'w') as f:
        json.dump(depute._json, f)
    i += 1
print(i)
    
