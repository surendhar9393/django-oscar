from django.contrib import admin

from oscar.core.loading import get_model

ProductReview = get_model('reviews', 'ProductReview')
Vote = get_model('reviews', 'Vote')


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'title', 'score', 'status', 'total_votes',
                    'delta_votes', 'date_created')

    def get_readonly_fields(self, request, obj=None):
        read_only_fields = [f.name for f in self.model._meta.fields]
        return read_only_fields


class VoteAdmin(admin.ModelAdmin):
    list_display = ('review', 'user', 'delta', 'date_created')


admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(Vote, VoteAdmin)
