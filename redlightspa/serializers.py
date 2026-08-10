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
        fields = "__all__"


class HeroSlideSerializer(serializers.ModelSerializer):
    background_image = serializers.ImageField(required=False, allow_null=True)
    main_image = serializers.ImageField(required=False, allow_null=True)
    shape_image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = HeroSlide
        fields = "__all__"


class BrandLogoSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = BrandLogo
        fields = "__all__"


class AboutSectionSerializer(serializers.ModelSerializer):
    main_image = serializers.ImageField(required=False, allow_null=True)
    side_image = serializers.ImageField(required=False, allow_null=True)
    feature_1_icon = serializers.ImageField(required=False, allow_null=True)
    feature_2_icon = serializers.ImageField(required=False, allow_null=True)
    feature_3_icon = serializers.ImageField(required=False, allow_null=True)
    video_url = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    class Meta:
        model = AboutSection
        fields = "__all__"


class ServiceSectionSerializer(serializers.ModelSerializer):
    icon_image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = ServiceSection
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    icon = serializers.ImageField(required=False, allow_null=True)
    background_image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Service
        fields = "__all__"


class MarqueeItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarqueeItem
        fields = "__all__"


class VideoSectionSerializer(serializers.ModelSerializer):
    background_image = serializers.ImageField(required=False, allow_null=True)
    video_url = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    class Meta:
        model = VideoSection
        fields = "__all__"


class GalleryItemSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = GalleryItem
        fields = "__all__"


class PricingSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingSection
        fields = "__all__"


class PricingPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingPlan
        fields = "__all__"


class TestimonialSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Testimonial
        fields = "__all__"


class TeamMemberSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = TeamMember
        fields = "__all__"


class InstagramSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstagramSection
        fields = "__all__"


class InstagramImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = InstagramImage
        fields = "__all__"


class BlogSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogSection
        fields = "__all__"


class BlogPostSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = BlogPost
        fields = "__all__"


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
    category = serializers.PrimaryKeyRelatedField(
        queryset=ServiceCategory.objects.all(), required=False, allow_null=True
    )

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

    def to_internal_value(self, data):
        if not ServiceCategory.objects.exists():
            ServiceCategory.objects.create(name="General Services", order=1)

        cat_id = data.get("category")
        if not cat_id or not ServiceCategory.objects.filter(id=cat_id).exists():
            default_cat = ServiceCategory.objects.first()
            if default_cat:
                if hasattr(data, "_mutable") and not data._mutable:
                    data = data.copy()
                else:
                    try:
                        data = data.copy()
                    except Exception:
                        pass
                data["category"] = default_cat.id

        return super().to_internal_value(data)



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
    button_url = serializers.CharField(required=False, allow_blank=True, default="")

    class Meta:
        model = HomeSection
        fields = "__all__"


# Serializer
class DynamicPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DynamicPage
        fields = "__all__"
