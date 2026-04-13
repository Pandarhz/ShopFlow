# app/services/stock.py
import redis
from app.models import Product
from app.cache import redis_client # à mocker dans les tests

def verifier_stock(product: Product, quantite: int) -> bool:
    """Vérifie si le stock est suffisant pour la quantité demandée."""
    return product.stock >= quantite
def reserver_stock(product: Product, quantite: int, session) -> Product:
    """Réserve du stock et invalide le cache Redis."""
    if not verifier_stock(product, quantite):
        raise ValueError(f'Stock insuffisant : {product.stock} disponible(s)') 
    product.stock -= quantite
    session.commit()
    redis_client.delete(f'product:{product.id}:stock') # invalide cache
    return product

def liberer_stock(product: Product, quantite: int, session) -> Product:
    """Libère du stock (annulation commande) et met à jour le cache."""
    product.stock += quantite
    session.commit()
    redis_client.set(f'product:{product.id}:stock', product.stock)
    return product