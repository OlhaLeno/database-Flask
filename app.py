from flask import Flask
from flask import Flask, jsonify
from sqlalchemy.exc import OperationalError
from __init__ import create_app
from my_project.auth.route.bus_routes import bus_bp
from my_project.auth.route.route_routes import route_bp
from my_project.auth.route.route_stop_routes import route_stop_bp
from my_project.auth.route.stop_routes import stop_bp
from my_project.auth.route.driver_routes import driver_bp
from my_project.auth.route.bus_inspection_route import inspection_bp
from my_project.auth.route.stats_route import stats_bp
app = create_app()

app.register_blueprint(bus_bp)
app.register_blueprint(driver_bp)
app.register_blueprint(route_bp)
app.register_blueprint(route_stop_bp)
app.register_blueprint(stop_bp)
app.register_blueprint(inspection_bp)
app.register_blueprint(stats_bp)

@app.errorhandler(OperationalError)
def handle_sql_error(error):
    # Перевірка на конкретну помилку тригера
    if 'Inserting rows into stop is not allowed' in str(error):
        return jsonify({"error": "Inserting rows into stop is not allowed"}), 403
    elif 'Updating rows in stop is not allowed' in str(error):
        return jsonify({"error": "Updating rows in stop is not allowed"}), 403
    elif 'Deleting rows from stop is not allowed' in str(error):
        return jsonify({"error": "Deleting rows from stop is not allowed"}), 403
    else:
        # Для інших помилок SQL
        return jsonify({"error": "Database error"}), 500
if __name__ == '__main__':
    app.run(debug=True)
