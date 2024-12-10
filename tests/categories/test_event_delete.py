from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import TestCase
from django.urls import reverse

from VolunteerAct.categories.models import Event, Category
from decouple import config

AppUser = get_user_model()


class TestEventDelete(TestCase):
    def setUp(self):
        regular_users_group = Group.objects.create(name='regular_users')
        staff_members_group = Group.objects.create(name='staff_members')

        self.user = AppUser.objects.create_user(
            email='test_user@email.com',
            password='Test123!!TT'
        )
        self.user.groups.add(regular_users_group)

        self.staff_user = AppUser.objects.create_user(
            email='test_user2@email.com',
            password='Test123!!TT'
        )
        self.staff_user.groups.add(staff_members_group)

        self.superuser = AppUser.objects.create_superuser(
            email='test_user3@email.com',
            password='Test123!!TT'
        )

        self.other_user = AppUser.objects.create_user(
            email='test_user4@email.com',
            password='Test123!!TT'
        )

        self.category = Category.objects.create(
            image=config('DEFAULT_PROFILE_IMAGE'),
            poster_img=config('DEFAULT_PROFILE_IMAGE'),
            name='Environment',
            short_description='This is a short description for the Environment category. This is a short description '
                              'for the Environment category.',
            long_description='This is a short description for the Environment category. This is a short description '
                              'for the Environment category. This is a short description for the Environment '
                              'category. This is a short description for the Environment category. This is a short '
                              'description for the Environment category. This is a short description for the '
                              'Environment category.This is a short description for the Environment category. This is '
                             'a short description for the Environment category. This is a short description for the '
                             'Environment category. This is a short description for the Environment category. This is '
                             'a short description for the Environment category. This is a short description for the '
                              'Environment category.'
        )

        self.event = Event.objects.create(
            poster_image=config('DEFAULT_PROFILE_IMAGE'),
            title='Test event',
            details='Test event that needs to have at least 1000 characters. Test event that needs to have at '
                        'least 1000 characters. Test event that needs to have at least 1000 characters. Test event '
                        'that needs to have at least 1000 characters. Test event that needs to have at least 1000 '
                        'characters. Test event that needs to have at least 1000 characters. Test event that needs to '
                        'have at least 1000 characters. Test event that needs to have at least 1000 characters. Test '
                        'event that needs to have at least 1000 characters. Test event that needs to have at least '
                        '1000 characters. Test event that needs to have at least 1000 characters. Test event that '
                        'needs to have at least 1000 characters. Test event that needs to have at least 1000 '
                        'characters. Test event that needs to have at least 1000 characters. Test event that needs to '
                        'have at least 1000 characters. Test event that needs to have at least 1000 characters. Test '
                        'event that needs to have at least 1000 characters. Test event that needs to have at least '
                        '1000 characters. Test event that needs to have at least 1000 characters. Test event that '
                        'needs to have at least 1000 characters.',
            online=False,
            city='Haskovo',
            location='Park Kenana',
            time='2025-02-05 13:00:00',
            host=self.user,
            category=self.category
        )

        self.client.login(
            email='test_user@email.com',
            password='Test123!!TT'
        )

    def test_author_delete_event__success(self):
        self.assertTrue(Event.objects.filter(pk=self.event.id).exists())

        response = self.client.post(
            reverse('event-page', kwargs={
                'categoryId': 1,
                'pk': self.event.id
            })
        )

        self.assertFalse(Event.objects.filter(pk=self.event.id).exists())
        self.assertRedirects(response, reverse('home-page'))

    def test_other_staff_members_delete_event__success(self):
        self.client.login(
            email='test_user2@email.com',
            password='Test123!!TT'
        )

        response = self.client.post(
            reverse('event-page', kwargs={
                'categoryId': 1,
                'pk': self.event.id
            })
        )

        self.assertFalse(Event.objects.filter(pk=self.event.id).exists())
        self.assertRedirects(response, reverse('home-page'))

    def test_superuser_delete_event__success(self):
        self.client.login(
            email='test_user3@email.com',
            password='Test123!!TT'
        )

        response = self.client.post(
            reverse('event-page', kwargs={
                'categoryId': 1,
                'pk': self.event.id
            })
        )

        self.assertFalse(Event.objects.filter(pk=self.event.id).exists())
        self.assertRedirects(response, reverse('home-page'))

    def test_other_user_delete_event__expect_to_not_delete(self):
        self.client.login(
            email='test_user4@email.com',
            password='Test123!!TT'
        )

        response = self.client.post(
            reverse('event-page', kwargs={
                'categoryId': 1,
                'pk': self.event.id
            })
        )

        self.assertTrue(Event.objects.filter(pk=self.event.id).exists())

    def test_anonymous_user_delete_event__expect_to_not_delete(self):
        self.client.logout()

        response = self.client.post(
            reverse('event-page', kwargs={
                'categoryId': 1,
                'pk': self.event.id
            })
        )

        self.assertTrue(Event.objects.filter(pk=self.event.id).exists())
