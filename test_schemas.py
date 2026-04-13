from app.schemas import ProductCreate, CouponCreate

# Valide
p = ProductCreate(name='Laptop', price=999.99, stock=10)
print('Produit valide:', p)

# Coupon avec code en minuscules → automatiquement en majuscules
c = CouponCreate(code='promo20', reduction=20.0)
print('Code coupon:', c.code)  # doit afficher PROMO20

# Test de validation : prix négatif doit échouer
try:
    ProductCreate(name='X', price=-5.0, stock=1)
except Exception as e:
    print('Validation OK — prix négatif rejeté:', type(e).__name__)
