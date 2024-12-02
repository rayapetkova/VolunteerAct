from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from yake import KeywordExtractor
from VolunteerAct.categories.models import Event, Category
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
    cities_tuple = [(cityDict['city'], f"{cityDict['city']} ({cityDict['cities_count']})") for cityDict in cities if cityDict['city'] != 'online_event']
    online_events_tuples = [(cityDict['city'], f"Online ({cityDict['cities_count']})") for cityDict in cities if cityDict['city'] == 'online_event']

    cities_and_online_tuple = cities_tuple + online_events_tuples
    return cities_and_online_tuple


def get_active_members_for_category(category):
    events = Event.objects.filter(category=category)

    members_events_in_category = [event.attendees.all() for event in events]
    if members_events_in_category:
        members_events_in_category = list(members_events_in_category[0])  # get the queryset inside a list

    active_category_members = members_events_in_category

    return active_category_members

