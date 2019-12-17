
from data_download.static import Wiki, WikiParagrahs
from trec_car.read_data import iter_paragraphs, iter_pages, iter_annotations, ParaText, ParaLink


def print_articles(path=Wiki.file_path_list[5], limit=1):

    print('*** reading {} articles from file: {} ***'.format(limit, path))
    with open(path, 'rb') as f:

        counter = 1

        for p in iter_pages(f):

            print('*** PRINTING PAGE {} ***'.format(counter))
            print('PageType  -> ArticlePage | CategoryPage | RedirectPage ParaLink | DisambiguationPage')

            print('----------------------- RAW PAGE  -----------------------')

            print(p)

            print('----------------------- INFO  -----------------------')
            print('page_name:', p.page_name)
            print('page_id:', p.page_id)
            print('page_type:', p.page_type)

            print('-----------------------  METADATA  -----------------------')

            print('PageMetadata -> RedirectNames DisambiguationNames DisambiguationIds CategoryNames CategoryIds InlinkIds InlinkAnchors')
            print('''
            RedirectNames       -> [$pageName] 
            DisambiguationNames -> [$pageName] 
            DisambiguationIds   -> [$pageId] 
            CategoryNames       -> [$pageName] 
            CategoryIds         -> [$pageId] 
            InlinkIds           -> [$pageId] 
            InlinkAnchors       -> [$anchorText])
            ''')

            print('page_meta:', p.page_meta)

            print('----------------------- SKELTON  -----------------------')

            print('''
            Section      -> $sectionHeading [PageSkeleton]
            Para         -> Paragraph
            Paragraph    -> $paragraphId, [ParaBody]
            ListItem     -> $nestingLevel, Paragraph
            Image        -> $imageURL [PageSkeleton]
            ParaBody     -> ParaText | ParaLink
            ParaText     -> $text
            ParaLink     -> $targetPage $targetPageId $linkSection $anchorText
            ''')
            print(p.skeleton)

            print('----------------------- HEADINGS RAW  -----------------------')
            # get one data structure with nested (heading, [children]) pairs
            headings = p.nested_headings()
            print(headings)

            print('----------------------- HEADINGS UNPACKED  -----------------------')
            if len(p.outline()) > 0:
                print(p.outline()[0].__str__())

                print('deep headings= ',
                      [(str(section.heading), len(children)) for (section, children) in p.deep_headings_list()])

                print('flat headings= ', ["/".join([str(section.heading) for section in sectionpath]) for sectionpath in
                                          p.flat_headings_list()])

            if counter >= limit:
                break

            counter += 1


def print_paragraphs(path=WikiParagrahs.file_path_list[0], limit=1):

    print('*** reading {} paragraph from file: {} ***'.format(limit, path))
    with open(path, 'rb') as f:

        counter = 1

        for p in iter_paragraphs(f):

            print()
            print('*** PRINTING PARAGRAPH {} ***'.format(counter))

            print('----------------------- PARAGRAPH ID  -----------------------')

            print(p.para_id)

            print('----------------------- RAW PARAGRAPH  -----------------------')
            print(p)

            # Print just the text
            texts = [elem.text if isinstance(elem, ParaText)
                     else elem.anchor_text
                     for elem in p.bodies]
            print('----------------------- TEXT  -----------------------------')
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

