
from index.static import write_d_norm_path, write_q_norm_path, write_rank_path

from rank_bm25 import BM25Okapi


def get_norm_d(path=write_d_norm_path):

    corpus = []
    corpus_token = []
    d_to_id_map = {}
    with open(path, 'r') as f:

        for l in f:

            l_split = str(l).split('\t')
            id = l_split[0]
            d = l_split[1].replace('\n', '')

            corpus.append(d)
            corpus_token.append(d.split(" "))
            d_to_id_map[d] = id

    return corpus, corpus_token, d_to_id_map


def retrieve_n_documents(read_path=write_q_norm_path, write_path=write_rank_path, n=1):

    print('*** retrieving {} relevant document for each query ***'.format(n))

    print('building normalised corpus data')
    corpus, corpus_token, d_to_id_map = get_norm_d()
    bm25 = BM25Okapi(corpus)

    len_d = len(corpus)
    len_q = len([l for l in open(read_path, 'r')])
    print('document count = {}'.format(len_d))
    print('query count = {}'.format(len_q))

    with open(read_path, 'r') as f_read:
        with open(write_path, 'w') as f_write:

            counter = 1

            for l in f_read:

                if counter % 100 == 0:
                    print('{}/{} queries complete'.format(counter, len_q))


                l_split = str(l).split('\t')
                page_id = l_split[0]
                query = l_split[1].replace('\n', '')

                d_list = bm25.get_top_n(query=query, documents=corpus, n=n)

                for d in d_list:

                    id = d_to_id_map[d]
                    f_write.write(page_id + '\t' + query + '\t' + id + '\t' + d + '\n')

                counter += 1





