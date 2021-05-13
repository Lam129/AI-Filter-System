def connect():
    """
    connect to mongodb server
    """
    username = "Samuel"
    pw = "samuelyeung"
    link = "mongodb+srv://" + username + ":" + pw + "@cluster0.fb1fv.mongodb.net/test"
    return link


def find_key(text):
    """extract most used words (keywords)"""
    from nltk import tokenize
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    import math

    def check_sent(word, sentences):
        """check if the word is present in a sentence list"""
        final = [all([w in x for w in word]) for x in sentences]
        sent_len = [sentences[i] for i in range(0, len(final)) if final[i]]
        return int(len(sent_len))

    def get_top_n(dict_elem, n):
        """get top N important words in the document"""
        from operator import itemgetter
        result = dict(sorted(dict_elem.items(), key=itemgetter(1), reverse=True)[:n])
        return result

    stop_words = stopwords.words('english')
    stop_words.extend(['-', 'I', 'The', '&', 'quite', "3", "How", "like", "(about", "5", "It's", "When", "ordered",
                       "assumed", "conducting", "similar", "Bose", "are,", "thought�", "work:normally", '"%hh%"=="',
                       "i'm", "would", "i've", "adjust", "amazon", "phone", "4", "make", "back", "work", "isn�t",
                       "cv1", "expect", "next"])

    # find total words
    text = text
    total_words = text.split()
    total_word_length = len(total_words)
    print("total_words:", total_word_length)

    # find total sentence
    total_sentences = tokenize.sent_tokenize(text)
    total_sent_len = len(total_sentences)
    # print(total_sent_len)

    # count total frequency score for each word
    tf_score = {}
    for each_word in total_words:
        each_word = each_word.replace('.', '')
        if each_word not in stop_words:
            if each_word in tf_score:
                tf_score[each_word] += 1
            else:
                tf_score[each_word] = 1

    # Dividing by total_word_length for each dictionary element
    tf_score.update((x, y / int(total_word_length)) for x, y in tf_score.items())
    # print(tf_score)

    # calculate idf score
    idf_score = {}
    for each_word in total_words:
        each_word = each_word.replace('.', '')
        if each_word not in stop_words:
            if each_word in idf_score:
                idf_score[each_word] = check_sent(each_word, total_sentences)
            else:
                idf_score[each_word] = 1

    # Performing a log and divide
    idf_score.update((x, math.log(int(total_sent_len) / y)) for x, y in idf_score.items())
    # print(idf_score)

    # calculate tf*idf score
    tf_idf_score = {key: tf_score[key] * idf_score.get(key, 0) for key in tf_score.keys()}
    # print(tf_idf_score)

    # get top five words of significance
    print(get_top_n(tf_idf_score, 10))