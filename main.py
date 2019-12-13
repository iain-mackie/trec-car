from index.preprocessing import extract_paragraphs, extract_queries
from index.ranking import retrieve_n_documents

from utils.static import WikiParagrahs, Wiki

if __name__ == "__main__":

    queries = extract_queries(path=Wiki.file_path_list[0], page_limit=1000000)

    paragraphs = extract_paragraphs(path=WikiParagrahs.file_path_list[0], paragraph_limit=1000000)

    retrieve_n_documents(queries=queries, corpus=paragraphs, n=1)














