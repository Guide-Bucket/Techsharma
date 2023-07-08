from meta.views import Meta
from .models import SeoModel

def getMeta(path):
    try:
        meta = SeoModel.objects.get(url=path)
    except:
        return ''
    return Meta(
    title=meta.title,
    description=meta.description,
    keywords=meta.keywords.split(","),
    extra_props = meta.extra_props,
    extra_custom_props=[(x.split(",")) for x in meta.extra_custom_props.split(":")],
    url=meta.url,
    locale=meta.locale
    )
