
from data_download.download import download_and_unpack_dataset, download_and_unpack_datasets
from data_download.static import WikiParagrahs, Wiki, dataset_list, Train, Benchmark

from index.static import write_q_path, write_d_path, write_q_norm_path, write_d_norm_path, write_rank_path
from index.build_q_and_d import build_q, build_d
from index.normalise_q_and_d import normalise_q, normalise_d
from index.ranking import retrieve_n_documents

import os

def anserini_hex_check():
    in_path = os.path.join(os.getcwd(), 'train_tree.topics')
    out_path = os.path.join(os.getcwd(), 'train_tree_out.topics')

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    alpha = ['A', 'B', 'C', 'D', 'E', 'F']
    valid_char = numbers + alpha
    hex_utc8 = []
    for c1 in valid_char:
        for c2 in valid_char:
            hex_utc8.append(c1 + c2)

    with open(in_path, "r") as f:
        lines = f.readlines()

    with open(out_path, "w") as f:
        for line in lines:
            if '%' in line:
                new_line = ''
                counter = 0
                for l in line:
                    if l == '%':
                        if line[counter + 1:counter + 3] in hex_utc8:
                            new_line += l
                        else:
                            print(line[counter:counter + 3])
                            new_line += '%25'
                    else:
                        new_line += l
                    counter += 1
                f.write(new_line)
            else:
                f.write(line)

def galago_numbers():
    in_path = os.path.join(os.getcwd(), 'test.topics')
    out_path = os.path.join(os.getcwd(), 'test_galago.topics')
    with open(in_path, "r") as f:
        lines = f.readlines()

    with open(out_path, "w") as f:
        counter = 0
        for line in lines:
            new_line = str(counter) + "\t" + line
            print(new_line)
            f.write(new_line)
            counter += 1



if __name__ == "__main__":
    #galago_numbers()
    anserini_hex_check()


















