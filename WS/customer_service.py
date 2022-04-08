from flask import Flask, jsonify
import BAL.customer

def sales_service():

    app = Flask(__name__)
    # app.config["DEBUG"] = True

    @app.route('/v1/customers', methods=['GET'])
    def get_all_sales():
        return jsonify(BAL.customer.get_all_customers())

    @app.route('/v1/customers/<id>', methods=['GET'])
    def get_sale_by_id(id):
        return jsonify(BAL.customer.get_customer(id)[0])

    @app.route('/v1/customers/Search/Last/<lastname>', methods=['GET'])
    def get_sale_by_lastname(lastname):
        return jsonify(BAL.customer.get_customer_by_last_name(lastname))

    @app.route('/', methods=['GET'])
    def home():
        return """<h1>Sales Statistics</h1><p>This site is a prototype API for reporting sales
         statistics for use with Python and Pandas clients.</p>"""

    @app.route('/v1/stats/data/full', methods=['GET'])
    def get_all_stats():
        return jsonify(BAL.stats.get_all_stats())

    @app.route('/v1/stats/data/students', methods=['GET'])
    def get_all_students():
        return jsonify(BAL.stats.get_all_students())

    @app.route('/v1/stats/data/province/<p>', methods=['GET'])
    def get_provinces():
        return jsonify(BAL.stats.get_all_provinces(p))

    @app.route('/v1/stats/lfs/<#>', methods=['GET'])
    def get_lfs():
        return jsonify(BAL.stats.get_lfs(#))

    app.run(host='0.0.0.0')