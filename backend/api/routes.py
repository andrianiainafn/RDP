from flask import Blueprint, abort, request


api_bp = Blueprint("api", __name__, url_prefix="/api")


@api_bp.get("/marking")
def get_marking():
    # Endpoint réservé: non implémenté volontairement (application vide)
    abort(501)


@api_bp.post("/fire")
def fire_transition():
    # Endpoint réservé: non implémenté volontairement (application vide)
    _ = request.args.get("transition")  # placeholder pour signature
    abort(501)


