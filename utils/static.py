
import os
from collections import namedtuple

file_folder_path = os.path.join(os.path.abspath(os.path.join(__file__,"../..")), 'file_folder')


# define metadata for each dataset in a namedtuple
Dataset = namedtuple('Dataset', 'name url download_path unpack_dir_path file_path_list')

WikiParagrahs = Dataset(
    name='Wikipedia paragraphs',
    url='http://trec-car.cs.unh.edu/datareleases/v2.0/paragraphCorpus.v2.0.tar.xz',
    download_path=os.path.join(file_folder_path, 'paragraphCorpus.v2.0.tar.xz'),
    unpack_dir_path=file_folder_path,
    file_path_list=[os.path.join(file_folder_path, 'paragraphCorpus', 'dedup.articles-paragraphs.cbor')],
)

Wiki = Dataset(
    name='Wikipedia',
    url='http://trec-car.cs.unh.edu/datareleases/v2.1/unprocessedAllButBenchmark.v2.1.tar.xz',
    download_path=os.path.join(file_folder_path, 'unprocessedAllButBenchmark.v2.1.tar.xz'),
    unpack_dir_path=file_folder_path,
    file_path_list=[os.path.join(file_folder_path, 'paragraphCorpus', 'fold-4-unprocessedAllButBenchmark.Y2.cbor'),
               os.path.join(file_folder_path, 'paragraphCorpus', 'unprocessedAllButBenchmark.Y2.cbor')],
)


dataset_list = [WikiParagrahs, Wiki]