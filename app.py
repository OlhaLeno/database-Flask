from flask import Flask
from __init__ import create_app
from my_project.auth.route.bus_routes import bus_bp
from my_project.auth.route.route_routes import route_bp
from my_project.auth.route.route_stop_routes import route_stop_bp
from my_project.auth.route.stop_routes import stop_bp
from my_project.auth.route.driver_routes import driver_bp
app = create_app()

app.register_blueprint(bus_bp)
app.register_blueprint(driver_bp)
app.register_blueprint(route_bp)
app.register_blueprint(route_stop_bp)
app.register_blueprint(stop_bp)

if __name__ == '__main__':
    app.run(debug=False)
