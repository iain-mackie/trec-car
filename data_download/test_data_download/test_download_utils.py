
import pytest
import os

@pytest.mark.skip(reason="Takes a long time to run")
@pytest.mark.webtest
def test_download_file(test_tar_xz_url, test_tar_xz_path):
    from data_download.dowload_utils import download_file
    download_file(url=test_tar_xz_url, path=test_tar_xz_path)
    assert os.path.exists(test_tar_xz_path)

@pytest.mark.skip(reason="Takes a long time to run")
def test_unpack_tar_file(test_tar_xz_path, test_tar_xz_unpack_dir, test_unpack_file_path):
     from data_download.dowload_utils import unpack_tar_file

     unpack_tar_file(read_path=test_tar_xz_path, write_dir_path=test_tar_xz_unpack_dir, file_path_list=test_unpack_file_path)
     assert os.path.exists(test_unpack_file_path)


@pytest.mark.skip(reason="Takes a long time to run")
def test_download_and_unpack_dataset(test_Dataset):
    from data_download.dowload_utils import download_and_unpack_dataset

    download_and_unpack_dataset(D=test_Dataset)
    assert os.path.exists(test_Dataset.file_path)


@pytest.mark.skip(reason="Takes a long time to run")
def test_download_and_unpack_datasets(test_dataset_list):
    from data_download.dowload_utils import download_and_unpack_datasets

    download_and_unpack_datasets(D=test_dataset_list)
    assert os.path.exists(test_dataset_list[0].file_path)
