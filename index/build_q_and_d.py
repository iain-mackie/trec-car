
from data_download.static import WikiParagrahs, Wiki
from trec_car.read_data import iter_paragraphs, ParaText, ParaLink, iter_pages
from index.static import write_d_path, write_q_path


def build_q(read_path=Wiki.file_path_list[0], write_path=write_q_path, page_limit=1):

    print('*** reading {} articles from file: {} ***'.format(page_limit, read_path))
    with open(read_path, 'rb') as f_read:
        with open(write_path, 'w') as f_write:

            counter = 1

            for p in iter_pages(f_read):

                if counter % 1000 == 0:
                    print('{} / {} of pages processed'.format(counter, page_limit))

                page_name = p.page_name

                q_list = [page_name + " " + " ".join([str(section.heading) for section in sectionpath]) for sectionpath in p.flat_headings_list()]

                for q in q_list:

                    f_write.write(p.page_id + "\t" + q + "\n")

                if counter >= page_limit:
                    break

                counter += 1


def build_d(read_path=WikiParagrahs.file_path_list[0], write_path=write_d_path, paragraph_limit=1):

    print('*** reading {} paragraph from file: {} ***'.format(paragraph_limit, read_path))
    with open(read_path, 'rb') as f_read:
        with open(write_path, 'w') as f_write:

            counter = 1

            for p in iter_paragraphs(f_read):

                if counter % 10000 == 0:
                    print('{} / {} of paragraphs processed'.format(counter, paragraph_limit))

                f_write.write(p.para_id + '\t' + p.get_text() + '\n')

                if counter >= paragraph_limit:
                    break

                counter += 1

