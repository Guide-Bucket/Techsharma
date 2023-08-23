from django.contrib.sitemaps import Sitemap
from django.urls import reverse

# from website.models import Content


class StaticSitemap(Sitemap):
    """Reverse 'static' views for XML sitemap."""
    changefreq = "daily"
    priority = 0.5

    def items(self):
        # Return list of url names for views to include in sitemap
        return [ 'about', 'notfound', 'career', 'service',
                'servicedetails', 'teamdetails', 'faq', 'saveinfo',
                'saveemail', 'webdevelopement', 'app', 'cloudcomputing', 'itmanaged',
                'softwaredevelopment', 'seo',]

    def location(self, item):
        return reverse(item)

# class DynamicSitemap(Sitemap):     this will use when we have blogs in site
#     changefreq = "daily"
#     priority = 0.5

#     def items(self):
#         return Content.objects.all()
