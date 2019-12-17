
import pytest
import os


@pytest.fixture
def test_tar_xz_url():
    return 'http://trec-car.cs.unh.edu/datareleases/v2.0/paragraphCorpus.v2.0.tar.xz'


@pytest.fixture
def test_tar_xz_path():
    return os.path.join(os.path.abspath(os.path.join(__file__,"../")), 'test_utils', 'test_file_folder', '1_raw_data', 'paragraphCorpus.v2.0.tar.xz')


@pytest.fixture
def test_tar_xz_unpack_dir():
    return os.path.join(os.path.abspath(os.path.join(__file__,"../")), 'test_utils', 'test_file_folder', '1_raw_data')


@pytest.fixture
def test_unpack_file_path():
    return [os.path.join(os.path.abspath(os.path.join(__file__,"../")), 'test_utils', 'test_file_folder', '1_raw_data', 'paragraphCorpus', 'dedup.articles-paragraphs.cbor')]


@pytest.fixture
def test_Dataset(test_tar_xz_url, test_tar_xz_path, test_tar_xz_unpack_dir, test_unpack_file_path):
    from data_download.static import Dataset
    return Dataset(
        name='Test dataset',
        url=test_tar_xz_url,
        download_path=test_tar_xz_path,
        unpack_dir_path=test_tar_xz_unpack_dir,
        file_path=test_unpack_file_path
    )

@pytest.fixture
def test_dataset_list(test_Dataset):
    return [test_Dataset]
