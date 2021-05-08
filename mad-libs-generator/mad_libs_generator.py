import random

def create_stories():
    weird_news = 'A sub was arrested this morning after he sub in front of sub. sub, had a history of sub, but' \
                 ' no one - not even his sub ever imagined he\'d sub with a sub stuck in his sub.' \
                 " I always thought he was sub, but I never thought he'd do something like this. Even his sub was surprised." \
                 " After a brief sub, cops followed him to a sub, where he reportedly sub in the fry machine." \
                 " In sub, a woman was charged with a similar crime. But rather than sub with a sub, she sub with a sub dog." \
                 " Either way, we imagine that after witnessing him sub there are probably a whole lot of sub that are going to need some therapy."

    weird_news_words = ['noun', 'verb', 'noun', 'name', 'verb', 'noun', 'verb', 'noun', 'part of the body', 'adjective',
                        'relative', 'activity', 'place', 'adjective/verb, past tense', 'month', 'verb', 'noun',
                        'verb, past tense', 'adjective', 'verb', 'plural noun']

    stories = {0: [weird_news, weird_news_words]}
    return stories

def mad_lib():
    stories = create_stories()
    index = random.randint(0, len(stories) - 1)
    story = stories[index][0]
    words = stories[index][1]
    for word in words:
        input_word = input('Give me a ' + word + ': ')
        story = story.replace('sub', input_word, 1)
    print(story)



mad_lib()