
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('super/admin/', admin.site.urls),
    path("",include("core.urls")),
    path("blog/",include("blog.urls")),
    path("contact/",include("contact.urls")),
    path("booking/",include("booking.urls")),
    path("restaurant/",include("restaurant.urls")),
    path("rooms/",include("rooms.urls")),
    path("auth/",include("users.urls")),
    path("owner/",include("owner.urls")),
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



