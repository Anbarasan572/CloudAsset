from flask import Blueprint, request, jsonify

from database.db import db
from models.asset_model import Asset


asset_bp = Blueprint("asset", __name__)


# GET all assets
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


# GET single asset
@asset_bp.route("/assets/<int:asset_id>", methods=["GET"])
def get_asset(asset_id):

    asset = Asset.query.get(asset_id)

    if not asset:
        return jsonify({
            "message": "Asset not found"
        }), 404

    return jsonify({
        "id": asset.id,
        "asset_name": asset.asset_name,
        "provider": asset.provider,
        "service": asset.service,
        "region": asset.region,
        "status": asset.status,
        "owner": asset.owner
    })


# POST - Add new asset
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
    }), 200


# PUT - Update asset
@asset_bp.route("/assets/<int:asset_id>", methods=["PUT"])
def update_asset(asset_id):

    asset = Asset.query.get(asset_id)

    if not asset:
        return jsonify({
            "message": "Asset not found"
        }), 404

    data = request.json

    asset.asset_name = data.get("asset_name", asset.asset_name)
    asset.provider = data.get("provider", asset.provider)
    asset.service = data.get("service", asset.service)
    asset.region = data.get("region", asset.region)
    asset.status = data.get("status", asset.status)
    asset.owner = data.get("owner", asset.owner)

    db.session.commit()

    return jsonify({
        "message": "Asset updated successfully"
    })


# DELETE - Delete asset
@asset_bp.route("/assets/<int:asset_id>", methods=["DELETE"])
def delete_asset(asset_id):

    asset = Asset.query.get(asset_id)

    if not asset:
        return jsonify({
            "message": "Asset not found"
        }), 404

    db.session.delete(asset)
    db.session.commit()

    return jsonify({
        "message": "Asset deleted successfully"
    })