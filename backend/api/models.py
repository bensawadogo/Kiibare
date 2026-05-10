from django.db import models
import uuid

class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    risk_profile = models.CharField(max_length=50, choices=[
        ('LOW', 'Faible'), ('MEDIUM', 'Moyen'), ('HIGH', 'Élevé')
    ], default='LOW')
    experience_level = models.CharField(max_length=50, choices=[
        ('BEGINNER', 'Débutant'), ('INTERMEDIATE', 'Intermédiaire'), ('ADVANCED', 'Avancé')
    ], default='BEGINNER')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class BrokerRecommendation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    broker_name = models.CharField(max_length=100)
    suitability_score = models.FloatField(help_text="Score de pertinence sur 10")
    # Dans la vraie vie, on utiliserait un ArrayField (PostgreSQL) ou un JSONField
    payment_methods = models.JSONField(default=list, help_text="Ex: ['Mobile Money', 'Bank Transfer']")

    def __str__(self):
        return f"{self.broker_name} (Score: {self.suitability_score})"

class AssetOpportunity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    asset_type = models.CharField(max_length=50, choices=[
        ('BRVM_STOCK', 'Action BRVM'), 
        ('UEMOA_BOND', 'Obligation UEMOA')
    ])
    confidence_score = models.FloatField(help_text="Confiance de l'IA sur cette opportunité")
    risk_level = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Opportunité {self.asset_type} - Risque {self.risk_level}"
