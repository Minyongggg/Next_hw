from django.shortcuts import render

# Create your views here.
def count(request):
    return render(request, 'count.html', {})

def result(request):
    text = request.POST['text']
    total_len = len(text)
    original_text = text
    len_noblank = len(text.replace(" ", ""))
    word_count = len(text.split(' '))

    return render(request, 'result.html', {'original_text':original_text, 'total_len': total_len, 'len_noblank':len_noblank, 'word_count':word_count,})