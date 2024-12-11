from django.contrib import admin

from theProject2.criminals.models import CriminalMainInfo


@admin.register(CriminalMainInfo)
class CriminalMainInfoAdmin(admin.ModelAdmin):
    # 1. List Display: Show these fields in the list view
    list_display = ('id', 'first_name', 'last_name', 'prison', 'is_approved')

    # 2. Filters: Add sidebar filters
    list_filter = ('is_approved', 'prison__security_level')

    # 3. Search Fields: Enable searching
    search_fields = ('first_name', 'last_name')

    # 4. Default Ordering: Sort records by approval status first, then last name
    ordering = ('-is_approved', 'last_name')

    # 5. Custom Actions: Add an action to mark criminals as approved
    @admin.action(description="Mark selected criminals as approved")
    def mark_as_approved(self, request, queryset):
        queryset.update(is_approved=True)

    actions = [mark_as_approved]  # Attach the custom action
