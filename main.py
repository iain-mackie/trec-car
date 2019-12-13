from index.preprocessing import extract_paragraphs, extract_queries

from utils.static import WikiParagrahs, Wiki

if __name__ == "__main__":

    #queries = extract_queries(path=Wiki.file_path_list[0], page_limit=3)

    paragraphs = extract_paragraphs(path=WikiParagrahs.file_path_list[0], paragraph_limit=3)












