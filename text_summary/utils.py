def summarize_text(text):
    # ここに要約処理を追加
    # 簡単な例として、テキストを30%に短縮するだけです
    sentences = text.split('。')
    num_sentences = max(1, len(sentences) // 3)
    summary = '。'.join(sentences[:num_sentences]) + '。'
    return summary
