from django.shortcuts import render
from .forms import TextForm
from .utils import summarize_text

def upload(request):
    summary = ''
    if request.method == 'POST':
        form = TextForm(request.POST)
        if 'submit_summary' in request.POST:  # 要約ボタンが押されたとき
            if form.is_valid():
                text = form.cleaned_data['text']
                summary = summarize_text(text)
        elif 'reset_text' in request.POST:  # 消去ボタンが押されたとき
            form = TextForm()  # フォームをリセット
    else:
        form = TextForm()

    return render(request, 'upload.html', {'form': form, 'summary': summary})

