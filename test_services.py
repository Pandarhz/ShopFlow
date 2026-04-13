# Tester pricing.py directement depuis le terminal Python
from app.services.pricing import calcul_prix_ttc, appliquer_coupon, calculer_total

from app.models import Coupon
print(calcul_prix_ttc(100.0)) # attendu : 120.0
print(calcul_prix_ttc(0.0)) # attendu : 0.0
coupon = Coupon(code='PROMO20', reduction=20.0, actif=True)
print(appliquer_coupon(120.0, coupon)) # attendu : 96.0
# calculer_total avec liste vide
print(calculer_total([])) # attendu : 0.0