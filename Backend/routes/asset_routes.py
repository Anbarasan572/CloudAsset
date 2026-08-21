from flask import Blueprint, request, jsonify

from database.db import db
from models.asset_model import Asset


asset_bp = Blueprint("asset", __name__)


# Get all assets
@asset_bp.route("/assets", methods=["GET"])
def get_assets():

    assets = Asset.query.all()

    result = []

    for asset in assets:
        result.append({
            "id": asset.id,
            "asset_name": asset.asset_name,
            "provider": asset.provider,
            "service": asset.service,
            "region": asset.region,
            "status": asset.status,
            "owner": asset.owner
        })

    return jsonify(result)



# Add new asset
@asset_bp.route("/assets", methods=["POST"])
def add_asset():

    data = request.json

    new_asset = Asset(
        asset_name=data["asset_name"],
        provider=data["provider"],
        service=data["service"],
        region=data["region"],
        status=data["status"],
        owner=data["owner"]
    )

    db.session.add(new_asset)
    db.session.commit()

    return jsonify({
        "message": "Asset added successfully"
    })