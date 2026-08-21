from database.db import db


class Asset(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    asset_name = db.Column(
        db.String(100),
        nullable=False
    )

    provider = db.Column(
        db.String(50)
    )

    service = db.Column(
        db.String(50)
    )

    region = db.Column(
        db.String(50)
    )

    status = db.Column(
        db.String(50)
    )

    owner = db.Column(
        db.String(100)
    )