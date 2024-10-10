import re

def replaceWithTag(shorcut, tag, sentence):
    matches = re.finditer(re.escape(shorcut), sentence)
    new_sentence = ''
    last_match_end = 0
    for index, match in enumerate(matches):
        if index % 2 == 0:
            new_sentence += sentence[last_match_end:match.start()] + f'<{tag}>'
        else:
            new_sentence += sentence[last_match_end:match.start()] + f'</{tag}>'
        last_match_end = match.end()
    return new_sentence + sentence[last_match_end:] 

def main():
    while True:
        try:
            sentence = input()
            sentence = replaceWithTag('_', 'i', sentence)
            sentence = replaceWithTag('*', 'b', sentence)
            print(sentence)
        except EOFError:
            break
if __name__ == "__main__":
    main()