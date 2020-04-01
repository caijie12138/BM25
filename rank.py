# BM25
# author: CaiJie

from math import log

k1 = 2
k2 = 1
b = 0.75

def BM25_score(N, df_i, f_i, qf_i, K):
    '''
    :param N: The total number of documents
    :param df_i: The total number of documents containing the term q
    :param f_i: The frequency of q that occurrence in the document
    :param qf_i: The number of q times in user questions
    :param K:
    :param query:
    :return:
    '''

    W_i = log((N - df_i + 0.5) / (df_i + 0.5))
    R_i = f_i * (k1 + 1) / (f_i + K) * qf_i * (k2 + 1) / (qf_i + k2)

    return W_i*R_i

def compute_K(doclen, avg_doclen):
    return k1 * (1 - b + b * doclen / avg_doclen)
