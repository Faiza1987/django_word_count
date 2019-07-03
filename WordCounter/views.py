from django.http import HttpResponse
from django.shortcuts import render
import operator

# homepage url
def homepage(request):
    return render(request, 'homepage.html')


def count(request):
    fulltext = request.GET['fulltext']

    word_list = fulltext.split()

    word_dictionary = {}

    for word in word_list:
        if word != '--' and word in word_dictionary:
            # Increase
            word_dictionary[word] += 1

        else:
            # Add to dictionary
            word_dictionary[word] = 1



        sorted_words = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)


    return render(
        request,
        'count.html',
        {
            'fulltext': fulltext,
            'count': len(word_list),
            # 'word_dictionary': word_dictionary
            # OR
            'sorted_words':sorted_words
        }
    )


def about(request):
    return render(request, 'about.html')