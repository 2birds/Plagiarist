class Predictor(object):
    def __init__(self):
        self.model = {}

    def associate(self, word, following_word):
        entry = self.model.setdefault(word, {following_word : 0})
        entry[following_word] = entry.setdefault(following_word, 0) + 1

    def generate_predictive_model(self):

        def build_likelyhoods(word_counts):
            total = sum(word_counts.values())
            likelihoods = []
            for k, v in word_counts.items():
                likelihoods.append((k, v / float(total)))

            likelihoods.sort(key = lambda a : a[1])
            running_total = 0
            for i in range(len(likelihoods)):
                n = likelihoods[i][1]
                likelihoods[i] = (likelihoods[i][0], n + running_total)
                running_total += n

            return likelihoods


        self.predictive_model = {}

        for key, value in self.model.items():
            self.predictive_model[key] = build_likelyhoods(value)

    def predict(self, word, chance=0):
        if not hasattr(self, 'predictive_model'):
            raise
        for w in self.predictive_model[word]:
            if chance < w[1]:
                return w[0]

if __name__ == '__main__':
    p = Predictor()

    s = "the cat sat on the mat"
    t = s.split()
    for i in range(len(t)-1):
        p.associate(t[i], t[i+1])

    p.generate_predictive_model()

