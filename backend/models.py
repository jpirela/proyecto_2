from backend.db import db
from datetime import datetime

class DesktopItem(db.Model):
    __tablename__ = "desktop_items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    icon_url = db.Column(db.String(200), nullable=False)
    x = db.Column(db.Integer, default=0)
    y = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "icon_url": self.icon_url,
            "x": self.x,
            "y": self.y
        }
