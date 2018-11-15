"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def sandbox_Yoshida(request):
    """Renders the sandbox page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/sandbox_Yoshida.html',
        {
            'title':'SandBox',
            'message':'It\'s a sandbox of Yoshida.',
            'year':datetime.now().year,
        }
    )

def sandbox_Toyosato(request):
    """Renders the sandbox page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/sandbox_Toyosato.html',
        {
            'title':'SandBox',
            'message':'It\'s a sandbox of Toyosato.',
            'year':datetime.now().year,
        }
    )

def sandbox_Mizuno(request):
    """Renders the sandbox page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/sandbox_Mizuno.html',
        {
            'title':'SandBox',
            'message':'It\'s a sandbox of Mizuno.',
            'year':datetime.now().year,
        }
    )

def sandbox_Ueda(request):
    """Renders the sandbox page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/sandbox_Ueda.html',
        {
            'title':'SandBox',
            'message':'It\'s a sandbox of Ueda.',
            'year':datetime.now().year,
        }
    )