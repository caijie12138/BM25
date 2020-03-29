import argparse
from parser import *

def main(query_file,doc_file):
    query_parser = QueryParser(query_file)
    doc_parser = CorpusParser(doc_file)

    


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--query_file',required=True,help='query_file path')
    parser.add_argument('--doc_file', required=True, help='doc_file path')
    args = parser.parse_args()
    main(args.query_file,args.doc_file)