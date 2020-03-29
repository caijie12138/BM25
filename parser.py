# Data preprocess
# author: Caiie

import re

class CorpusParser(object):
    def __init__(self,file_path):
        self.file_path = file_path
        self.regex = re.compile('^#\s*\d+')
        self.corpus = dict()

    def parse(self):
        '''
        Put the corpus in a dict with 'id':[text] pattern.
        :return: None
        '''
        with open(self.file_path) as f:
            cur_id = 0
            for line in f.readlines():
                if line[0] == '#':
                    cur_id = line.strip().split()[-1]
                    self.corpus[cur_id] = []
                    continue
                self.corpus[cur_id].extend(line.strip().split())

    def get_corpus(self):
        '''
        Get the structural corpus.
        :return: self.corpus
        '''
        return self.corpus

class QueryParser(object):
    def __init__(self,file_path):
        self.file_path = file_path
        self.quires = []

    def parse(self):
        '''
        Put the quires in a list.
        :return: None
        '''
        with open(self.file_path) as f:
            for line in f.readlines():
                self.quires.append(line.strip().split())

    def get_quires(self):
        '''
        Get the structural corpus.
        :return: self.corpus
        '''
        return self.quires


