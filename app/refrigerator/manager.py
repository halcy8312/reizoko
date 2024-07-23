from app import db

class RefrigeratorItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    count = db.Column(db.Integer, nullable=False, default=1)

class RefrigeratorManager:
    def __init__(self, db):
        self.db = db

    def add_item(self, item):
        existing_item = RefrigeratorItem.query.filter_by(name=item).first()
        if existing_item:
            existing_item.count += 1
        else:
            new_item = RefrigeratorItem(name=item, count=1)
            db.session.add(new_item)
        db.session.commit()

    def remove_item(self, item):
        existing_item = RefrigeratorItem.query.filter_by(name=item).first()
        if existing_item:
            existing_item.count -= 1
            if existing_item.count <= 0:
                db.session.delete(existing_item)
            db.session.commit()

    def get_contents(self):
        items = RefrigeratorItem.query.all()
        if not items:
            return "冷蔵庫は空です。"
        return [f"{item.name}: {item.count}" for item in items]

    def get_items(self):
        items = RefrigeratorItem.query.all()
        return [item.name for item in items]