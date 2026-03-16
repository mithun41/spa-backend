from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import (
    SiteConfig,
    HeroSlide,
    BrandLogo,
    AboutSection,
    ServiceSection,
    Service,
    MarqueeItem,
    VideoSection,
    GalleryItem,
    PricingSection,
    PricingPlan,
    Testimonial,
    TeamMember,
    InstagramSection,
    InstagramImage,
    BlogSection,
    BlogPost,
)

from .serializers import (
    SiteConfigSerializer,
    HeroSlideSerializer,
    BrandLogoSerializer,
    AboutSectionSerializer,
    ServiceSectionSerializer,
    ServiceSerializer,
    MarqueeItemSerializer,
    VideoSectionSerializer,
    GalleryItemSerializer,
    PricingSectionSerializer,
    PricingPlanSerializer,
    TestimonialSerializer,
    TeamMemberSerializer,
    InstagramSectionSerializer,
    InstagramImageSerializer,
    BlogSectionSerializer,
    BlogPostSerializer,
)


@api_view(["GET"])
def homepage_view(request):
    site_config = SiteConfig.objects.first()
    about_section = AboutSection.objects.first()
    service_section = ServiceSection.objects.first()
    video_section = VideoSection.objects.first()
    pricing_section = PricingSection.objects.first()
    instagram_section = InstagramSection.objects.first()
    blog_section = BlogSection.objects.first()

    hero_slides = HeroSlide.objects.filter(is_active=True).order_by("order")
    brand_logos = BrandLogo.objects.filter(is_active=True).order_by("order")
    services = Service.objects.filter(is_active=True).order_by("order")
    marquee_items = MarqueeItem.objects.filter(is_active=True).order_by("order")
    gallery_items = GalleryItem.objects.filter(is_active=True).order_by("order")
    pricing_plans = PricingPlan.objects.filter(is_active=True).order_by("order")
    testimonials = Testimonial.objects.filter(is_active=True).order_by("order")
    team_members = TeamMember.objects.filter(is_active=True).order_by("order")
    instagram_images = InstagramImage.objects.filter(is_active=True).order_by("order")
    blog_posts = BlogPost.objects.filter(is_active=True).order_by("order")

    data = {
        "site_config": SiteConfigSerializer(
            site_config, context={"request": request}
        ).data if site_config else {
            "site_name": "",
            "logo": None,
            "phone_number": "",
            "address": "",
            "email": "",
        },

        "hero": {
            "slides": HeroSlideSerializer(
                hero_slides, many=True, context={"request": request}
            ).data
        },

        "brands": {
            "items": BrandLogoSerializer(
                brand_logos, many=True, context={"request": request}
            ).data
        },

        "about": AboutSectionSerializer(
            about_section, context={"request": request}
        ).data if about_section else {
            "subtitle": "",
            "title": "",
            "description": "",
            "main_image": None,
            "side_image": None,
            "feature_1": "",
            "feature_1_icon": None,
            "feature_2": "",
            "feature_2_icon": None,
            "feature_3": "",
            "feature_3_icon": None,
            "button_text": "",
            "button_link": "",
            "contact_label": "",
            "contact_value": "",
            "video_url": "",
        },

        "services": {
            "section_info": ServiceSectionSerializer(
                service_section, context={"request": request}
            ).data if service_section else {
                "subtitle": "",
                "title": "",
                "description": "",
                "icon_image": None,
            },
            "items": ServiceSerializer(
                services, many=True, context={"request": request}
            ).data,
        },

        "marquee": {
            "items": MarqueeItemSerializer(
                marquee_items, many=True, context={"request": request}
            ).data
        },

        "video": VideoSectionSerializer(
            video_section, context={"request": request}
        ).data if video_section else {
            "title": "",
            "button_text": "",
            "button_link": "",
            "video_url": "",
            "background_image": None,
        },

        "gallery": {
            "items": GalleryItemSerializer(
                gallery_items, many=True, context={"request": request}
            ).data
        },

        "pricing": {
            "section_info": PricingSectionSerializer(
                pricing_section, context={"request": request}
            ).data if pricing_section else {
                "subtitle": "",
                "title": "",
            },
            "plans": PricingPlanSerializer(
                pricing_plans, many=True, context={"request": request}
            ).data,
        },

        "testimonials": {
            "items": TestimonialSerializer(
                testimonials, many=True, context={"request": request}
            ).data
        },

        "team": {
            "items": TeamMemberSerializer(
                team_members, many=True, context={"request": request}
            ).data
        },

        "instagram": {
            "section_info": InstagramSectionSerializer(
                instagram_section, context={"request": request}
            ).data if instagram_section else {
                "title": "",
            },
            "items": InstagramImageSerializer(
                instagram_images, many=True, context={"request": request}
            ).data,
        },

        "blog": {
            "section_info": BlogSectionSerializer(
                blog_section, context={"request": request}
            ).data if blog_section else {
                "subtitle": "",
                "title": "",
            },
            "posts": BlogPostSerializer(
                blog_posts, many=True, context={"request": request}
            ).data,
        },
    }

    return Response(data)