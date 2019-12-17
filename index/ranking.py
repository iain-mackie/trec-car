
from index.static import write_d_norm_path, write_q_norm_path

from rank_bm25 import BM25Okapi


def get_norm_d(path=write_d_norm_path):

    corpus = []
    corpus_token = []
    with open(path, 'r') as f:
        for l in f:
            doc = str(l).split('\t')[1].replace('\n', '')
            corpus.append(doc)
            corpus_token.append(doc.split(" "))

    return corpus, corpus_token


def retrieve_n_documents(n=3):
    corpus, corpus_token = get_norm_d()
    bm25 = BM25Okapi(corpus)

    with open(write_q_norm_path) as f:

        for q in f:
            query = str(q).split('\t')[1].replace('\n', '')
            d = bm25.get_top_n(query=query, documents=corpus, n=n)
            print('--- query: {} ---'.format(query))
            print(doc_scores)

    return





