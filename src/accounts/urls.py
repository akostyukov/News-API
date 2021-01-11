from django.urls import path, include

accounts_urls = [
    path("auth/", include("dj_rest_auth.urls")),
    path('registration/', include('dj_rest_auth.registration.urls')),
]
