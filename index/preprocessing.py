
from utils.static import WikiParagrahs, Wiki
from trec_car.read_data import iter_paragraphs, ParaText, ParaLink, iter_pages

def extract_queries(path=Wiki.file_path_list[0], page_limit=1):

    queries = []

    print('*** reading {} articles from file: {} ***'.format(page_limit, path))
    with open(path, 'rb') as f:

        counter = 1

        for p in iter_pages(f):

            page_name = p.page_name

            if len(p.outline()) > 0:
                queries += [[page_name + ' ' + " ".join([str(section.heading) for section in section_path])] for section_path in p.flat_headings_list()][0]

            if counter >= page_limit:
                break

            counter += 1

    return queries


def extract_paragraphs(path=WikiParagrahs.file_path_list[0], paragraph_limit=1):

    paragraphs = []

    print('*** reading {} paragraph from file: {} ***'.format(paragraph_limit, path))
    with open(path, 'rb') as f:

        counter = 1

        for p in iter_paragraphs(f):

            paragraphs.append(p.get_text())

            if counter >= paragraph_limit:
                break

            counter += 1

    return paragraphs





