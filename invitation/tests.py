from datetime import date

from django.contrib.auth.models import User, Group
from django.test import RequestFactory, Client, TransactionTestCase
from django.urls import reverse

from invitation.models import Invite, InviteTemplate, InviteCategory


class InvitationTestCase(TransactionTestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.client = Client()

        # Staff user
        self.user_staff = User.objects.create_user(username='jacob',
                                                   email='jacob@…',
                                                   password='top_secret')
        self.group = Group.objects.create(name='Testes')
        self.group.user_set.add(self.user_staff)

        self.invite_category = InviteCategory.objects.create(
            name="Aniversário", description="Categoria para aniversário")

        self.modelo = InviteTemplate.objects.create(
            name="Festa Menino")

        self.invite_brian = Invite.objects.create(name='Brian', age=12,
                                                  date=date.today(),
                                                  start_time='18:00',
                                                  end_time='21:00',
                                                  maximum_guests=33,
                                                  invite_template=self.modelo)

    def test_view_for_invites_list_with_logged_user(self):
        self.client.force_login(self.user_staff)
        request = self.client.get(reverse('invites_list'))

        self.assertEqual(request.status_code, 200)

    def test_view_for_invites_list_with_non_logged_user(self):
        self.client.logout()
        request = self.client.get(reverse('invites_list'))

        self.assertEqual(request.status_code, 302)
        self.assertRedirects(request,
                             '/accounts/login/?next=/invites/',
                             status_code=302,
                             target_status_code=200)

    def test_invite_download_view_status_code(self):
        self.client.logout()
        request = self.client.get(reverse('invite_download_jpg',
                                          kwargs={'pk': self.invite_brian.pk,
                                                  'slug': self.invite_brian.slug}))

        self.assertEqual(request.status_code, 200)

    def test_invite_create_view_with_logged_user(self):
        self.client.force_login(self.user_staff)
        request = self.client.get(reverse('invite_create'))

        self.assertEqual(request.status_code, 200)

    def test_invite_create_view_with_non_logged_user(self):
        self.client.logout()
        request = self.client.get(reverse('invite_create'))

        self.assertEqual(request.status_code, 302)
        self.assertRedirects(request,
                             '/accounts/login/?next=/invite/create/',
                             status_code=302,
                             target_status_code=200)

    def test_invite_create_new(self):
        invites = Invite.objects.all()
        self.assertEqual(len(invites), 1)
        self.assertEqual(Invite.objects.count(), 1)

        new_invite = {
            'name': 'Baby Yoda',
            'age': '104',
            'gender': 1,
            'date': '01/12/2020',
            'start_time': '19:00',
            'end_time': '21:00',
            'maximum_guests': '30',
        }

        self.client.force_login(self.user_staff)

        response = self.client.post(reverse('invite_create'), data=new_invite)
        self.assertEqual(response.status_code, 302)

        invites = Invite.objects.all()
        self.assertEqual(len(invites), 2)
        self.assertEqual(Invite.objects.count(), 2)
