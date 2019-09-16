#!/usr/bin/python3
"""Review objects that handles all default RestFul API actions"""

from models.base_model import BaseModel
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.review import Review
from models.state import State
from models.state import City
from models.place import Place


@app_views.route("/places/<place_id>/reviews", methods=['GET'],
                 strict_slashes=False)
def get_places_reviews(place_id):
    """ Retrieves the list of all review of a place objects """
    place = storage.get('Place', place_id)
    if not place:
        abort(404)
    for value in place.reviews:
        reviews_list.append(value.to_dict())
    return jsonify(places_list)


@app_views.route("/reviews/<review_id>", methods=['GET'], strict_slashes=False)
def get_places_reviews(review_id):
    """ Retrieves a Review object """
    review = storage.get('Review', review_id)
    if review:
        return jsonify(review.to_dict())
    else:
        abort(404)


@app_views.route("/reviews/<review_id>", methods=['DELETE'],
                 strict_slashes=False)
def delete_place_reviews(review_id):
    """ Delete a Review object """
    review = storage.get('Review', review_id)
    if review:
        storage.delete(review)
        storage.save()
        return jsonify({}), 200
    else:
        abort(404)


@app_views.route("/places/<place_id>/reviews", methods=['POST'],
                 strict_slashes=False)
def create_place(place_id):
    """ Creatte a Review object """
    if not request.is_json:
        abort(400, "Not a JSON")
    if 'user_id' not in request.json:
        abort(400, "Missing user_id")
    if 'text' not in request.json:
        abort(400, "Missing text")
    data = request.get_json()
    user_id = datos.get("user_id")
    usuario = storage.get("User", user_id)
    if usuario is None:
        abort(404)
    review = Review(**data)
    review.place_id = place_id
    storage.save()
    respuesta = jsonify(objeto.to_dict())
    respuesta.status_code = 201
    return respuesta


@app_views.route("/reviews/<review_id>", methods=['PUT'], strict_slashes=False)
def update_place_review(review_id):
    """ Update a Review object """
    if not request.is_json:
        abort(400, "Not a JSON")
    review = storage.get('Review', review_id)
    if review:
        data = request.get_json()
        omitir = ['id', 'user_id', 'place_id', 'created_at', 'updated_at']
        for name, value in datos.items():
            if name not in omitir:
                setattr(review, name, value)
        storage.save()
        return jsonify(review.to_dict()), 200
    abort(404)
