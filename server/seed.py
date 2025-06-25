from server.app import app
from server.models import db
from server.models.user import User
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance
from datetime import date
from werkzeug.security import generate_password_hash

with app.app_context():
    print("🧹 Clearing existing data...")
    db.session.query(Appearance).delete()
    db.session.query(Guest).delete()
    db.session.query(Episode).delete()
    db.session.query(User).delete()

    print("🌱 Seeding users...")
    user1 = User(username="admin", password_hash=generate_password_hash("password123"))
    user2 = User(username="producer", password_hash=generate_password_hash("letmein456"))
    db.session.add_all([user1, user2])

    print("🌱 Seeding guests...")
    g1 = Guest(name="Emma Stone", occupation="Actor")
    g2 = Guest(name="Bill Nye", occupation="Scientist")
    g3 = Guest(name="Adele", occupation="Musician")
    g4 = Guest(name="Trevor Noah", occupation="Comedian")
    g5 = Guest(name="Zendaya", occupation="Actor")
    g6 = Guest(name="Malala Yousafzai", occupation="Activist")
    db.session.add_all([g1, g2, g3, g4, g5, g6])

    print("🌱 Seeding episodes...")
    e1 = Episode(date=date(2025, 1, 10), number=1)
    e2 = Episode(date=date(2025, 1, 17), number=2)
    e3 = Episode(date=date(2025, 1, 24), number=3)
    e4 = Episode(date=date(2025, 1, 31), number=4)
    e5 = Episode(date=date(2025, 2, 7),  number=5)
    db.session.add_all([e1, e2, e3, e4, e5])

    print("🌱 Seeding appearances...")
    a1 = Appearance(guest=g1, episode=e1, rating=5)
    a2 = Appearance(guest=g2, episode=e2, rating=4)
    a3 = Appearance(guest=g3, episode=e4, rating=5)
    a4 = Appearance(guest=g4, episode=e3, rating=3)
    a5 = Appearance(guest=g5, episode=e1, rating=4)
    a6 = Appearance(guest=g3, episode=e1, rating=5)
    a7 = Appearance(guest=g6, episode=e5, rating=5)
    db.session.add_all([a1, a2, a3, a4, a5, a6, a7])

    db.session.commit()
    print("✅ Done seeding!")

