from django.contrib import admin

from theProject2.prisons.models import Prison


@admin.register(Prison)
class PrisonAdmin(admin.ModelAdmin):
    # 1. List Display: Show these fields in the list view
    list_display = ('id', 'name', 'security_level', 'capacity')

    # 2. Filters: Add sidebar filters
    list_filter = ('security_level',)

    # 3. Search Fields: Enable searching
    search_fields = ('name', 'security_level')

    # 4. Default Ordering: Sort prisons by security level
    ordering = ('security_level',)

    # 5. Custom Actions: Add an action to flag overcrowded prisons
    @admin.action(description="Flag selected prisons as overcrowded")
    def flag_overcrowded(self, request, queryset):
        queryset.update(is_overcrowded=True)

    actions = [flag_overcrowded]  # Attach the custom action