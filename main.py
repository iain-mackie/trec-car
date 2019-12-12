
from utils.dowload_utils import download_and_unpack_datasets
from utils.static import dataset_list, Wiki, WikiParagrahs
from data_exploration.printing_data import print_paragraphs, print_articles
from utils.static import Wiki, WikiParagrahs

if __name__ == "__main__":

    #download_and_unpack_datasets(D_list=dataset_list

    #print_paragraphs(path=WikiParagrahs.file_path_list[0], limit=1)
    print_articles(path=Wiki.file_path_list[4], limit=1)

