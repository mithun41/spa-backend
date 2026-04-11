from rest_framework import serializers, viewsets
from .models import (
    BlogComment,
    BlogPage,
    Category,
    DynamicPage,
    Gallery,
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


class SiteConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteConfig
        fields = [
            "site_name",
            "logo",
            "phone_number",
            "address",
            "email",
        ]


class HeroSlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSlide
        fields = [
            "id",
            "stroke_text",
            "subtitle",
            "title",
            "description",
            "background_image",
            "main_image",
            "shape_image",
            "button_text",
            "button_link",
            "order",
        ]


class BrandLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandLogo
        fields = [
            "id",
            "image",
            "link",
            "order",
        ]


class AboutSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutSection
        fields = [
            "subtitle",
            "title",
            "description",
            "main_image",
            "side_image",
            "feature_1",
            "feature_1_icon",
            "feature_2",
            "feature_2_icon",
            "feature_3",
            "feature_3_icon",
            "button_text",
            "button_link",
            "contact_label",
            "contact_value",
            "video_url",
        ]


class ServiceSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceSection
        fields = [
            "id",
            "subtitle",
            "title",
            "description",
            "icon_image",
        ]


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = "__all__"


class MarqueeItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarqueeItem
        fields = [
            "id",
            "text",
            "order",
        ]


class VideoSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoSection
        fields = [
            "title",
            "button_text",
            "button_link",
            "video_url",
            "background_image",
        ]


class GalleryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryItem
        fields = [
            "id",
            "image",
            "view_link",
            "order",
        ]


class PricingSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingSection
        fields = [
            "subtitle",
            "title",
        ]


class PricingPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingPlan
        fields = [
            "id",
            "title",
            "session_1",
            "session_2",
            "session_3",
            "price",
            "order",
        ]


class TestimonialSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Testimonial
        fields = "__all__"


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = [
            "id",
            "name",
            "designation",
            "photo",
            "details_link",
            "order",
        ]


class InstagramSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstagramSection
        fields = [
            "title",
        ]


class InstagramImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstagramImage
        fields = [
            "id",
            "image",
            "link",
            "order",
        ]


class BlogSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogSection
        fields = [
            "subtitle",
            "title",
        ]


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = [
            "id",
            "category",
            "date",
            "title",
            "image",
            "details_link",
            "order",
        ]


# Sevice Section এর জন্য Serializer
from rest_framework import serializers
from .models import ServiceItem, ServiceCategory


# ১. ক্যাটাগরি সিরিয়ালাইজার
class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = ["id", "name", "order"]


# ২. সার্ভিস আইটেম সিরিয়ালাইজার (সার্ভিস পেজের জন্য)
class ServiceItemSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source="category.name")

    class Meta:
        model = ServiceItem
        fields = [
            "id",
            "category",
            "category_name",
            "service_type",
            "title",
            "description",
            "icon_image",
            "main_image",
            "price",
            "duration",
            "show_on_homepage",
            "is_active",
            "order",
        ]


# vipspa/serializers.py

from rest_framework import serializers
from .models import SiteConfig


class SiteConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteConfig
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        extra_kwargs = {
            "slug": {"required": False}  # যদি স্লাগ থাকে তবে এটা রিকোয়ার্ড অফ করে দিন
        }


class BlogCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogComment  # এখানে আগে ভুল ছিল
        fields = "__all__"


class BlogPageSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source="category.name")
    comments = BlogCommentSerializer(many=True, read_only=True)
    day = serializers.SerializerMethodField()
    month = serializers.SerializerMethodField()

    class Meta:
        model = BlogPage
        fields = "__all__"

    def get_day(self, obj):
        return obj.created_at.strftime("%d")

    def get_month(self, obj):
        return obj.created_at.strftime("%b")


class GallerySerializer(serializers.ModelSerializer):
    class Meta:  # এখানে Dictionary লেখা ছিল, এটাকে Meta করে দিন
        model = Gallery
        fields = "__all__"


from .models import HomeSection


class HomeSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeSection
        fields = "__all__"


# Serializer
class DynamicPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DynamicPage
        fields = "__all__"
