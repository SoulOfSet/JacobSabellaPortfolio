from flask import Flask

from routes.portfolio import portfolio_routes

app = Flask(__name__)
app.register_blueprint(portfolio_routes, url_prefix='/portfolio')

# Start App
if __name__ == "__main__":
    app.run()


