from app.extensions import db
from app.models import Character, Blog
from app import create_app

app = create_app()
with app.app_context():
    # Create sample characters
    character1 = Character(name="Paul Graham", description="Co-founder of Y Combinator", source_url="http://paulgraham.com")
    character2 = Character(name="Naval Ravikant", description="AngelList founder", source_url="https://nav.al")

    # Add to database
    db.session.add_all([character1, character2])
    db.session.commit()
    print("Database seeded!")