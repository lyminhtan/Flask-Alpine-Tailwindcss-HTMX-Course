from .urls import bp


# Create your views here.
@bp.route("/", endpoint="test", methods=["GET"])
def index():
    return "<h1>Hello world</h1>"
