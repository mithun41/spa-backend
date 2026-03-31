from django.db import models


class SiteConfig(models.Model):
    site_name = models.CharField(max_length=200, blank=True)
    logo = models.ImageField(upload_to="site/", blank=True, null=True)
    phone_number = models.CharField(max_length=30, blank=True)
    address = models.TextField(blank=True)
    email = models.EmailField(blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Site Config"
        verbose_name_plural = "Site Config"

    def __str__(self):
        return self.site_name or "Site Config"


class HeroSlide(models.Model):
    stroke_text = models.CharField(max_length=200, blank=True)
    subtitle = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)

    background_image = models.ImageField(upload_to="homepage/hero/", blank=True, null=True)
    main_image = models.ImageField(upload_to="homepage/hero/", blank=True, null=True)
    shape_image = models.ImageField(upload_to="homepage/hero/", blank=True, null=True)

    button_text = models.CharField(max_length=100, blank=True)
    button_link = models.CharField(max_length=255, blank=True)

    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title or f"Hero Slide {self.id}"


class BrandLogo(models.Model):
    image = models.ImageField(upload_to="homepage/brands/")
    link = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"Brand Logo {self.id}"


class AboutSection(models.Model):
    subtitle = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)

    main_image = models.ImageField(upload_to="homepage/about/", blank=True, null=True)
    side_image = models.ImageField(upload_to="homepage/about/", blank=True, null=True)

    feature_1 = models.CharField(max_length=100, blank=True)
    feature_1_icon = models.ImageField(upload_to="homepage/about/features/", blank=True, null=True)

    feature_2 = models.CharField(max_length=100, blank=True)
    feature_2_icon = models.ImageField(upload_to="homepage/about/features/", blank=True, null=True)

    feature_3 = models.CharField(max_length=100, blank=True)
    feature_3_icon = models.ImageField(upload_to="homepage/about/features/", blank=True, null=True)

    button_text = models.CharField(max_length=100, blank=True)
    button_link = models.CharField(max_length=255, blank=True)

    contact_label = models.CharField(max_length=100, blank=True)
    contact_value = models.CharField(max_length=100, blank=True)

    video_url = models.URLField(blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "About Section"
        verbose_name_plural = "About Section"

    def __str__(self):
        return self.title or "About Section"


class ServiceSection(models.Model):
    subtitle = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    icon_image = models.ImageField(upload_to="homepage/services/", blank=True, null=True)

    class Meta:
        verbose_name = "Service Section"
        verbose_name_plural = "Service Section"

    def __str__(self):
        return self.title or "Service Section"


class Service(models.Model):
    title = models.CharField(max_length=200)
    icon = models.ImageField(upload_to="homepage/services/items/", blank=True, null=True)
    background_image = models.ImageField(upload_to="homepage/services/items/", blank=True, null=True)
    details_link = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title


class MarqueeItem(models.Model):
    text = models.CharField(max_length=150)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.text


class VideoSection(models.Model):
    title = models.CharField(max_length=255, blank=True)
    button_text = models.CharField(max_length=100, blank=True)
    button_link = models.CharField(max_length=255, blank=True)
    video_url = models.URLField(blank=True)
    background_image = models.ImageField(upload_to="homepage/video/", blank=True, null=True)

    class Meta:
        verbose_name = "Video Section"
        verbose_name_plural = "Video Section"

    def __str__(self):
        return self.title or "Video Section"


class GalleryItem(models.Model):
    image = models.ImageField(upload_to="homepage/gallery/")
    view_link = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"Gallery Item {self.id}"


class PricingSection(models.Model):
    subtitle = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = "Pricing Section"
        verbose_name_plural = "Pricing Section"

    def __str__(self):
        return self.title or "Pricing Section"


class PricingPlan(models.Model):
    title = models.CharField(max_length=200)
    session_1 = models.CharField(max_length=255, blank=True)
    session_2 = models.CharField(max_length=255, blank=True)
    session_3 = models.CharField(max_length=255, blank=True)
    price = models.CharField(max_length=50, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length=150)
    designation = models.CharField(max_length=150, blank=True)
    comment = models.TextField(blank=True)
    photo = models.ImageField(upload_to="homepage/testimonials/", blank=True, null=True)
    rating = models.PositiveIntegerField(default=5)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    name = models.CharField(max_length=150)
    designation = models.CharField(max_length=150, blank=True)
    photo = models.ImageField(upload_to="homepage/team/", blank=True, null=True)
    details_link = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name


class InstagramSection(models.Model):
    title = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = "Instagram Section"
        verbose_name_plural = "Instagram Section"

    def __str__(self):
        return self.title or "Instagram Section"


class InstagramImage(models.Model):
    image = models.ImageField(upload_to="homepage/instagram/")
    link = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"Instagram Image {self.id}"


class BlogSection(models.Model):
    subtitle = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = "Blog Section"
        verbose_name_plural = "Blog Section"

    def __str__(self):
        return self.title or "Blog Section"


class BlogPost(models.Model):
    category = models.CharField(max_length=100, blank=True)
    date = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="homepage/blogs/", blank=True, null=True)
    details_link = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title
    
# service page এর জন্য নতুন মডেল
from django.db import models


class SiteConfig(models.Model):
    site_name = models.CharField(max_length=200, blank=True)
    logo = models.ImageField(upload_to="site/", blank=True, null=True)
    phone_number = models.CharField(max_length=30, blank=True)
    address = models.TextField(blank=True)
    email = models.EmailField(blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Site Config"
        verbose_name_plural = "Site Config"

    def __str__(self):
        return self.site_name or "Site Config"


class HeroSlide(models.Model):
    stroke_text = models.CharField(max_length=200, blank=True)
    subtitle = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)

    background_image = models.ImageField(upload_to="homepage/hero/", blank=True, null=True)
    main_image = models.ImageField(upload_to="homepage/hero/", blank=True, null=True)
    shape_image = models.ImageField(upload_to="homepage/hero/", blank=True, null=True)

    button_text = models.CharField(max_length=100, blank=True)
    button_link = models.CharField(max_length=255, blank=True)

    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title or f"Hero Slide {self.id}"


class BrandLogo(models.Model):
    image = models.ImageField(upload_to="homepage/brands/")
    link = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"Brand Logo {self.id}"


class AboutSection(models.Model):
    subtitle = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)

    main_image = models.ImageField(upload_to="homepage/about/", blank=True, null=True)
    side_image = models.ImageField(upload_to="homepage/about/", blank=True, null=True)

    feature_1 = models.CharField(max_length=100, blank=True)
    feature_1_icon = models.ImageField(upload_to="homepage/about/features/", blank=True, null=True)

    feature_2 = models.CharField(max_length=100, blank=True)
    feature_2_icon = models.ImageField(upload_to="homepage/about/features/", blank=True, null=True)

    feature_3 = models.CharField(max_length=100, blank=True)
    feature_3_icon = models.ImageField(upload_to="homepage/about/features/", blank=True, null=True)

    button_text = models.CharField(max_length=100, blank=True)
    button_link = models.CharField(max_length=255, blank=True)

    contact_label = models.CharField(max_length=100, blank=True)
    contact_value = models.CharField(max_length=100, blank=True)

    video_url = models.URLField(blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "About Section"
        verbose_name_plural = "About Section"

    def __str__(self):
        return self.title or "About Section"


class ServiceSection(models.Model):
    subtitle = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    icon_image = models.ImageField(upload_to="homepage/services/", blank=True, null=True)

    class Meta:
        verbose_name = "Service Section"
        verbose_name_plural = "Service Section"

    def __str__(self):
        return self.title or "Service Section"


class Service(models.Model):
    title = models.CharField(max_length=200)
    icon = models.ImageField(upload_to="homepage/services/items/", blank=True, null=True)
    background_image = models.ImageField(upload_to="homepage/services/items/", blank=True, null=True)
    details_link = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title


class MarqueeItem(models.Model):
    text = models.CharField(max_length=150)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.text


class VideoSection(models.Model):
    title = models.CharField(max_length=255, blank=True)
    button_text = models.CharField(max_length=100, blank=True)
    button_link = models.CharField(max_length=255, blank=True)
    video_url = models.URLField(blank=True)
    background_image = models.ImageField(upload_to="homepage/video/", blank=True, null=True)

    class Meta:
        verbose_name = "Video Section"
        verbose_name_plural = "Video Section"

    def __str__(self):
        return self.title or "Video Section"


class GalleryItem(models.Model):
    image = models.ImageField(upload_to="homepage/gallery/")
    view_link = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"Gallery Item {self.id}"


class PricingSection(models.Model):
    subtitle = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = "Pricing Section"
        verbose_name_plural = "Pricing Section"

    def __str__(self):
        return self.title or "Pricing Section"


class PricingPlan(models.Model):
    title = models.CharField(max_length=200)
    session_1 = models.CharField(max_length=255, blank=True)
    session_2 = models.CharField(max_length=255, blank=True)
    session_3 = models.CharField(max_length=255, blank=True)
    price = models.CharField(max_length=50, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length=150)
    designation = models.CharField(max_length=150, blank=True)
    comment = models.TextField(blank=True)
    photo = models.ImageField(upload_to="homepage/testimonials/", blank=True, null=True)
    rating = models.PositiveIntegerField(default=5)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    name = models.CharField(max_length=150)
    designation = models.CharField(max_length=150, blank=True)
    photo = models.ImageField(upload_to="homepage/team/", blank=True, null=True)
    details_link = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name


class InstagramSection(models.Model):
    title = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = "Instagram Section"
        verbose_name_plural = "Instagram Section"

    def __str__(self):
        return self.title or "Instagram Section"


class InstagramImage(models.Model):
    image = models.ImageField(upload_to="homepage/instagram/")
    link = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"Instagram Image {self.id}"


class BlogSection(models.Model):
    subtitle = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = "Blog Section"
        verbose_name_plural = "Blog Section"

    def __str__(self):
        return self.title or "Blog Section"


class BlogPost(models.Model):
    category = models.CharField(max_length=100, blank=True)
    date = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="homepage/blogs/", blank=True, null=True)
    details_link = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title
    
# service page এর জন্য নতুন মডেল
from django.db import models

# --- Service Page এর জন্য নতুন মডেল (নাম বদলে ServiceItem করা হয়েছে যেন ডুপ্লিকেট না হয়) ---

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Service Categories"

    def __str__(self): 
        return self.name

class ServiceItem(models.Model): # নাম Service থেকে ServiceItem করা হলো
    SERVICE_TYPE_CHOICES = [
        ('general', 'General Service (Section 1)'),
        ('top', 'Top Service (Section 3)'),
    ]

    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='services')
    service_type = models.CharField(max_length=10, choices=SERVICE_TYPE_CHOICES, default='general')
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon_image = models.FileField(upload_to='services/icons/', help_text="SVG preferred", null=True, blank=True)
    main_image = models.ImageField(upload_to='services/main/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    duration = models.CharField(max_length=50, blank=True)
    
    show_on_homepage = models.BooleanField(default=False) # এই ফিল্ডটি এখানে যোগ করা হলো
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self): 
        return self.title