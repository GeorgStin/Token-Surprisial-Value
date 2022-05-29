# imports
import math


##############################################
# 1. Read text
# Input:   Filename (str)
# Output:  Orthographic tokens (list)

def get_text(datei):
    infile = open(datei, mode='r', encoding='utf8')

    tokens = []

    # add every token to the list
    for line in infile:
        for tok in line.split():
            tokens.append(tok)

    infile.close()

    return tokens


##############################################
# 2. Sentence boundaries
# Input:  Orthographic tokens (list)
# Output: Tokens with correct token boundaries (list)

def tokenize(tokens):
    tokenized = []

    # "list index out of range" fix
    tokens.append('End')

    for i in range(len(tokens) - 1):

        if tokens[i].endswith('.') and tokens[i + 1].istitle():

            tokenized.append(tokens[i][:-1])
            tokenized.append(tokens[i][-1])
            tokenized.append('')

        else:
            tokenized.append(tokens[i])

    tokenized.pop()

    return tokenized


##############################################
# 3. Padding
# Input:  Tokens (list)
# Output: Tokens with padding (list)

def padding(sentences, ngram):
    tokens_pad = []

    # padding at the beginning of the text
    tokens_pad.extend(ngram)

    # padding at the beginning of each sentence
    for tok in sentences:
        if tok == '':
            tokens_pad.append('')
            tokens_pad.extend(ngram)
        else:
            tokens_pad.append(tok)

    return tokens_pad


##############################################
# 4. Ngrams counting
# Input:  Tokens with padding (list)
# Output: Ngrams with their freqs (dict)

def count_ngrams(tokens, ngram):
    freqs = {}

    # a loop for bigrams counting
    if ngram == 2:
        for i in range(len(tokens) - 1):
            bigram = (tokens[i], tokens[i + 1])

            if tokens[i] and tokens[i + 1] != '':
                freqs[bigram] = freqs.get(bigram, 0) + 1

    # a loop for trigrams counting
    if ngram == 3:
        for i in range(len(tokens) - 2):
            trigram = (tokens[i], tokens[i + 1], tokens[i + 2])

            if tokens[i] and tokens[i + 1] and tokens[i + 2] != '':
                freqs[trigram] = freqs.get(trigram, 0) + 1

    return freqs


##############################################
# 5. Surprisial
# Input:    Bigrams freqs (dict), Trigrams freqs (dict), Target token (str)
# Output:   Surprisial value (float)

def get_surprisial(bigrams, trigrams, target_token):
    # amount of all trigrams
    trigrams_sum = sum(trigrams.values())

    # freq of the target trigram
    for key, value in trigrams.items():
        if key[2] == target_token:
            trigram_freq = value
            target_trigram = key

    # relative trigram freq
    trigram_relfreq = trigram_freq / trigrams_sum


    # amount of all bigrams
    bigrams_sum = sum(bigrams.values())

    # find target bigram
    for key, value in trigrams.items():
        if key[2] == target_token:
            target_bigram = (key[0], key[1])

    # freq of the target bigram
    for key, value in bigrams.items():
        if key == target_bigram:
            bigram_freq = value

    # relative bigram freq
    bigram_relfreq = bigram_freq / bigrams_sum


    # conditional probability
    cond_prob = trigram_relfreq / bigram_relfreq

    # calculate surprisial
    surprisial = math.log2(1 / cond_prob)

    # output
    print('Surprisal of', '"' + target_token + '"', 'is:', surprisial)
    print('Context:', *target_trigram, sep=' ')

    return surprisial


##############################################
# Function that calls all other functions

def run_script(corpus, target_word):
    # 1. Read text/corpus „korpus.txt“
    tokens = get_text(corpus)

    # 2. Satzgrenzen
    sentences = tokenize(tokens)

    # 3. Padding
    bigram = ['^', '^']  # Padding tokens for bigrams
    trigram = ['^', '^', '^']  # Padding tokens for trigrams
    bigram_pad_sentences = padding(sentences, bigram)
    trigram_pad_sentences = padding(sentences, trigram)

    # 4. Ngrams counting
    bigrams_freqs = count_ngrams(bigram_pad_sentences, 2)
    trigrams_freqs = count_ngrams(trigram_pad_sentences, 3)

    # 5. Surprisial calculating
    surprisial = get_surprisial(bigrams_freqs, trigrams_freqs, target_token)


###########################################################
# Main program
###########################################################

if __name__ == "__main__":

    corpus = "korpus.txt"  # File name of the text / corpus
    target_token = "men"   # Target word / token

    # Function that calls all other functions
    run_script(corpus, target_token)
