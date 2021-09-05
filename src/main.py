import Parser
import Predictor
import random
import sys

def main():
    fname = sys.argv[-2]
    number_of_symbols = int(sys.argv[-1])

    predictor = Predictor.Predictor()

    with Parser.Parser(fname) as p:
        prev_word = p.next()
        next_word = p.next()

        while next_word != None:
            predictor.associate(prev_word, next_word)
            prev_word = next_word
            next_word = p.next()

    predictor.generate_predictive_model()

    next_word = list(predictor.model.keys())[0]
    text = next_word

    for i in range(number_of_symbols):
        next_word = predictor.predict(next_word, random.random())    
        if next_word in ".,?!\"';:":
            text += next_word
        else:
            text += " " + next_word

    print(text)

if __name__ == '__main__':
    main()
