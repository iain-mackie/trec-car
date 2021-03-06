
import os
from collections import namedtuple

file_folder_path = os.path.join(os.path.abspath(os.path.join(__file__,"../..")), 'file_folder', '1_raw_data')


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
    file_path_list=[
                os.path.join(file_folder_path, 'unprocessedAllButBenchmark.v2.1', 'fold-0-unprocessedAllButBenchmark.Y2.cbor'),
                os.path.join(file_folder_path, 'unprocessedAllButBenchmark.v2.1', 'fold-1-unprocessedAllButBenchmark.Y2.cbor'),
                os.path.join(file_folder_path, 'unprocessedAllButBenchmark.v2.1', 'fold-2-unprocessedAllButBenchmark.Y2.cbor'),
                os.path.join(file_folder_path, 'unprocessedAllButBenchmark.v2.1', 'fold-3-unprocessedAllButBenchmark.Y2.cbor'),
                os.path.join(file_folder_path, 'unprocessedAllButBenchmark.v2.1', 'fold-4-unprocessedAllButBenchmark.Y2.cbor'),
                os.path.join(file_folder_path, 'unprocessedAllButBenchmark.v2.1', 'unprocessedAllButBenchmark.Y2.cbor')],
)

Train = Dataset(
    name='Train',
    url='http://trec-car.cs.unh.edu/datareleases/v2.0/train.v2.0.tar.xz',
    download_path=os.path.join(file_folder_path, 'train.v2.0.tar.xz'),
    unpack_dir_path=file_folder_path,
    file_path_list=[os.path.join(file_folder_path, 'train.v2.0', '')], #TODO
)

Benchmark = Dataset(
    name='Train',
    url='http://trec-car.cs.unh.edu/datareleases/v2.0/benchmarkY1-test.v2.0.tar.xz',
    download_path=os.path.join(file_folder_path, 'benchmarkY1-test.v2.0.tar.xz'),
    unpack_dir_path=file_folder_path,
    file_path_list=[os.path.join(file_folder_path, 'TODO')], #TODO
)



dataset_list = [WikiParagrahs, Wiki]