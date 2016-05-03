
mongoimport -h c157.candidate.13.mongolayer.com:10157 -d agbert-mtg-research -u agbert-mtg-research -p ********** -c Cards --jsonArray --upsertFields name Cards.json
mongoimport -h c157.candidate.13.mongolayer.com:10157 -d agbert-mtg-research -u agbert-mtg-research -p ********** -c Relatives --jsonArray --upsertFields source,name,word Relatives.json
mongoimport -h c157.candidate.13.mongolayer.com:10157 -d agbert-mtg-research -u agbert-mtg-research -p ********** -c TheTokenProject --jsonArray --upsertFields id,name TheTokenProject.json
mongo c157.candidate.13.mongolayer.com:10157/agbert-mtg-research -u agbert-mtg-research -p ********** TheTokenProject_Cards_MapReduce.js

MONGO_URL=mongodb://agbert-mtg-research:**********@candidate.13.mongolayer.com:10157,candidate.12.mongolayer.com:10157/agbert-mtg-research?replicaSet=set-532299780c25bddd8f0004e8 meteor
