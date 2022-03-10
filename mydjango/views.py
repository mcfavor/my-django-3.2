"""
To render html pages
"""
import random   
from django.http import HttpResponse

from django.template.loader import render_to_string
from articles.models import Article

def home_view(request, *args, **kwargs):
    """
    Take in a request (django sends in request)
    Return HTML as a response
    """
    random_id = random.randint(1, 4) #pseudo random
    article_obj = Article.objects.get(id=random_id)
    article_queryset = Article.objects.all()
    
    context = {

        "object_list": article_queryset,
        "object": article_obj,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content
    }

    #Templates
    HTML_STRING = render_to_string("home-view.html", context=context)
    #HTML_STRING = """
    #<h1>{title} (id: {id})!</h1>
    #<p>{content}!</p>
    #""".format(**context)
     
    return HttpResponse(HTML_STRING)