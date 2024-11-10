import os

# Définit les révisions good et bad
good_revision = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"  # Remplace par ton hash "good"
bad_revision = "c1a4be04b972b6c17db242fc37752ad517c29402"  # Remplace par ton hash "bad"

# Commence git bisect avec les révisions good et bad
os.system(f"git bisect start {bad_revision} {good_revision}")

# Lance git bisect avec la commande de test
os.system("git bisect run python manage.py test")
