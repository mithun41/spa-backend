from django.contrib import admin

from vipspa.views import BlogPageViewSet
from .models import (
    BlogPage,
    Category,
    Gallery,
    ServiceCategory,
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
from vipspa import models


from django.contrib import admin
from .models import SiteConfig


@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    # list_display মানে এডমিন লিস্টে কোন কোন কলাম দেখা যাবে
    list_display = ("site_name", "phone_number", "email", "updated_at")

    # চাইলে এখানে এডিট করার সুবিধাও দিতে পারেন
    list_editable = ("phone_number", "email")


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


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)

@admin.register(ServiceItem) # এখানে ServiceItem হবে
class ServiceItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'service_type', 'show_on_homepage', 'is_active', 'order')
    list_editable = ('service_type', 'show_on_homepage', 'is_active', 'order')
    list_filter = ('service_type', 'category', 'show_on_homepage', 'is_active')


from .models import Category, BlogComment, BlogPage  


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(BlogComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "blog", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name", "message")


# এখানে ভুল ছিল, BlogPageViewSet এর বদলে BlogPage হবে
@admin.register(BlogPage)
class BlogPageAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "author", "created_at")
    list_filter = ("category", "created_at")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    # অ্যাডমিন প্যানেলের লিস্টে যা যা দেখাবে
    list_display = ("id", "thumbnail", "title", "uploaded_at")
    readonly_fields = ("uploaded_at", "thumbnail")

    # অ্যাডমিন প্যানেলে ছবির প্রিভিউ দেখার জন্য একটি ফাংশন
    def thumbnail(self, obj):
        from django.utils.html import format_html

        if obj.image:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 5px;" />',
                obj.image.url,
            )
        return "No Image"

    thumbnail.short_description = "Preview"
