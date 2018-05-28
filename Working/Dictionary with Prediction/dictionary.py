import json
from difflib import get_close_matches
def load_corpus():
    with open("corpus.json", "r") as write_file:
      data = json.load( write_file)
      data = {k.lower():v for k, v in data.items()}
      return data


def get_def(data, word):
    if word  in data:
        return   " || ".join(data.get(word)) 
    elif len(get_close_matches(word, data.keys())) > 0:
        temp = get_close_matches(word, data.keys(),n = 8)
        return get_def(data, temp[0]) if input(
            'Did you mean ' + temp[0]+'? enter y or n.'
        ) == 'y' else  """No such word found try again please with other similar words : """ + " ,".join(temp[1:])

    else:
        return "No such word found try again please"
if __name__ == '__main__':
    data = load_corpus()
    print(get_def(data, input("Please enter the word? \n").lower()))



# from difflib import SequenceMatcher
#  for key in data.keys():
#     return SequenceMatcher(None,word,key).ratio()