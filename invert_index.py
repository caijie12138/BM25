# invert_index.py
# author CaiJie

class InvertIndex(object):
    def __init__(self):
        self.index = dict()

    def __contains__(self,item):
        return item in self.index

    def __getitem__(self,item):
        return self.index[item]

    def add(self,word,docid):
        '''
        add a invert index to self.index and convenient after the statistical frequency
        :param docid: the id of document
        :param word: the unique word that occurs in document
        :return: None
        '''
        if word in self.index:
            if docid in self.index[word]:
                self.index[word][docid] += 1
            else:
                self.index[word][docid] = 1
        else:
            self.index[word] = dict()
            self.index[word][docid] = 1

    def get_document_frequency(self,word,docid):
        '''
        Gets the frequency of a word in an article
        :param word: the word
        :param docid: article
        :return: the frequency
        '''
        has_word = self.index.get(word,None)
        if has_word:
            has_doc = self.index[word].get(docid, None)
            if has_doc:
                return self.index[word][docid]
            else:
                raise LookupError('%s is not in $s-th article' % (word, docid))
        else:
            raise LookupError('There is not the word: %s' % word)

    def get_index_frequency(self,word):
        '''
        Gets the frequency of a word in all articles
        :param word: the word
        :return: the frequency
        '''
        has_word = self.index.get(word,None)
        if has_word:
            return len(self.index[word])
        else:
            raise LookupError('There is not the word: %s' % word)

class DocumentLengthTable(object):
    def __init__(self):
        self.table = dict()

    def __len__(self):
        return len(self.table)

    def add(self,docid,length):
        self.table[docid] = length

    def get_length(self,docid):
        has_doc = self.table.get(docid,None)
        if has_doc:
            return self.table[docid]
        else:
            raise LookupError('%s doc is not found' % docid)

    def get_average_length(self):
        '''
        Calculate the average document length
        :return: average document length
        '''
        sum = 0
        for _,value in self.table.items():
            sum += value
        return sum / len(self.table)

def build_data_structural(corpus):
    '''
    Building data structures
    :param corpus:
    :return: InvertIndex() and DocumentLengthTable()
    '''
    invert = InvertIndex()
    doclentable = DocumentLengthTable()

    for docid in corpus:
        for word in corpus[docid]:
            invert.add(word,docid)

        doclentable.add(docid,len(corpus[docid]))
    return invert,doclentable
