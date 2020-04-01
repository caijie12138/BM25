# Main Function
# author: CaiJie

import argparse
from parser import *
from query import *

def main(query_file,doc_file):
    query_parser = QueryParser(query_file)
    doc_parser = CorpusParser(doc_file)

    #query_parser and doc_parser
    query_parser.parse()
    queries = query_parser.get_queries()
    doc_parser.parse()
    corpus = doc_parser.get_corpus()

    #get the BM25 values
    query_proc = QueryProcess(queries,corpus)
    results = query_proc.run()

    qid = 0
    for res in results:
        sorted_x = sorted(res.items(),key = lambda x:x[1])
        sorted_x.reverse()
        index = 0
        for i in sorted_x[:10]:
            print(f'{qid}\t{i[0]}\t{index}\t{i[1]}')
            index += 1
        qid += 1


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--query_file',required=True,help='query_file path')
    parser.add_argument('--doc_file', required=True, help='doc_file path')
    args = parser.parse_args()
    main(args.query_file,args.doc_file)