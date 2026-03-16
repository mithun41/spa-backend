from django.contrib import admin
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


@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    list_display = ("site_name", "phone_number", "email", "updated_at")


@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active")
    list_editable = ("order", "is_active")


@admin.register(BrandLogo)
class BrandLogoAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "is_active")
    list_editable = ("order", "is_active")


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ("title", "updated_at")


@admin.register(ServiceSection)
class ServiceSectionAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active")
    list_editable = ("order", "is_active")


@admin.register(MarqueeItem)
class MarqueeItemAdmin(admin.ModelAdmin):
    list_display = ("text", "order", "is_active")
    list_editable = ("order", "is_active")


@admin.register(VideoSection)
class VideoSectionAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "is_active")
    list_editable = ("order", "is_active")


@admin.register(PricingSection)
class PricingSectionAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(PricingPlan)
class PricingPlanAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "order", "is_active")
    list_editable = ("order", "is_active")


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "designation", "rating", "order", "is_active")
    list_editable = ("order", "is_active")


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "designation", "order", "is_active")
    list_editable = ("order", "is_active")


@admin.register(InstagramSection)
class InstagramSectionAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(InstagramImage)
class InstagramImageAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "is_active")
    list_editable = ("order", "is_active")


@admin.register(BlogSection)
class BlogSectionAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "order", "is_active")
    list_editable = ("order", "is_active")