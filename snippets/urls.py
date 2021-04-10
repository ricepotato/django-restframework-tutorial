from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views


router = DefaultRouter()
router.register("snippets", views.SnippetViewSet)
urlpatterns = [path("", include(router.urls))]

"""urlpatterns = [
    path("", views.api_root),
    path("snippets/", views.SnippetListGeneric.as_view(), name="snippet-list"),
    path(
        "snippets/<int:pk>", views.SnippetDetailGeneric.as_view(), name="snippet-detail"
    ),
    path(
        "snippets/<int:pk>/highlight/",
        views.SnippetHighlight.as_view(),
        name="snippet-highlight",
    ),
]"""

# urlpatterns = format_suffix_patterns(urlpatterns)
