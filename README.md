![output](https://github.com/nicolasbon38/CuriousRacoon/blob/master/graphe_fruchterman_reingold.jpeg)


# README

I played with the Twitter API : I collected data about likes french députés give to each others. I created a network graph using gephi. The colors correspond to their political groups in the Assembly (that are differents from their actual politic party). I got information on this website : https://www.nosdeputes.fr/

I have collected only the 199 last likes of each account. I haven't found the account of 40 députés (on 585).


# API keys

The credentials for the API are in a file named auth.py, stocked at the root of the repository and with this syntax :

```{python}
CONSUMER_KEY = '<your key>'
CONSUMER_SECRET = '<your key>'
ACCESS_TOKEN = ''<your key>''
ACCESS_TOKEN_SECRET = '<your key>'
```

# Data folder
I did not git the data I collected to build the graph.


