import string
import json
import io
import nltk
from spacy.en import English
nlp = English()


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.integer):
            return int(obj)
        elif isinstance(obj, numpy.floating):
            return float(obj)
        elif isinstance(obj, numpy.ndarray):
            return obj.tolist()
        else:
            return super(MyEncoder, self).default(obj)



with open('AllCards.json') as infile:
    data = json.load(infile);
    
translate_table = dict((ord(char), None) for char in string.punctuation)   
outArray = [];
outRelative = [];

with open('Cards.json','w') as Cardoutfile:
    with open('Relatives.json','w') as Relativeoutfile:
        for card in data:
            lCard = data[card];
            name = lCard["name"];
            if "text" in lCard:
                text = lCard["text"];
                texts = nltk.sent_tokenize(text);
                text_nltk_sents = [];
                text_spacy_setns = [];
        
                #nltk
                for txt in texts:
                    if txt:
                        sent = {};
                        txtn = txt.translate(translate_table);
                        #text = text.translate(None, string.punctuation);
                        tokenized = nltk.word_tokenize(txtn);
                        tokenized = nltk.pos_tag(tokenized);
                        word_psos = [];
                        for token in tokenized:
                            relate = {};
                            relate["name"] = name;
                            relate["source"] = "nltk";
                            relate["word"] = token[0];
                            relate["pos"] = token[1];
                            outRelative.append(relate);
                            word_pos = {};
                            word_pos["word"] = token[0];
                            word_pos["pos"] = token[1];
                            word_psos.append(word_pos);
                    
                        sent["sent"] = txt;
                        sent["word_pos"] = word_psos;
                        text_nltk_sents.append(sent);
                
                #spacy
                text_spacy_sents = [];
                doc = nlp(text);
                
                for sent in doc.sents:
                    spacy_sent = {};
                    spacy_sent["sent"]= sent.text_with_ws;
                    orths_psos = [];
                    sentindex = 0;
                    for token in sent:
                        if token.is_alpha:
                            #print(token);
                            orth = token.lower;
                            tag = token.tag;
                            pos = token.pos;
                            lemma = token.lemma;
                            orth_ = token.lower_;
                            tag_ = token.tag_;
                            pos_ = token.pos_;
                            lemma_ = token.lemma_;
                            relate = {}
                            relate["name"] = name;
                            relate["source"] = "spacy";
                            relate["sentIndex"] = sentindex;
                            relate["orth"] = orth;
                            relate["orth_"] = orth_;
                            relate["pos"] = pos;
                            relate["pos_"] = pos_;
                            relate["tag"] = tag;
                            relate["tag_"] = tag_;
                            relate["lemma"] = lemma;
                            relate["lemma_"] = lemma_;
                            orth_pos = {};
                            orth_pos["orth"] = orth;
                            orth_pos["orth_"] = orth_;
                            orth_pos["pos"] = pos;
                            orth_pos["pos_"] = pos_;
                            orth_pos["tag"] = tag;
                            orth_pos["tag_"] = tag_;
                            orth_pos["lemma"] = lemma;
                            orth_pos["lemma_"] = lemma_;

                            lex = doc.vocab[orth_];
                            #print(lex.vector);
                            #input("Press Enter to continue...")
                            
                            prob = lex.prob;
                            cluster = lex.cluster;
                            vector = 0;
                            if lex.has_vector:
                                for v in lex.vector:
                                    vector += v;
                            orth_pos["lexprob"] = prob;
                            orth_pos["lexcluster"] = cluster;
                            if vector and vector is not None:
                                orth_pos["lexvector"] = vector;
                            relate["lexprob"] = prob;
                            relate["lexcluster"] = cluster;
                            if vector and vector is not None:
                                relate["lexvector"] = vector;

                            outRelative.append(relate);
                            orths_psos.append(orth_pos);
                            
                        sentindex += 1;
                
                    #spacy_sent["sent"] = sent;
                    if len(orths_psos)>0:
                        spacy_sent["orths_psos"] = orths_psos;
                    text_spacy_sents.append(spacy_sent);
    
                text_spacy_ents = [];
                for ent in doc.ents:
                    spacy_ent = {};
                    spacy_ent["ent"] = ent.text_with_ws;
                    spacy_ent_toks = []
                    for token in ent:
                        if token.is_alpha:
                            orth = token.orth;
                            orth_ = token.orth_;
                            if hasattr(token,'label'):
                                label = token.label
                            else:
                                label = None;
                            if hasattr(token,'label_'):
                                label_ = token.label_
                            else:
                                label_ = None;
                            if label is not None or label_ is not None:
                                spacy_ent_tok = {};
                                spacy_ent_tok["orth"] = orth;
                                spacy_ent_tok["orth_"] = orth_;
                                if label is not None:
                                    spacy_ent_tok["label"] = label;
                                if label_ is not None:
                                    spacy_ent_tok["label_"] = label_;
                                spacy_ent_toks.append(spacy_ent_tok);
            
                    #spacy_ent["ent"] = ent;
                    if len(spacy_ent_toks)>0:
                        spacy_ent["ents"] = spacy_ent_toks;
                        text_spacy_ents.append(spacy_ent);
                                
                lCard["text_nltk"] = text_nltk_sents;
                if len(text_spacy_sents)>0 or len(text_spacy_ents)>0:
                    text_spacy = {};
                    if len(text_spacy_sents)>0:
                        text_spacy["sents"] = text_spacy_sents;
                    if len(text_spacy_ents)>0:
                        text_spacy["ents"] = text_spacy_ents;
                    lCard["text_spacy"] = text_spacy;
         
            #json.dump(lCard,Cardoutfile,sort_keys=True,indent=4, separators=(',', ': '));
            outArray.append(lCard);
        
        json.dump(outRelative,Relativeoutfile,sort_keys=True,indent=4, separators=(',', ': '));
        json.dump(outArray,Cardoutfile,sort_keys=True,indent=4, separators=(',', ': '));
