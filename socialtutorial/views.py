from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView, FormView, TemplateView
from django.utils.decorators import method_decorator
from .models import Article, DigitalProduct, Tag, ProductKey, FeaturedVideo, SuperTag
from ratelimit.decorators import ratelimit
from datetime import timedelta
from blacklist.ratelimit import blacklist_ratelimited
from .forms import ContactForm, KeyValidator, frog
from django.urls import reverse_lazy

# Create your views here.
def page_not_found(request, exception):
    return render(request, '404.html', status=404)

@ratelimit(key='ip', rate = '30/m', block=False)
@ratelimit(key='ip', rate = '100/20m', block=False)
@ratelimit(key='ip', rate = '800/d', block=False)
@blacklist_ratelimited(timedelta(minutes=20))
def dashboard(request):
    articles = list(Article.objects.all().filter(published=True).filter(featured_on_home_page=False).order_by('-created_at'))[:4]
    featured_articles = list(Article.objects.all().filter(published=True).filter(featured_on_home_page=True).order_by('-created_at'))[:3]
    return render(request, "index.html",
                  {"articles": articles,
                   "featured1":featured_articles[0],
                   "featured2":featured_articles[1],
                   "featured3":featured_articles[2],
                   "featured_videos":FeaturedVideo.objects.all()[0:2],
                   "tags":list(Tag.objects.all()),
                   "supertags":list(SuperTag.objects.all())}
                  )

@ratelimit(key='ip', rate = '30/m', block=False)
@ratelimit(key='ip', rate = '100/20m', block=False)
@ratelimit(key='ip', rate = '800/d', block=False)
@blacklist_ratelimited(timedelta(minutes=20))
def test(request):
    return render(request, "test.html")

@ratelimit(key='ip', rate = '1/m', block=False)
@ratelimit(key='ip', rate = '10/20m', block=False)
@ratelimit(key='ip', rate = '20/d', block=False)
@blacklist_ratelimited(timedelta(minutes=60))
def old_admin(request):
    return render(request, "404.html")

@method_decorator(ratelimit(key='ip', rate = '30/m', block=False), name="dispatch")
@method_decorator(ratelimit(key='ip', rate = '100/20m', block=False), name="dispatch")
@method_decorator(ratelimit(key='ip', rate = '800/d', block=False), name="dispatch")
@method_decorator(blacklist_ratelimited(timedelta(minutes=20)), name="dispatch")  
class ArticleList(ListView):
    model = Article
    template_name = "article_list.html"
    def get_ordering(self):
        ordering = self.request.GET.get('ordering', '-created_at')
        # validate ordering here
        return ordering
    paginate_by = 6
    orphans = 3
    

@ratelimit(key='ip', rate = '30/m', block=False)
@ratelimit(key='ip', rate = '100/20m', block=False)
@ratelimit(key='ip', rate = '800/d', block=False)
@blacklist_ratelimited(timedelta(minutes=20))
def article_random(request):
    import random
    articles = list(Article.objects.all().filter(published=True))
    article = random.choice(articles)
    return render(request, "article_random.html", {"object": article})

@method_decorator(ratelimit(key='ip', rate = '30/m', block=False), name="dispatch")
@method_decorator(ratelimit(key='ip', rate = '100/20m', block=False), name="dispatch")
@method_decorator(ratelimit(key='ip', rate = '800/d', block=False), name="dispatch")
@method_decorator(blacklist_ratelimited(timedelta(minutes=20)), name="dispatch")
class ArticleView(DetailView):
    model = Article
    template_name = "single_article.html"

@method_decorator(ratelimit(key='ip', rate = '30/m', block=False), name="dispatch")
@method_decorator(ratelimit(key='ip', rate = '100/20m', block=False), name="dispatch")
@method_decorator(ratelimit(key='ip', rate = '800/d', block=False), name="dispatch")
@method_decorator(blacklist_ratelimited(timedelta(minutes=20)), name="dispatch")     
class ProductView(DetailView):
    model = DigitalProduct
    template_name = "product.html"
    

@method_decorator(ratelimit(key='ip', rate = '30/m', block=False), name="dispatch")
@method_decorator(ratelimit(key='ip', rate = '100/20m', block=False), name="dispatch")
@method_decorator(ratelimit(key='ip', rate = '800/d', block=False), name="dispatch")
@method_decorator(blacklist_ratelimited(timedelta(minutes=20)), name="dispatch")   
class TagView(DetailView):
    model = Tag
    template_name = "category.html"
    def get_context_data(self, **kwargs):
        context = super(TagView, self).get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(tags=self.object)
        context['products'] = DigitalProduct.objects.filter(tags=self.object)
        context['object'] = self.object
        return context
    
@method_decorator(ratelimit(key='ip', rate = '30/m', block=False), name="dispatch")
@method_decorator(ratelimit(key='ip', rate = '100/20m', block=False), name="dispatch")
@method_decorator(ratelimit(key='ip', rate = '800/d', block=False), name="dispatch")
@method_decorator(blacklist_ratelimited(timedelta(minutes=20)), name="dispatch")   
class SuperTagView(DetailView):
    model = SuperTag
    template_name = "category.html"
    def get_context_data(self, **kwargs):
        context = super(SuperTagView, self).get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(supertags=self.object)
        context['object'] = self.object
        return context

@method_decorator(ratelimit(key='ip', rate = '30/m', block=False), name="dispatch")
@method_decorator(ratelimit(key='ip', rate = '100/20m', block=False), name="dispatch")
@method_decorator(ratelimit(key='ip', rate = '800/d', block=False), name="dispatch")
@method_decorator(blacklist_ratelimited(timedelta(minutes=20)), name="dispatch") 
class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('socialtutorial:success')

    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)

@method_decorator(ratelimit(key='ip', rate = '30/m', block=False), name="dispatch")
@method_decorator(ratelimit(key='ip', rate = '100/20m', block=False), name="dispatch")
@method_decorator(ratelimit(key='ip', rate = '800/d', block=False), name="dispatch")
@method_decorator(blacklist_ratelimited(timedelta(minutes=20)), name="dispatch")  
class ContactSuccessView(TemplateView):
    template_name = 'contact_success.html'
    

def KeyValidatorView(request):
    form = KeyValidator(request.POST or None)
    if request.method == "POST" and form.is_valid():
        email = form.cleaned_data['email']
        try:
            k = ProductKey.objects.get(email__exact=email)
            return render(request, 'key_validated.html', {"key" : k})
        except:
            return render(request, 'key_validator.html', {'form':form, "errors":'no key'})
    else:
        form = KeyValidator()
        return render(request, 'key_validator.html', {'form':form})
    

def PurchaseView(request, slug):
    form = KeyValidator(request.POST or None)
    if request.method == "POST" and form.is_valid():
        email = form.cleaned_data['email']
        try:
            k = ProductKey.objects.get(email__exact=email)
            if frog(email) == slug:
                return render(request, "view_purchase.html", {"key" : k})
            else:
                return render(request, 'key_validator.html', {'form':form, "errors":'wrong key'})
        except Exception as e:
            return render(request, 'key_validator.html', {'form':form, "errors":'no key'})
    else:
        form = KeyValidator()
        return render(request, 'key_validator.html', {'form':form})