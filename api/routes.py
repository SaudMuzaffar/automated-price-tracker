from flask import request
from flask_restx import Namespace, Resource, fields
from database.database import get_all_products, get_price_history, insert_product

api = Namespace("products", description="Product related operations")

# Define models for Swagger docs
product_model = api.model("Product", {
    "name": fields.String(required=True, description="Product name"),
    "url": fields.String(required=True, description="Product URL")
})

price_model = api.model("PriceEntry", {
    "price": fields.Float,
    "date_checked": fields.String
})

product_detail_model = api.model("ProductWithHistory", {
    "product_id": fields.Integer,
    "name": fields.String,
    "price_history": fields.List(fields.Nested(price_model))
})


@api.route("")
class ProductList(Resource):
    @api.doc("list_all_products")
    def get(self):
        """List all products"""
        products = get_all_products()
        return {"products": products}, 200

    @api.expect(product_model)
    @api.doc("add_new_product")
    def post(self):
        """Add a new product"""
        data = request.get_json()
        name = data.get("name")
        url = data.get("url")

        if not name or not url:
            return {"error": "Both 'name' and 'url' are required"}, 400

        product_id = insert_product(name, url)
        if not product_id:
            return {"message": "Product already exists"}, 200

        return {
            "message": "Product added successfully",
            "product_id": product_id
        }, 201


@api.route("/<int:product_id>")
@api.param("product_id", "The product ID")
class ProductDetails(Resource):
    @api.marshal_with(product_detail_model)
    def get(self, product_id):
        """Get product details and price history"""
        products = get_all_products()
        product = next((p for p in products if p["product_id"] == product_id), None)
        if not product:
            api.abort(404, "Product not found")

        history = get_price_history(product_id)
        price_history = [
            {
                "price": float(h["price"]),
                "date_checked": h["date_checked"].isoformat()
            }
            for h in history
        ]
        return {
            "product_id": product["product_id"],
            "name": product["name"],
            "price_history": price_history
        }
