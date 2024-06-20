from django.contrib import admin
from .models import MyFirstModel, Review, Tag, Certificate

# Register your models here.
admin.site.register(MyFirstModel) # Freelancer
admin.site.register(Review)
admin.site.register(Tag)
admin.site.register(Certificate)

# class ReviewInline(admin.TabularInline):
  # model = Review
  # extra = 2

# class MyFirstModelAdmin(admin.ModelAdmin):
  # list_display = ('name', 'date_added', 'occupation', 'description')
  # inlines = [ReviewInline]

# class TagInline(admin.ModelAdmin):
  # list_display = ('name', 'location', 'freelancers')
  # filter_horizontal = ('freelancers')

# class CertificateAdmin(admin.ModelAdmin):
  # list_display = ('freelancer', 'certificate_name', 'issued_date')
  # filter_horizontal = ('freelancer')

# admin.site.register(MyFirstModel, MyFirstModelAdmin)
# admin.site.register(Tag, TagInline)
# admin.site.register(Certificate, CertificateAdmin)
