class SimpleEditor:
    def __init__(self, document):
        self.document = document
        self.dictionary = set()
        # On windows, the dictionary can often be found at:
        # C:/Users/{username}/AppData/Roaming/Microsoft/Spelling/en-US/default.dic
        with open("/usr/share/dict/words") as input_dictionary:
            for line in input_dictionary:
                words = line.strip().split(" ")
                for word in words:
                    self.dictionary.add(word)
        self.paste_text = ""
        self.dic_doc = dict((k, v) for k, v in enumerate(self.document))
        self.end = len(self.document)

    def cut(self, i, j):
        self.paste_list = [self.dic_doc[v] for v in range(i, j)]
        self.doc_front_list = [self.dic_doc[v] for v in range(i)]
        for v in range(j, self.end):
            self.doc_front_list.append(self.dic_doc[v])
        self.document = ''.join(self.doc_front_list)
    def copy(self, i, j):
        self.paste_list = [self.dic_doc[v] for v in range(i, j)]
    def paste(self, i):
        self.doc_front_list = [self.dic_doc[v] for v in range(i)]
        self.doc_end_list = [self.dic_doc[v] for v in range(i, self.end)]
        for v in self.paste_list:
            self.doc_front_list.append(v)
        for v in self.doc_end_list:
            self.doc_front_list.append(v)
        self.document = ''.join(self.doc_front_list)
    def get_text(self):
        return self.document

    def misspellings(self):
        result = 0
        for word in self.document.split(" "):
            if word not in self.dictionary:
                result = result + 1
        return result

    def find_word(self, word):
        word_index = self.document.find(word)
        return word_index

import timeit

class EditorBenchmarker:
    new_editor_case = """
from __main__ import SimpleEditor
s = SimpleEditor("{}")"""

    editor_cut_paste = """
for n in range({}):
    if n%2 == 0:
        s.cut(1, 3)
    else:
        s.paste(2)"""

    editor_copy_paste = """
for n in range({}):
    if n%2 == 0:
        s.copy(1, 3)
    else:
        s.paste(2)"""

    editor_get_text = """
for n in range({}):
    s.get_text()"""

    editor_mispellings = """
for n in range({}):
    s.misspellings()"""

    editor_find_word = """
for n in range({}):
    s.find_word('hello')"""

    def __init__(self, cases, N):
        self.cases = cases
        self.N = N
        self.editor_cut_paste = self.editor_cut_paste.format(N)
        self.editor_copy_paste = self.editor_copy_paste.format(N)
        self.editor_get_text = self.editor_get_text.format(N)
        self.editor_mispellings = self.editor_mispellings.format(N)
        self.editor_find_word = self.editor_find_word.format(N)

    def benchmark(self):
        for case in self.cases:
            print("Evaluating case: {}".format(case))
            new_editor = self.new_editor_case.format(case)
            cut_paste_time = timeit.repeat(stmt=self.editor_cut_paste,setup=new_editor,repeat=3,number=1)
            print("{} cut paste operations took {} s".format(self.N, cut_paste_time))
            copy_paste_time = timeit.repeat(stmt=self.editor_copy_paste,setup=new_editor,repeat=3,number=1)
            print("{} copy paste operations took {} s".format(self.N, copy_paste_time))
            get_text_time = timeit.repeat(stmt=self.editor_get_text,setup=new_editor,repeat=3,number=1)
            print("{} text retrieval operations took {} s".format(self.N, get_text_time))
            mispellings_time = timeit.repeat(stmt=self.editor_mispellings,setup=new_editor,repeat=3,number=1)
            print("{} mispelling operations took {} s".format(self.N, mispellings_time))
            find_word_time = timeit.repeat(stmt=self.editor_find_word,setup=new_editor,repeat=3,number=1)
            print("{} find word operations took {} s".format(self.N, find_word_time))
            

if __name__ == "__main__":
    b = EditorBenchmarker(["hello frends"], 20)
    b.benchmark()
