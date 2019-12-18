
from data_download.download import download_and_unpack_dataset
from data_download.static import WikiParagrahs, Wiki, dataset_list

from index.static import write_q_path, write_d_path, write_q_norm_path, write_d_norm_path, write_rank_path
from index.build_q_and_d import build_q, build_d
from index.normalise_q_and_d import normalise_q, normalise_d
from index.ranking import retrieve_n_documents


if __name__ == "__main__":

    #download_and_unpack_dataset(D=Wiki)
    #
    build_q(read_path=Wiki.file_path_list[5], write_path=write_q_path, page_limit=500)

    build_d(read_path=WikiParagrahs.file_path_list[0], write_path=write_d_path, paragraph_limit=100000)

    normalise_q(read_path=write_q_path, write_path=write_q_norm_path)

    normalise_d(read_path=write_d_path, write_path=write_d_norm_path)

    retrieve_n_documents(read_path=write_q_norm_path, write_path=write_rank_path,  n=5)















