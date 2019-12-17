

from index.static import write_d_path, write_d_norm_path, write_q_path, write_q_norm_path

from rank_bm25 import BM25Okapi
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
import nltk


try:
    nltk.data.find('tokenize/punkt')
except LookupError:
    nltk.download('tokenize')

try:
    nltk.data.find('stopwords/punkt')
except LookupError:
    nltk.download('stopwords')


def norm_string(s):

    words = word_tokenize(s.lower())

    stop_words = set(stopwords.words('english'))

    format_words = []
    for w in words:
        w_non_punc = w.translate(str.maketrans('', '', punctuation))

        if (w_non_punc not in stop_words) and (len(w_non_punc) > 0):
            format_words += [w_non_punc]

    return " ".join(format_words)


def normalise_q(read_path=write_q_path, write_path=write_q_norm_path):

    with open(read_path, 'r') as f_read:
        with open(write_path, 'w') as f_write:

            for l in f_read:
                split = [x for x in str(l).split('\t')]
                page_name = split[0]
                q = norm_string(s=split[1])

                f_write.write(page_name + '\t' + q + '\n')


def normalise_d(read_path=write_d_path, write_path=write_d_norm_path):

    with open(read_path, 'r') as f_read:
        with open(write_path, 'w') as f_write:

            for l in f_read:
                split = [x for x in str(l).split('\t')]
                para_id = split[0]
                q = norm_string(s=split[1])

                f_write.write(para_id + '\t' + q + '\n')

