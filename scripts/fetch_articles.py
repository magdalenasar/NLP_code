from newspaper import build

# Задай URL на новинарски сайт (пример: BBC)
news_url = "https://www.bbc.com"

# Изграждане на обект за новинарския сайт
paper = build(news_url, memoize_articles=False)

# Извеждане на броя намерени статии
print(f"Намерени {len(paper.articles)} статии от {news_url}")

# Обхождаме първите 3 статии, за да проверим дали всичко работи
for idx, article in enumerate(paper.articles[:3], start=1):
    try:
        article.download()
        article.parse()
        print(f"\nСтатия {idx}:")
        print("Заглавие:", article.title)
        print("Първи 200 символа от текста:", article.text[:200])
    except Exception as e:
        print(f"Грешка при обработка на статия {idx}: {e}")
