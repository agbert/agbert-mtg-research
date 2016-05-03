
mongoimport -h c157.candidate.13.mongolayer.com:10157 -d agbert-mtg-research -u agbert-mtg-research -p drag0n -c Cards --jsonArray --upsertFields name Cards.json
mongoimport -h c157.candidate.13.mongolayer.com:10157 -d agbert-mtg-research -u agbert-mtg-research -p drag0n -c Relatives --jsonArray --upsertFields source,name,word Relatives.json
mongoimport -h c157.candidate.13.mongolayer.com:10157 -d agbert-mtg-research -u agbert-mtg-research -p drag0n -c TheTokenProject --jsonArray --upsertFields id,name TheTokenProject.json
mongo c157.candidate.13.mongolayer.com:10157/agbert-mtg-research -u agbert-mtg-research -p drag0n TheTokenProject_Cards_MapReduce.js

MONGO_URL=mongodb://agbert-mtg-research:drag0n@candidate.13.mongolayer.com:10157,candidate.12.mongolayer.com:10157/agbert-mtg-research?replicaSet=set-532299780c25bddd8f0004e8 meteor
