from django.contrib import admin
from .models import UserProfile, BrokerRecommendation, AssetOpportunity


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('email', 'risk_profile', 'experience_level', 'created_at')
    list_filter = ('risk_profile', 'experience_level')
    search_fields = ('email',)
    ordering = ('-created_at',)


@admin.register(BrokerRecommendation)
class BrokerRecommendationAdmin(admin.ModelAdmin):
    list_display = ('broker_name', 'suitability_score')
    list_filter = ('suitability_score',)
    search_fields = ('broker_name',)


@admin.register(AssetOpportunity)
class AssetOpportunityAdmin(admin.ModelAdmin):
    list_display = ('asset_type', 'confidence_score', 'risk_level')
    list_filter = ('asset_type', 'risk_level')
