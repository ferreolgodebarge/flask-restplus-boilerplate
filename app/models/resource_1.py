from models import db


class Resource_1(db.Model):
    uuid = db.Column(db.String(80), primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return "<uuid: {}, name: {}, description: {}>".format(
            self.uuid, self.name, self.description
        )

    def to_dict(self):
        return {
            "id": self.uuid,
            "name": self.name,
            "description": self.description
        }
