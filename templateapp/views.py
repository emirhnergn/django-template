from django.shortcuts import render, get_object_or_404, redirect
from models import TextModel
from forms import AddCommentForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.views import View
from django.contrib import messages
import logging

def home(request):
    query = request.GET.get('search')
    texts = TextModel.objects.order_by('-id')
    if query:
        texts = texts.filter(
            Q(title__icontains=query) | 
            Q(text__icontains=query)
        ).distinct()
    page = request.GET.get('page')
    paginator = Paginator(texts, 2)
    
    context = {
        "texts" : paginator.get_page(page)
    }
    
    return render(request, 'pages/home.html', context = context)

logger = logging.getLogger('article_read')
class DetailView(View):
    http_method_names = ['get', 'post']
    add_comment_form = AddCommentForm
    def get(self,request,slug):
        text = get_object_or_404(TextModel, slug=slug)
        
        if request.user.is_authenticated:
            logger.info(f'"{request.user.username}" -> read: "{text.title}"')
            
        comments = text.comments.all()
        context = {
            'text':text, 
            'comments':comments,
            'form' : self.add_comment_form()
        }
        return render(request, 'pages/detail.html', context=context)
    def post(self,request,slug):
        text = get_object_or_404(TextModel, slug=slug)
        add_comment_form = self.add_comment_form(request.POST)
        if add_comment_form.is_valid() and request.user:
            comment = add_comment_form.save(commit=False)
            comment.writer = request.user
            comment.text = text
            comment.save()
            messages.success(request, 'Comment shared successfully')
        return redirect('detail', slug=slug)

