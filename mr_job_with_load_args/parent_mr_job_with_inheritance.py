import re

from mrjob.job import MRJob

WORD_RE = re.compile(r"[\w']+")


class MRWordFrequencyCount(MRJob):
    def mapper_get_words(self, _, line):
        for word in WORD_RE.findall(line):
            result = self.process_mapper_get_words(word)
            yield result[0], result[1]

    def process_mapper_get_words(self, word):
        pass


if __name__ == '__main__':
    MRWordFrequencyCount.run()
