from django.core.urlresolvers import reverse
from django.db import models
from djorm_pgfulltext.fields import VectorField
from djorm_pgfulltext.models import SearchManager


class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(null=True, blank=True)

    search_index = VectorField()

    objects = SearchManager(
        fields=('name',),
        config='pg_catalog.english',
        search_field='search_index',
        auto_update_search_field=True
    )

    def __str__(self):
        return self.name


class Quotation(models.Model):
    author = models.ForeignKey(Author, related_name='underquoted')
    text = models.CharField(max_length=500, unique=True)

    search_index = VectorField()

    objects = SearchManager(
        fields=('text',),
        config='pg_catalog.english',
        search_field='search_index',
        auto_update_search_field=True
    )

    def __str__(self):
        return "%s - %s" % (self.text, self.author.name)

    def get_absolute_url(self):
        return reverse('show_quotation', args=[self.pk])
