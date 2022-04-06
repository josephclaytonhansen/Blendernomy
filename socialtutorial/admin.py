from django.contrib import admin
from django.contrib.auth.models import Group, User
# Register your models here.

from.models import Author, Article, FeaturedVideo, Tag, CTA, Banner, DigitalProduct, ProductKey, SheepFrame, SuperTag
class AuthorInline(admin.StackedInline):
    model = Author

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username", "email", "first_name", "is_staff", "is_active"]
    inlines = [AuthorInline]

@admin.action(description='Publish')    
def publish(modeladmin, request, queryset):
    queryset.update(published=True)
    
@admin.action(description='Un-publish')    
def unpublish(modeladmin, request, queryset):
    queryset.update(published=False)
    
@admin.action(description='Feature (home page)')    
def feature_home(modeladmin, request, queryset):
    queryset.update(featured_on_home_page=True)

@admin.action(description='Unfeature')    
def unfeature(modeladmin, request, queryset):
    queryset.update(featured_on_tag_page=False)
    queryset.update(featured_on_home_page=False)

class ArticleAdmin(admin.ModelAdmin):
    model = Article
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'featured_on_home_page', 'cta', 'published', "slug", "views")
    list_editable = ('featured_on_home_page', 'published')
    list_display_links = ('title',)
    def get_changeform_initial_data(self, request):
        return {'user': User.objects.all()[0]}
    actions = [publish, unpublish, feature_home, unfeature]

class CtaAdmin(admin.ModelAdmin):
    model = CTA
    list_display = ('title', 'location', 'published',)
    list_editable=('published',)
    list_display_links=('title',)
    actions = [publish, unpublish]

class TagAdmin(admin.ModelAdmin):
    model = Tag
    list_display = ('tag','display',)
    list_editable = ('display',)
    list_display_links = ('tag',)
    
class SuperTagAdmin(admin.ModelAdmin):
    model = SuperTag
    list_display = ('tag','display',)
    list_editable = ('display',)
    list_display_links = ('tag',)

class BannerAdmin(admin.ModelAdmin):
    model = Banner
    list_display = ('title','published',)
    list_editable = ('published',)
    list_display_links = ('title',)

class FramesAdmin(admin.ModelAdmin):
    model = SheepFrame

class FVideoAdmin(admin.ModelAdmin):
    model = FeaturedVideo

class KeyInline(admin.StackedInline):
    model = ProductKey

class ProductAdmin(admin.ModelAdmin):
    model = DigitalProduct
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'published', 'sales', 'onsale', 'rating', 'price')
    list_editable = ('onsale', 'price', 'published')
    list_display_links = ('title',)
    actions = [publish, unpublish] 
    inlines = [KeyInline] 

class KeyAdmin(admin.ModelAdmin):
    model = ProductKey 
    prepopulated_fields = {"slug": ("key",)}
    
admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(DigitalProduct, ProductAdmin)
admin.site.register(ProductKey, KeyAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(SuperTag, SuperTagAdmin)
admin.site.register(CTA, CtaAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(SheepFrame, FramesAdmin)
admin.site.register(FeaturedVideo, FVideoAdmin)