from flask import Blueprint, request
import stripe
from os import getenv

stripe_routes = Blueprint("stripe_routes", __name__)

@stripe_routes.route("/")
def main():
    return "Hola"


@stripe_routes.route("/payment/card", methods = ["POST"] )
def payment():
    try:
        data = request.json
        stripe.Charge.create(
        amount=data['amount'],
        currency="usd",
        description=data['description'],
        source="tok_visa",  # obtained with Stripe.js
        idempotency_key=data['id'],
        api_key=getenv("SECRET_KEY")
    )
    except Exception as e:
        return e
    return "RECIBIDO"