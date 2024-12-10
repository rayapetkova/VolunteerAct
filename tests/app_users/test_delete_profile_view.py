from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import TestCase
from django.urls import reverse

AppUser = get_user_model()


class TestDeleteProfileView(TestCase):
    def setUp(self):
        regular_users_group = Group.objects.create(name='regular_users')

        self.user = AppUser.objects.create_user(
            email='test_user@email.com',
            password='Test123!!TT'
        )
        self.user.groups.add(regular_users_group)

        self.client.login(
            email='test_user@email.com',
            password='Test123!!TT'
        )

    def test_delete_profile_author__success(self):
        self.assertTrue(AppUser.objects.filter(pk=self.user.id).exists())

        response = self.client.post(
            reverse('delete-profile')
        )

        self.assertFalse(AppUser.objects.filter(pk=self.user.id).exists())

    def test_delete_profile_anonymous_user__error(self):
        self.client.logout()

        response = self.client.post(
            reverse('delete-profile')
        )

        self.assertEquals(response.status_code, 404)
