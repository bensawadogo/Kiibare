"""
Kiibare API — Main router with all endpoints.
Documentation auto-generated at /api/docs
"""
from ninja import NinjaAPI
from typing import List
from django.shortcuts import get_object_or_404

from .models import UserProfile, BrokerRecommendation, AssetOpportunity
from .schemas import (
    UserProfileIn, UserProfileOut,
    BrokerRecommendationOut,
    AssetOpportunityOut,
    MessageOut, ErrorOut,
)

api = NinjaAPI(
    title="Kiibare API",
    description="API for Africa Market Access Intelligence — Courtiers, Opportunités, Profils investisseurs.",
    version="1.0.0",
)


# ============================================================
# Health Check
# ============================================================
@api.get("/health", response=MessageOut, tags=["System"])
def health_check(request):
    """Vérification rapide que l'API est en ligne."""
    return {"message": "Kiibare API is running smoothly!"}


# ============================================================
# User Profiles
# ============================================================
@api.post("/profiles", response={201: UserProfileOut}, tags=["Profiles"])
def create_profile(request, payload: UserProfileIn):
    """Créer un nouveau profil investisseur."""
    profile = UserProfile.objects.create(**payload.dict())
    return 201, profile


@api.get("/profiles", response=List[UserProfileOut], tags=["Profiles"])
def list_profiles(request):
    """Lister tous les profils investisseurs."""
    return list(UserProfile.objects.all())


@api.get("/profiles/{profile_id}", response=UserProfileOut, tags=["Profiles"])
def get_profile(request, profile_id: str):
    """Récupérer un profil investisseur par ID."""
    profile = get_object_or_404(UserProfile, id=profile_id)
    return profile


# ============================================================
# Broker Recommendations
# ============================================================
@api.get("/brokers", response=List[BrokerRecommendationOut], tags=["Brokers"])
def list_brokers(request):
    """Lister toutes les recommandations de courtiers."""
    return list(BrokerRecommendation.objects.all())


@api.get("/brokers/top", response=List[BrokerRecommendationOut], tags=["Brokers"])
def top_brokers(request, limit: int = 5):
    """Récupérer les courtiers les mieux notés."""
    return list(
        BrokerRecommendation.objects.order_by('-suitability_score')[:limit]
    )


# ============================================================
# Asset Opportunities
# ============================================================
@api.get("/opportunities", response=List[AssetOpportunityOut], tags=["Opportunities"])
def list_opportunities(request):
    """Lister toutes les opportunités d'investissement détectées."""
    return list(AssetOpportunity.objects.all())


@api.get("/opportunities/high-confidence", response=List[AssetOpportunityOut], tags=["Opportunities"])
def high_confidence_opportunities(request, min_score: float = 7.0):
    """Filtrer les opportunités à haute confiance IA."""
    return list(
        AssetOpportunity.objects.filter(confidence_score__gte=min_score)
        .order_by('-confidence_score')
    )
