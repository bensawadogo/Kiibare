"""
Pydantic schemas for Django Ninja API serialization.
These schemas define the shape of data going in and out of the API.
"""
from ninja import Schema
from uuid import UUID
from datetime import datetime
from typing import Optional


# ============================================================
# UserProfile Schemas
# ============================================================
class UserProfileIn(Schema):
    email: str
    risk_profile: str = "LOW"
    experience_level: str = "BEGINNER"


class UserProfileOut(Schema):
    id: UUID
    email: str
    risk_profile: str
    experience_level: str
    created_at: datetime


# ============================================================
# BrokerRecommendation Schemas
# ============================================================
class BrokerRecommendationOut(Schema):
    id: UUID
    broker_name: str
    suitability_score: float
    payment_methods: list


# ============================================================
# AssetOpportunity Schemas
# ============================================================
class AssetOpportunityOut(Schema):
    id: UUID
    asset_type: str
    confidence_score: float
    risk_level: str


# ============================================================
# Generic Schemas
# ============================================================
class MessageOut(Schema):
    message: str


class ErrorOut(Schema):
    detail: str
