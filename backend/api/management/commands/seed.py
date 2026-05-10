"""
Seed command — Populates the database with initial demo data.
Usage: python manage.py seed
"""
from django.core.management.base import BaseCommand
from api.models import BrokerRecommendation, AssetOpportunity


class Command(BaseCommand):
    help = 'Insère des données de démonstration dans la base de données'

    def handle(self, *args, **options):
        self.stdout.write('🌱 Seeding de la base de données Kiibare...')

        # --- Courtiers ---
        brokers_data = [
            {
                "broker_name": "Coris Bourse",
                "suitability_score": 8.5,
                "payment_methods": ["Mobile Money", "Virement Bancaire"],
            },
            {
                "broker_name": "SGI Abidjan",
                "suitability_score": 7.8,
                "payment_methods": ["Virement Bancaire", "Chèque"],
            },
            {
                "broker_name": "BOA Capital",
                "suitability_score": 9.1,
                "payment_methods": ["Mobile Money", "Virement Bancaire", "Carte Visa"],
            },
            {
                "broker_name": "Ecobank Invest",
                "suitability_score": 8.0,
                "payment_methods": ["Mobile Money", "Virement Bancaire"],
            },
            {
                "broker_name": "BNI Finances",
                "suitability_score": 7.2,
                "payment_methods": ["Virement Bancaire"],
            },
        ]

        for data in brokers_data:
            BrokerRecommendation.objects.get_or_create(
                broker_name=data["broker_name"],
                defaults=data,
            )
        self.stdout.write(self.style.SUCCESS(f'  ✅ {len(brokers_data)} courtiers créés'))

        # --- Opportunités ---
        opportunities_data = [
            {
                "asset_type": "BRVM_STOCK",
                "confidence_score": 8.7,
                "risk_level": "MEDIUM",
            },
            {
                "asset_type": "UEMOA_BOND",
                "confidence_score": 9.2,
                "risk_level": "LOW",
            },
            {
                "asset_type": "BRVM_STOCK",
                "confidence_score": 6.5,
                "risk_level": "HIGH",
            },
            {
                "asset_type": "UEMOA_BOND",
                "confidence_score": 8.0,
                "risk_level": "LOW",
            },
        ]

        for data in opportunities_data:
            AssetOpportunity.objects.get_or_create(
                asset_type=data["asset_type"],
                confidence_score=data["confidence_score"],
                defaults=data,
            )
        self.stdout.write(self.style.SUCCESS(f'  ✅ {len(opportunities_data)} opportunités créées'))

        self.stdout.write(self.style.SUCCESS('🎉 Seeding terminé avec succès !'))
