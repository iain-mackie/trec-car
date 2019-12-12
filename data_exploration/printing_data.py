
from utils.static import Wiki, WikiParagrahs
from trec_car.read_data import iter_paragraphs, iter_pages, iter_annotations, ParaText, ParaLink


def print_paragraphs(path=WikiParagrahs.file_path_list[0], limit=1):

    print('*** reading {} paragraph from file: {} ***'.format(limit, path))
    with open(path, 'rb') as f:

        counter = 1

        for p in iter_paragraphs(f):

            print()
            print('PRINTING PARAGRAPH {}'.format(counter))

            print('----------------------- RAW PARAGRAPH  -----------------------')
            print(p)

            # Print just the text
            texts = [elem.text if isinstance(elem, ParaText)
                     else elem.anchor_text
                     for elem in p.bodies]
            print('----------------------- TEX  -----------------------------')
            print(' '.join(texts))

            print('----------------------- ENTITIES -----------------------------')
            entities = [elem.page
                        for elem in p.bodies
                        if isinstance(elem, ParaLink)]
            print(entities)

            print('----------------------- MIXED -----------------------------')
            mixed = [(elem.anchor_text, elem.page) if isinstance(elem, ParaLink)
                     else (elem.text, None)
                     for elem in p.bodies]
            print(mixed)


            if counter >= limit:
                break

            counter += 1


def print_articles(path=Wiki.file_path_list[5], limit=1):

    print('*** reading {} articles from file: {} ***'.format(limit, path))
    with open(path, 'rb') as f:

        counter = 1

        for p in iter_pages(f):

            print('PRINTING PAGE {}'.format(counter))

            print('----------------------- RAW PAGE  -----------------------')
            print(p)

            print('-----------------------  METADATA  -----------------------')

            print('\npagename:', p.page_name)
            print('\npageid:', p.page_id)
            print('\nmeta:', p.page_meta)

            print('----------------------- HEADINGS  -----------------------')
            # get one data structure with nested (heading, [children]) pairs
            headings = p.nested_headings()
            print(headings)

            print('----------------------- OUTLINES  -----------------------')
            if len(p.outline()) > 0:
                print(p.outline()[0].__str__())

                print('deep headings= ',
                      [(str(section.heading), len(children)) for (section, children) in p.deep_headings_list()])

                print('flat headings= ', ["/".join([str(section.heading) for section in sectionpath]) for sectionpath in
                                          p.flat_headings_list()])

            if counter >= limit:
                break

            counter += 1


def print_outlines(path='', limit=1):

    print('*** reading {} outlines from file: {} ***'.format(limit, path))

    with open(path, 'rb') as f:

        counter = 1

        for p in iter_annotations(f):

            print()
            print('PRINTING OUTLINE {}'.format(counter))

            print('-----------------------  METADATA  -----------------------')

            print('\npagename:', p.page_name)

            print('----------------------- OUTLINES  -----------------------')
            # get one data structure with nested (heading, [children]) pairs
            headings = p.nested_headings()
            print('headings= ', [(str(section.heading), len(children)) for (section, children) in headings])

            if len(p.outline()) > 2:
                print('heading 1=', p.outline()[0])

                print('deep headings= ',
                      [(str(section.heading), len(children)) for (section, children) in p.deep_headings_list()])

                print('flat headings= ', ["/".join([str(section.heading) for section in sectionpath]) for sectionpath in
                                          p.flat_headings_list()])

            if counter >= limit:
                break

            counter += 1