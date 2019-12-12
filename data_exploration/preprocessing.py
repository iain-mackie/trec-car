
from utils.static import WikiParagrahs, Wiki
from trec_car.read_data import iter_paragraphs, ParaText, ParaLink, iter_pages


def preprocess_queries(path=Wiki.file_path_list[0], limit=1):

    print('*** reading {} articles from file: {} ***'.format(limit, path))
    with open(path, 'rb') as f:

        counter = 1

        for p in iter_pages(f):

            print('----------------------- Queries   -----------------------')
            # get one data structure with nested (heading, [children]) pairs
            headings = p.nested_headings()

            if len(p.outline()) > 0:

                print('flat headings= ', ["/".join([str(section.heading) for section in sectionpath]) for sectionpath in p.flat_headings_list()])

            if counter >= limit:
                break

            counter += 1


def preprocess_paragraphs(path=WikiParagrahs.file_path_list[0], limit=1):

    print('*** reading {} paragraph from file: {} ***'.format(limit, path))
    with open(path, 'rb') as f:

        counter = 1

        for p in iter_paragraphs(f):

            print('----------------------- PARA ID  -----------------------')
            print(p.para_id)

            print('----------------------- PARA TEXT  -----------------------')

            texts = [elem.text if isinstance(elem, ParaText)
                     else elem.anchor_text
                     for elem in p.bodies]

            print(texts)

            if counter >= limit:
                break

            counter += 1




