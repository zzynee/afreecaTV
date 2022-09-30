from django.shortcuts import render
from django.views.generic import *
from django.views.generic.dates import *
from blog.models import Post
from django.db.models import Q
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin
from blog.templates.blog.forms import PostSearchForm

# Create your views here.
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 10

class PostDV(DetailView):
    model = Post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}"
        context['disqus_id'] = f"post-{self.object.id}-{self.object.slug}"
        context['disqus_url'] = f"{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}"
        context['disqus_title'] = f'{self.object.slug}'
        return context

class PostLV(ListView, FormView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 10
    form_class = PostSearchForm

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        if searchWord == " " :
            post_list = Post.objects.all()
        else :
            post_list = Post.objects.filter(Q(title__icontains = searchWord) |
                                            Q(description__icontains = searchWord) |
                                            Q(content__icontains = searchWord)).distinct()
        context = {'form' : form,
                   'search_term' : searchWord,
                   'posts' : post_list,
                   }
        
        return render(self.request, self.template_name, context)
    
class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_dt'

class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_dt'
    make_object_list = True
    # month_format = '%d' # 디폴트 값
    
class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_dt'
    month_format = '%m'

class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_dt'
    month_format = '%m'

class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_dt'

class TagCloudTV(TemplateView):
    template_name = 'taggit/taggit_cloud.html'
    
class TaggedObjectLV(ListView):
    model = Post
    template_name = 'taggit/taggit_post_list.html'
    
    def get_queryset(self):
        return Post.objects.filter(tags__name = self.kwargs.get('tag'))
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context
    
class SearchFV(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'
    
    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        post_list = Post.objects.filter(Q(title__icontains = searchWord)|
                                        Q(description__icontains = searchWord)|
                                        Q(content__icontains = searchWord)).distinct()
        context = {'form' : form,
                   'search_term' : searchWord,
                   'object_list' : post_list
                   }
        return render(self.request, self.template_name,context)
    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','slug','description','content','tags']
    initial = {'slug' : '자동으로-완성되니-적지마세요'}
    success_url = reverse_lazy('blog:index')
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
        
class PostChangeLV(LoginRequiredMixin,ListView):
    template_name = 'blog/post_change_list.html'
    
    def get_queryset(self):
        return Post.objects.filter(owner = self.request.user)
    
class PostUpdateView(OwnerOnlyMixin, UpdateView):
    model = Post
    fields=['title','slug','description','content','tags']
    success_url = reverse_lazy('blog:index')
    
class PostDeleteView(OwnerOnlyMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:index')