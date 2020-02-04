from flask import escape, request, Blueprint, render_template
import constants as CONSTANTS

portfolio_routes = Blueprint('portfolio_routes', __name__)

# Get home page for portfolio
@portfolio_routes.route('/', methods=['GET'])
def index():
    return render_template('index.html', name=CONSTANTS.PORTFOLIO_NAME, title=CONSTANTS.PORTFOLIO_TITLE,
                           description=CONSTANTS.PORTFOLIO_DESCRIPTION)
