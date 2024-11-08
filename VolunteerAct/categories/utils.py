from yake import KeywordExtractor
from VolunteerAct.categories.models import Event, Category
from django.utils import timezone
from django.db.models import Count


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


def get_categories():
    categories = Category.objects.all()
    categories_names_tuple = [(category.name, category.name) for category in categories]

    return categories_names_tuple


def get_cities():
    cities = Event.objects.values('city').annotate(cities_count=Count('city')).order_by('-cities_count')
    cities_tuple = [(cityDict['city'], f"{cityDict['city']} ({cityDict['cities_count']})") for cityDict in cities]

    return cities_tuple
