def count_characters(text):
    return len(text.replace(" ", ""))

if __name__ == "__main__":
    article = input("請輸入文章：\n")
    character_count = count_characters(article)
    print(f"文章的字數（不含空格）為：{character_count}")
