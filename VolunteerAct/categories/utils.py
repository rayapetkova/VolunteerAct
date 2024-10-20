from yake import KeywordExtractor


extractor = KeywordExtractor()


def count_events(count, max_number):
    if count > max_number:
        return f"{count - 1}+"

    return count


def extract_keywords(text):
    keywords_tuples = extractor.extract_keywords(text)
    keywords = set()

    for kw in keywords_tuples:
        if len(kw[0].split()) == 1:
            keywords.add(kw[0])

    return list(keywords)[:8]
