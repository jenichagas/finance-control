from bson import ObjectId

def serialize_category(cat):
    return {
        "id": str(cat["_id"]),
        "name": cat["name"],
        "slug": cat["slug"],
        "color": cat["color"],
    }
