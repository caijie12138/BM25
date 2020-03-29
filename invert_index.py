# invert_index.py
# author CaiJie

class InvertIndex(object):
    def __init__(self):
        self.index = dict()

    def __contains__(self,item):
        return item in self.index

    def __getitem__(self,item):
        return self.index[item]

    def add(self,docid,word):

