
from rank_bm25 import BM25Okapi
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import punctuation

def format_strings(s):

    words = word_tokenize(s.lower())
    stop_words = set(stopwords.words('english'))
    non_valid_symbols = [p for p in punctuation]

    format_words = []
    for w in words:
        if (w not in stop_words) and (w not in non_valid_symbols):
            format_words += [w]

    return format_words


def retrieve_n_documents(queries, corpus, n=1):

    tokenized_corpus = [format_strings(s) for s in corpus]
    bm25 = BM25Okapi(tokenized_corpus)

    documents = []
    for q in queries:
        tokenized_query = format_strings(q)
        d = bm25.get_top_n(query=tokenized_query, documents=corpus, n=n)
        documents.append(d)

    return documents



