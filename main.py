
from data_download.download import download_and_unpack_dataset
from data_download.static import WikiParagrahs, Wiki, dataset_list

from index.build_q_and_d import build_q, build_d
from index.normalise_q_and_d import normalise_q
from index.static import write_q_path, write_d_path, write_q_norm_path


if __name__ == "__main__":

    #download_and_unpack_dataset(D=Wiki)
    #
    #build_q(read_path=Wiki.file_path_list[5], write_path=write_q_path, page_limit=1500)
    #
    #build_d(read_path=WikiParagrahs.file_path_list[0], write_path=write_d_path, paragraph_limit=100)

    normalise_q(read_path=write_q_path, write_path=write_q_norm_path)














