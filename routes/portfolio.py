from flask import escape, request, Blueprint

portfolio_routes = Blueprint('portfolio_routes', __name__)

# Get home page for portfolio
@portfolio_routes.route('/', methods=['GET'])
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
