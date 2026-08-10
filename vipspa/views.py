from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .permissions import IsVipSpaAdmin
from redlightspa.models import Gallery
from redlightspa.serializers import GallerySerializer

from .models import (
    BlogComment,
    BlogPage,
    Category,
    DynamicPage,
    HomeSection,
    ServiceItem,
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
    BlogPageSerializer,
    CategorySerializer,
    BlogCommentSerializer,
    DynamicPageSerializer,
    HomeSectionSerializer,
    ServiceItemSerializer,
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


class HeroSlideViewSet(viewsets.ModelViewSet):
    queryset = HeroSlide.objects.all().order_by("order")
    serializer_class = HeroSlideSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class BrandLogoViewSet(viewsets.ModelViewSet):
    queryset = BrandLogo.objects.all().order_by("order")
    serializer_class = BrandLogoSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class AboutSectionViewSet(viewsets.ModelViewSet):
    queryset = AboutSection.objects.all()
    serializer_class = AboutSectionSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class ServiceSectionViewSet(viewsets.ModelViewSet):  # এইটা আপনার মিসিং ছিল
    queryset = ServiceSection.objects.all()
    serializer_class = ServiceSectionSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all().order_by("order")
    serializer_class = ServiceSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class MarqueeItemViewSet(viewsets.ModelViewSet):
    queryset = MarqueeItem.objects.all().order_by("order")
    serializer_class = MarqueeItemSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class VideoSectionViewSet(viewsets.ModelViewSet):
    queryset = VideoSection.objects.all()
    serializer_class = VideoSectionSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class GalleryItemViewSet(viewsets.ModelViewSet):
    queryset = GalleryItem.objects.all().order_by("order")
    serializer_class = GalleryItemSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class PricingSectionViewSet(viewsets.ModelViewSet):
    queryset = PricingSection.objects.all()
    serializer_class = PricingSectionSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class PricingPlanViewSet(viewsets.ModelViewSet):
    queryset = PricingPlan.objects.all().order_by("order")
    serializer_class = PricingPlanSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all().order_by("order")
    serializer_class = TestimonialSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all().order_by("order")
    serializer_class = TeamMemberSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class InstagramSectionViewSet(viewsets.ModelViewSet):
    queryset = InstagramSection.objects.all()
    serializer_class = InstagramSectionSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class InstagramImageViewSet(viewsets.ModelViewSet):
    queryset = InstagramImage.objects.all().order_by("order")
    serializer_class = InstagramImageSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class BlogSectionViewSet(viewsets.ModelViewSet):
    queryset = BlogSection.objects.all()
    serializer_class = BlogSectionSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all().order_by("-id")
    serializer_class = BlogPostSerializer
    permission_classes = [
        permissions.AllowAny
    ]


# --- ২. আপনার মেইন GET API (ফ্রন্টএন্ড হোমপেজের জন্য) ---


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
    if not hero_slides.exists():
        hero_slides = HeroSlide.objects.all().order_by("order")
    brand_logos = BrandLogo.objects.filter(is_active=True).order_by("order")
    services = Service.objects.filter(is_active=True).order_by("order")
    marquee_items = MarqueeItem.objects.filter(is_active=True).order_by("order")
    gallery_items = GalleryItem.objects.filter(is_active=True).order_by("order")
    pricing_plans = PricingPlan.objects.filter(is_active=True).order_by("order")
    testimonials = Testimonial.objects.filter(is_active=True).order_by("order")
    team_members = TeamMember.objects.filter(is_active=True).order_by("order")
    instagram_images = InstagramImage.objects.filter(is_active=True).order_by("order")
    blog_posts = BlogPost.objects.filter(is_active=True).order_by("order")
    home_sections = HomeSection.objects.all()

    data = {
        "site_config": (
            SiteConfigSerializer(site_config, context={"request": request}).data
            if site_config
            else {}
        ),
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
        "about": (
            AboutSectionSerializer(about_section, context={"request": request}).data
            if about_section
            else {}
        ),
        "services": {
            "section_info": (
                ServiceSectionSerializer(
                    service_section, context={"request": request}
                ).data
                if service_section
                else {}
            ),
            "items": ServiceSerializer(
                services, many=True, context={"request": request}
            ).data,
        },
        "marquee": {
            "items": MarqueeItemSerializer(
                marquee_items, many=True, context={"request": request}
            ).data
        },
        "video": (
            VideoSectionSerializer(video_section, context={"request": request}).data
            if video_section
            else {}
        ),
        "gallery": {
            "items": GalleryItemSerializer(
                gallery_items, many=True, context={"request": request}
            ).data
        },
        "pricing": {
            "section_info": (
                PricingSectionSerializer(
                    pricing_section, context={"request": request}
                ).data
                if pricing_section
                else {}
            ),
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
            "section_info": (
                InstagramSectionSerializer(
                    instagram_section, context={"request": request}
                ).data
                if instagram_section
                else {}
            ),
            "items": InstagramImageSerializer(
                instagram_images, many=True, context={"request": request}
            ).data,
        },
        "blog": {
            "section_info": (
                BlogSectionSerializer(blog_section, context={"request": request}).data
                if blog_section
                else {}
            ),
            "posts": BlogPostSerializer(
                blog_posts, many=True, context={"request": request}
            ).data,
        },
        "home_sections": {
            "items": HomeSectionSerializer(
                home_sections, many=True, context={"request": request}
            ).data
        },
    }

    return Response(data)


class SiteConfigViewSet(viewsets.ModelViewSet):
    queryset = SiteConfig.objects.all()
    serializer_class = SiteConfigSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


class BlogPageViewSet(viewsets.ModelViewSet):
    queryset = BlogPage.objects.all().order_by("-created_at")
    serializer_class = BlogPageSerializer
    permission_classes = [
        permissions.AllowAny
    ]
    lookup_field = "slug"  # Fetch by slug for SEO-friendly URLs

    def get_permissions(self):
        # Public can see the blogs, but only Admin can Create/Update/Delete
        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def get_permissions(self):
        # যে কেউ ক্যাটাগরি দেখতে পারবে (list/retrieve)
        # কিন্তু Create/Update/Delete করতে হলে লগইন করা লাগবে
        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


class BlogCommentViewSet(viewsets.ModelViewSet):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def get_permissions(self):
        if self.action == "create":  # যে কেউ কমেন্ট করতে পারবে
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]  # শুধু এডমিন ডিলিট/এডিট করতে পারবে


class GalleryViewSet(viewsets.ModelViewSet):
    serializer_class = GallerySerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def get_queryset(self):
        return Gallery.objects.filter(site="vipspa").order_by("-uploaded_at")

    def perform_create(self, serializer):
        serializer.save(site="vipspa")  # সেভ করার সময় অটো vipspa ট্যাগ পড়বে


class HomeSectionViewSet(viewsets.ModelViewSet):
    queryset = HomeSection.objects.all()
    serializer_class = HomeSectionSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class ServiceItemViewSet(viewsets.ModelViewSet):
    queryset = ServiceItem.objects.all()
    serializer_class = ServiceItemSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def get_queryset(self):
        queryset = ServiceItem.objects.all()
        # যদি URL-এ ?homepage=true থাকে তবে শুধু হোমপেজের গুলো দেখাবে
        homepage = self.request.query_params.get("homepage")
        if homepage == "true":
            queryset = queryset.filter(show_on_homepage=True)

        # যদি শুধু একটি নির্দিষ্ট ক্যাটেগরি ফিল্টার করতে চান
        category_id = self.request.query_params.get("category")
        if category_id:
            queryset = queryset.filter(category_id=category_id)

        return queryset.filter(is_active=True)


class DynamicPageViewSet(viewsets.ModelViewSet):
    queryset = DynamicPage.objects.all()
    serializer_class = DynamicPageSerializer
    permission_classes = [
        permissions.AllowAny
    ]
    lookup_field = "slug"  # এইটা মাস্ট, যাতে আইডি'র বদলে স্লাগ দিয়ে এডিট করা যায়
