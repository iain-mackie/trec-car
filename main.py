
from utils.dowload_utils import download_and_unpack_datasets, download_and_unpack_dataset
from utils.static import dataset_list, Wiki, WikiParagrahs
from data_exploration.printing_data import print_paragraphs, print_articles
from data_exploration.preprocessing import preprocess_paragraphs, preprocess_queries

from utils.static import Wiki, WikiParagrahs, Train, Benchmark
from rank_bm25 import BM25Okapi


if __name__ == "__main__":
    #download_and_unpack_dataset(D=Benchmark)

    #print_paragraphs(path=WikiParagrahs.file_path_list[0], limit=1)
    #print_articles(path=Wiki.file_path_list[4], limit=1)

    #queries = preprocess_queries(path=Wiki.file_path_list[0], limit=100000)
    #print(len(queries))

    paragraphs = preprocess_paragraphs(path=WikiParagrahs.file_path_list[0], limit=1)
    print(paragraphs)
    #print(len(paragraphs))

    # print('tokenized corpus')
    # tokenized_corpus = [doc.split(" ") for doc in paragraphs][0]
    # print(tokenized_corpus)
    #
    # print('tokenized corpus')
    # bm25 = BM25Okapi(tokenized_corpus)
    #
    # #tokenized_query = queries[0].split(" ")
    # tokenized_query = ['Bay']
    # print(tokenized_query)
    #
    # doc_scores = bm25.get_scores(tokenized_query)
    # print(doc_scores)


    # corpus = [
    #     "Hello there good man!",
    #     "It is quite windy in London",
    #     "How is the weather today?"
    # ]
    #
    # tokenized_corpus = [doc.split(" ") for doc in corpus]
    # print(tokenized_corpus)
    #
    # bm25 = BM25Okapi(tokenized_corpus)
    #
    # query = "windy London"
    # tokenized_query = query.split(" ")
    #
    # print(tokenized_query)
    #
    # doc_scores = bm25.get_scores(tokenized_query)
    #
    # print(doc_scores)
    #
    # print(bm25.get_top_n(tokenized_query, corpus, n=1))










