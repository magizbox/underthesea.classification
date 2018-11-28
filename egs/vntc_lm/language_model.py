import subprocess
from os.path import abspath
import re

class SRILanguageModel:
    def __init__(self, sri_bin, savepath):
        self.sri_bin = sri_bin
        self.savepath = abspath(savepath)

    def fit(self, corpuspath):
        ngram_count_command = f"{self.sri_bin}/ngram-count"
        cmd = f"{ngram_count_command} -text {corpus_path} -lm {self.savepath} -order 2"
        output = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, universal_newlines=True)

    def predict(self, filepath):
        """ calculate logprob of a new text
        :rtype: float
        """
        ngram_command = f"{self.sri_bin}/ngram"
        cmd = f"{ngram_command} -lm {self.savepath} -order 2 -ppl \"{filepath}\""
        text = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
        text = text.stdout.split("\n")[1]
        score_text = re.search("logprob= (-?\d+(.\d+)?)", text).group(1)
        score = float(score_text)
        return score


if __name__ == '__main__':
    lm = SRILanguageModel(sri_bin="/usr/share/srilm/bin/i686-m64", savepath="tmp/lm.bin")
    corpus_path = "tmp/corpus.txt"
    lm.fit(corpus_path)
    filepath = "tmp/corpus-test.txt"
    score = lm.predict(filepath)
    print(score)