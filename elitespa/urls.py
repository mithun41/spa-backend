from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from elitespa import views

router = DefaultRouter()
router.register(r"site-config", SiteConfigViewSet)
router.register(r"hero-slides", HeroSlideViewSet)
router.register(r"brand-logos", BrandLogoViewSet)
router.register(r"about-sections", AboutSectionViewSet)
router.register(r"service-sections", ServiceSectionViewSet)  # এখন আর 404 হবে না
router.register(r"services", ServiceViewSet)  # এখন আর 404 হবে nich
router.register(r"marquee-items", MarqueeItemViewSet)
router.register(r"video-sections", VideoSectionViewSet)
router.register(r"gallery-items", GalleryItemViewSet)
router.register(r"pricing-sections", PricingSectionViewSet)
router.register(r"pricing-plans", PricingPlanViewSet)
router.register(r"testimonials", TestimonialViewSet)
router.register(r"team-members", TeamMemberViewSet)
router.register(r"instagram-sections", InstagramSectionViewSet)
router.register(r"instagram-images", InstagramImageViewSet)
router.register(r"blog-sections", BlogSectionViewSet)
router.register(r"blog-posts", BlogPostViewSet)
router.register(r"blog-pages", BlogPageViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"comments", BlogCommentViewSet)
router.register(r"gallery", GalleryViewSet, basename="gallery")
router.register(r"home-sections", HomeSectionViewSet)
router.register(r"service-items", ServiceItemViewSet, basename="serviceitem")
router.register(r"pages", DynamicPageViewSet, basename="dynamic-page")

urlpatterns = [
    path("homepage/", homepage_view, name="homepage"),
    # path('services/', views.services_page_view, name='services-page'),
    path("", include(router.urls)),
    
]
