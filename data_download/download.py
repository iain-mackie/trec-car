
from urllib import request
import tarfile
import os

from data_download.static import dataset_list


def download_file(url, path):

    if os.path.exists(path=path):
        print('File already exists - will not download again (delete manually if required)')

    else:
        print('Downloading file from URL: {}'.format(url))
        request.urlretrieve(url, path)

        if os.path.exists(path=path):
            print('Saved file to path: {}'.format(path))
        else:
            print('ERROR - file has not correctly written')


def unpack_tar_file(read_path, write_dir_path, file_path_list):

    print('Unpacking tar file from: {}'.format(read_path))
    my_tar = tarfile.open(read_path)

    print('Writing to dir path: {}'.format(write_dir_path))
    my_tar.extractall(write_dir_path)
    my_tar.close()

    for f in file_path_list:
        if os.path.exists(path=f):
            print('File unpacked to path: {}'.format(f))
        else:
            print('ERROR - file has not correctly written: {}'.format(f))


def download_and_unpack_dataset(D):

    print('*** Downloading {} dataset ***'.format(D.name))
    download_file(D.url, D.download_path)

    print('*** Unpacking {} dataset ***'.format(D.name))
    unpack_tar_file(read_path=D.download_path, write_dir_path=D.unpack_dir_path, file_path_list=D.file_path_list)

    print(' ------------- '.format(D.name))


def download_and_unpack_datasets(D_list=dataset_list):

    counter = 1
    for D in D_list:
        print(' ----- Downloading {}/{} datasets ------ '.format(counter, len(D)))
        download_and_unpack_dataset(D=D)
        counter += 1





