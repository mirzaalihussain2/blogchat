from app.extensions import db
from app.models import Character, Blog
from app import create_app

def seed_database():
    try:
        app = create_app()
        with app.app_context():
            # Check if characters already exist
            if Character.query.count() == 0:
                # Create sample characters
                character1 = Character(
                    name="Paul Graham",
                    description="Co-founder of Y Combinator",
                    source_url="http://paulgraham.com"
                )
                character2 = Character(
                    name="Naval Ravikant",
                    description="AngelList founder",
                    source_url="https://nav.al"
                )

                # Add to database
                db.session.add_all([character1, character2])
                db.session.commit()
                print("Database seeded successfully!")
            else:
                print("Database already contains characters. Skipping seed.")
    except Exception as e:
        print(f"Error seeding database: {str(e)}")
        db.session.rollback()

if __name__ == '__main__':
    seed_database()