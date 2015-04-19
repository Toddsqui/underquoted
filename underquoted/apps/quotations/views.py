from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from underquoted.apps.quotations import models as q_models
from underquoted.libs import query_set


def redirect_to_random(request):
    quotations = query_set.get_random(q_models.Quotation.objects.all())
    return redirect(quotations[0])


def list_quotations(request):
    search_text = request.GET.get('search_text', '').strip()
    quotations = q_models.Quotation.objects.all()
    if search_text:
        quotation_ids = quotations.search(search_text).values_list('id', flat=True)
        authors = q_models.Author.objects.search(search_text)
        quotations = quotations.filter(Q(id__in=quotation_ids) | Q(author__in=authors))

    paginator = Paginator(quotations, settings.MAX_PER_PAGE)

    page = request.GET.get('page')
    try:
        quotations = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        quotations = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        quotations = paginator.page(paginator.num_pages)

    return render_to_response('quotations/show.html',
                              {'quotations': quotations,
                               'pages': [i for i in range(1, paginator.num_pages+1)],
                               'search_text': search_text},
                              context_instance=RequestContext(request))


def show_quotation(request, pk):
    quotations = q_models.Quotation.objects.filter(pk=pk)
    return render_to_response('quotations/show.html',
                              {'quotations': quotations,
                               'pages': [1]},
                              context_instance=RequestContext(request))
