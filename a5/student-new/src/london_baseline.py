# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
import utils

eval_corpus_path = './birth_dev.tsv'

correct = 0
total = 0

predictions = ['London'] * len(open(eval_corpus_path).readlines())
total, correct = utils.evaluate_places(eval_corpus_path, predictions)
# if total > 0:
print('Correct: {} out of {}: {}%'.format(correct, total, correct/total*100))
