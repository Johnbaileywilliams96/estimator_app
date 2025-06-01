from django.contrib import admin
from .models import *


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'company_name', 'email_address', 'phone', 'status', 'created_at']
    list_filter = ['status', 'country', 'state', 'created_at']
    search_fields = ['first_name', 'last_name', 'company_name', 'email_address']
    readonly_fields = ['created_at']
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'company_name')
        }),
        ('Contact Information', {
            'fields': ('email_address', 'phone', 'address_1', 'address_2', 'city', 'state', 'zip_code', 'country')
        }),
        ('Project Details', {
            'fields': ('type_of_project', 'references', 'notes', 'status')
        }),
        ('System Information', {
            'fields': ('created_at', 'created_by'),
            'classes': ('collapse',)
        })
    )


@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ['business_name', 'business_email', 'business_phone', 'seats', 'joinable', 'creator_id']
    list_filter = ['joinable', 'seats']
    search_fields = ['business_name', 'business_email']
    filter_horizontal = []


@admin.register(BusinessFiles)
class BusinessFilesAdmin(admin.ModelAdmin):
    list_display = ['business_id', 'file_path', 'field', 'created_at']
    list_filter = ['created_at', 'field']
    search_fields = ['business_id__business_name']
    readonly_fields = ['created_at']


@admin.register(BusinessMember)
class BusinessMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'business_id', 'email', 'phone', 'purchased_seats']
    list_filter = ['business_id', 'purchased_seats']
    search_fields = ['name', 'email', 'business_id__business_name']


@admin.register(BusinessPresetType)
class BusinessPresetTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Standing)
class StandingAdmin(admin.ModelAdmin):
    list_display = ['client', 'name', 'updated_at']
    list_filter = ['updated_at']
    search_fields = ['client__first_name', 'client__last_name', 'name']
    readonly_fields = ['updated_at']


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'client_id', 'status_id', 'total_est', 'business_type_id']
    list_filter = ['status_id', 'business_type_id']
    search_fields = ['title', 'client_id__first_name', 'client_id__last_name', 'client_id__company_name']
    raw_id_fields = ['client_id']  # Better for large datasets
    fieldsets = (
        ('Project Information', {
            'fields': ('title', 'description', 'client_id')
        }),
        ('Status & Budget', {
            'fields': ('status_id', 'total_est', 'business_type_id')
        })
    )


@admin.register(ProjectFiles)
class ProjectFilesAdmin(admin.ModelAdmin):
    list_display = ['project_id', 'file_path', 'created_at']
    list_filter = ['created_at']
    search_fields = ['project_id__title']
    readonly_fields = ['created_at']


@admin.register(ProjectNotes)
class ProjectNotesAdmin(admin.ModelAdmin):
    list_display = ['project_id', 'note_preview', 'created_at']
    list_filter = ['created_at']
    search_fields = ['project_id__title', 'note']
    readonly_fields = ['created_at']
    
    def note_preview(self, obj):
        return obj.note[:50] + "..." if len(obj.note) > 50 else obj.note
    note_preview.short_description = 'Note Preview'


@admin.register(ProjectEmployee)
class ProjectEmployeeAdmin(admin.ModelAdmin):
    list_display = ['business_member_id', 'project_id']
    list_filter = ['project_id']
    search_fields = ['business_member_id__name', 'project_id__title']


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description_preview']
    search_fields = ['name', 'description']
    
    def description_preview(self, obj):
        if obj.description:
            return obj.description[:50] + "..." if len(obj.description) > 50 else obj.description
        return "No description"
    description_preview.short_description = 'Description'


@admin.register(SubLibrary)
class SubLibraryAdmin(admin.ModelAdmin):
    list_display = ['name', 'library_id', 'description_preview']
    list_filter = ['library_id']
    search_fields = ['name', 'library_id__name', 'description']
    
    def description_preview(self, obj):
        if obj.description:
            return obj.description[:50] + "..." if len(obj.description) > 50 else obj.description
        return "No description"
    description_preview.short_description = 'Description'


@admin.register(ItemsServices)
class ItemsServicesAdmin(admin.ModelAdmin):
    list_display = ['name', 'sub_library_id', 'item_pricing_id', 'description_preview']
    list_filter = ['sub_library_id']
    search_fields = ['name', 'sub_library_id__name', 'description']
    
    def description_preview(self, obj):
        if obj.description:
            return obj.description[:50] + "..." if len(obj.description) > 50 else obj.description
        return "No description"
    description_preview.short_description = 'Description'


@admin.register(ProjectItemsServices)
class ProjectItemsServicesAdmin(admin.ModelAdmin):
    list_display = ['project_id', 'items_id', 'material_costs', 'labor_costs', 'total', 'unit_of_measure']
    list_filter = ['unit_of_measure']
    search_fields = ['project_id__title', 'items_id__name']


@admin.register(ItemPricing)
class ItemPricingAdmin(admin.ModelAdmin):
    list_display = ['material', 'labor_costs', 'margin_pct', 'total_price']
    list_filter = []
    search_fields = ['material']


@admin.register(UnitOfMeasure)
class UnitOfMeasureAdmin(admin.ModelAdmin):
    list_display = ['name', 'abbreviation', 'description_preview']
    search_fields = ['name', 'abbreviation']
    
    def description_preview(self, obj):
        if obj.description:
            return obj.description[:50] + "..." if len(obj.description) > 50 else obj.description
        return "No description"
    description_preview.short_description = 'Description'