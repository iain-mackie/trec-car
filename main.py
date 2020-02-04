
from data_download.download import download_and_unpack_dataset, download_and_unpack_datasets
from data_download.static import WikiParagrahs, Wiki, dataset_list, Train, Benchmark

from index.static import write_q_path, write_d_path, write_q_norm_path, write_d_norm_path, write_rank_path
from index.build_q_and_d import build_q, build_d
from index.normalise_q_and_d import normalise_q, normalise_d
from index.ranking import retrieve_n_documents

from krovetzstemmer import Stemmer

from nltk.corpus import stopwords

import os
import re
import json

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
alpha = ['A', 'B', 'C', 'D', 'E', 'F']
valid_char = numbers + alpha
hex_utc8 = []
for c1 in valid_char:
    for c2 in valid_char:
        hex_utc8.append(c1 + c2)

def anserini_hex_check_topics():
    in_path = os.path.join(os.getcwd(), 'train.topics')
    out_path = os.path.join(os.getcwd(), 'train_out.topics')

    with open(in_path, "r") as f:
        lines = f.readlines()

    with open(out_path, "w") as f:
        for line in lines:
            if '%' in line:
                new_line = ''
                counter = 0
                for l in line:
                    if l == '%':
                        if line[counter + 1:counter + 3] in hex_utc8:
                            new_line += l
                        else:
                            print(line[counter:counter + 3])
                            new_line += '%25'
                    else:
                        new_line += l
                    counter += 1
                f.write(new_line)
            else:
                f.write(line)

def anserini_hex_check_qrels():
    in_path = os.path.join(os.getcwd(), 'train.qrels')
    out_path = os.path.join(os.getcwd(), 'train_out.qrels')

    with open(in_path, "r") as f:
        lines = f.readlines()

    with open(out_path, "w") as f:
        for line in lines:
            s = line.split()
            query = s[0]
            rel = ' ' + s[1] + ' ' + s[2] + ' ' + s[3]
            if '%' in query:
                new_query = ''
                counter = 0
                for q in query:
                    if q == '%':
                        if query[counter + 1:counter + 3] in hex_utc8:
                            new_query += q
                        else:
                            print(query[counter:counter + 3])
                            new_query += '%25'
                    else:
                        new_query += q
                    counter += 1
                new_line = new_query + rel
                f.write(new_line)
            else:
                new_line = query + rel
                f.write(new_line)


def galago_numbers():
    in_path = os.path.join(os.getcwd(), 'test.topics')
    out_path = os.path.join(os.getcwd(), 'test_galago.topics')
    with open(in_path, "r") as f:
        lines = f.readlines()

    with open(out_path, "w") as f:
        counter = 0
        for line in lines:
            new_line = str(counter) + "\t" + line
            print(new_line)
            print(new_line.decode("utf-8").encode("windows-1252").decode("utf-8"))
            #f.write(new_line)
            counter += 1


########################################################################
########################################################################
########################################################################

def format_query(q, preprocess=True):
    stopwords_list = stopwords.words('english')
    stemmer = Stemmer()

    q = q[7:]
    q = q.replace('%20', ' ')
    q = q.replace('/', ' ')
    q = q.replace('-', ' ')
    text = re.sub(r'[^A-Za-z0-9 ]+', '', q).lower()
    if preprocess:
        new_q = ''
        for w in text.split():
            word = str(w)
            if word not in stopwords_list:
                if len(new_q) == 0:
                    # new_q += stemmer.stem(word)
                    new_q += word
                else:
                    # new_q += " " + stemmer.stem(word)
                    new_q += " " + word

        return new_q
    else:
        return text


def get_queries(qrels_path):

    print('reading queries')
    with open(qrels_path, "r") as f:
        qrels = f.readlines()

    print('preprocessing queries')
    ids = []
    texts = []
    for qrel in qrels:
        q_id = qrel.split()[0]
        q_text = format_query(q_id)
        if q_id not in ids:
            ids.append(q_id)
            texts.append(q_text)
    return zip(ids, texts)


def write_json(d, path):
    with open(path, 'w') as f:
        json.dump(d, f, sort_keys=True, indent=4)


def get_galago_topics(qrels_path, file_name):

    query_data = get_queries(qrels_path=qrels_path)

    print('building galago json')

    bm25_queries = []
    bm25_rm3_queries = []
    ql_queries = []

    for q in query_data:

        if len(q[1]) > 0:

            bm25_text = "#combine("
            ql_text = "#combine("

            for w in q[1].split():
                bm25_text += " #bm25:K=0.9:b=0.4({w}) ".format(w=w)
                ql_text += " #dirichlet:mu=1000({w}) ".format(w=w)

            bm25_text += ")"
            ql_text += ")"
            bm25_rm3_text = "#rm( " + bm25_text + " )"

            bm25_queries.append({'number': str(q[0]),'text': bm25_text})
            bm25_rm3_queries.append({'number': str(q[0]), 'text': bm25_rm3_text})
            ql_queries.append({'number': str(q[0]), 'text': ql_text})

    ###### BM25 ######

    bm25_config = {
        "casefold": True,
        "verbose": True,
        "queries": bm25_queries
    }

    write_json(d=bm25_config, path=os.path.join(os.getcwd(), '{}_bm25.json'.format(file_name)))

    ###### BM25+RM3 #######

    bm25_rm3_config = {
        "casefold": True,
        "verbose": True,
        "relevanceModel": "org.lemurproject.galago.core.retrieval.prf.RelevanceModel3",
        "fbDocs": 10,
        "fbTerm": 10,
        "fbOrigWeight": 0.5,
        "rmstopwords": "rmstop",
        "rmStemmer": "org.lemurproject.galago.core.parse.stem.KrovetzStemmer",
        "queries": bm25_rm3_queries
    }

    write_json(d=bm25_rm3_config, path=os.path.join(os.getcwd(), '{}_bm25_rm3.json'.format(file_name)))

    ###### QL #######

    ql_config = {
        "casefold": True,
        "verbose": True,
        "queries": ql_queries
    }

    write_json(d=ql_config, path=os.path.join(os.getcwd(), '{}_ql.json'.format(file_name)))


if __name__ == "__main__":
    #galago_numbers()
    #anserini_hex_check_topics()
    #anserini_hex_check_qrels()
    qrels_path = os.path.join(os.getcwd(), 'test.pages.cbor-hierarchical.qrels')
    file_name = 'galago_test_tree_hierarchical_preprocessed_no_stemming'
    get_galago_topics(qrels_path=qrels_path, file_name=file_name)
    #print(format_query('sfn.4rg /dg dfAS%20DVB KDSAF u,s, . DV 4378Q47~}sa~}f)*£QUTRNL2351'))


















