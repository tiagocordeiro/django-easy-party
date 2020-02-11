from datetime import date

from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory, Client
from django.urls import reverse

from invitation.models import Invite
from invitation.views import invite_download_jpg


class InvitationTestCase(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.client = Client()

        # Staff user
        self.user_staff = User.objects.create_user(username='jacob', email='jacob@…', password='top_secret')

        self.invite_brian = Invite.objects.create(name='Brian', age=12, gender=1, date=date.today(), start_time='18:00',
                                                  end_time='21:00', maximum_guests=33)

    def test_view_for_invites_list_with_non_logged_user(self):
        self.client.logout()
        request = self.client.get(reverse('invites_list'))

        self.assertEqual(request.status_code, 302)
        self.assertRedirects(request,
                             '/accounts/login/?next=/invites/',
                             status_code=302,
                             target_status_code=200)

    def test_view_for_invites_list_with_logged_user(self):
        self.client.force_login(self.user_staff)
        request = self.client.get(reverse('invites_list'))

        self.assertEqual(request.status_code, 200)

    def test_invite_download_view_status_code(self):
        self.client.logout()
        request = self.client.get(reverse('invite_download_jpg', args={self.invite_brian.pk}))

        response = invite_download_jpg(request, pk=self.invite_brian.pk)
        self.assertEqual(response.status_code, 200)
