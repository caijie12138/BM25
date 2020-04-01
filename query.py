# Calculate BM25 for each word in the query
# author: CaiJie

from invert_index import *
from rank import *

class QueryProcess(object):
    def __init__(self,queries,cropus):
        self.queries = queries
        self.invert, self.doclentable = build_data_structural(cropus)
        self.avg_doclen=self.doclentable.get_average_length()

    def run(self):
        '''
        Calculate BM25 for each word in the query
        :return: BM25 results
        '''
        results = []
        for query in self.queries:
            results.append(self.run_for_query(query))
        return results

    def run_for_query(self,query):
        '''
        Calculate the BM25 value for each word in query
        :param query: Question
        :return: BM25 value
        '''
        query_results = dict()
        for word in query:
            has_word = self.invert.index.get(word,None)
            if has_word:
                doc_dic = self.invert.index[word]
                for docid,freq in doc_dic.items():
                    K = compute_K(doclen=self.doclentable.get_length(docid),avg_doclen=self.avg_doclen)
                    score = BM25_score(N=len(self.doclentable),df_i=len(doc_dic),f_i=freq,qf_i=1,K=K)
                    if docid in query_results:
                        query_results[docid] += score
                    else:
                        query_results[docid] = score
        return query_results








