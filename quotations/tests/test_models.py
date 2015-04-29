from datetime import date

from django import test

from quotations import models as quotation_models


class AuthorTest(test.TestCase):

    def setUp(self):
        self.author = quotation_models.Author(name='Jane',
                                              date_of_birth=date(1950, 1, 3))
        self.author.save()

    def test_str(self):
        self.assertEqual(u'Jane', '%s' % self.author)


class QuotationTest(test.TestCase):

    def setUp(self):
        self.author = quotation_models.Author(name='Emily',
                                              date_of_birth=date(1950, 1, 3))
        self.author.save()
        self.quotation = quotation_models.Quotation(author=self.author, text='hello')
        self.quotation.save()

    def test_str(self):
        self.assertEqual(u'hello - Emily', '%s' % self.quotation)

    def test_get_absolute_url(self):
        self.assertEqual(u'/quotations/%s/' % self.quotation.pk, self.quotation.get_absolute_url())
