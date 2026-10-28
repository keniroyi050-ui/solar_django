from django.test import TestCase
from django.urls import reverse

from .models import ContactSubmission


class ContactSubmissionTests(TestCase):
    def test_contact_page_displays_real_submission_form(self):
        response = self.client.get(reverse('contact'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Send Message')
        self.assertNotContains(response, 'Demo:')
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_valid_contact_submission_is_saved(self):
        response = self.client.post(reverse('contact'), {
            'name': 'Ada Lovelace',
            'email': 'ada@example.com',
            'subject': 'Solar installation',
            'message': 'Please contact me about a home system.',
        })

        self.assertRedirects(response, reverse('contact'))
        submission = ContactSubmission.objects.get()
        self.assertEqual(submission.name, 'Ada Lovelace')
        self.assertEqual(submission.email, 'ada@example.com')
        self.assertEqual(submission.subject, 'Solar installation')
        self.assertEqual(submission.message, 'Please contact me about a home system.')

    def test_invalid_contact_submission_is_not_saved(self):
        response = self.client.post(reverse('contact'), {
            'name': 'Ada Lovelace',
            'email': 'not-an-email',
            'subject': 'Solar installation',
            'message': 'Please contact me.',
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(ContactSubmission.objects.count(), 0)
        self.assertContains(response, 'Enter a valid email address.')
