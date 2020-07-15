from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(404)
def error_404(error):
	return render_template('errors/404.html'), 404
# in flask you can return second value returning status code,
# by default it is 200 that is why we didn't needed to 200 previously

@errors.app_errorhandler(403)
def error_403(error):
	return render_template('errors/403.html'), 403

@errors.app_errorhandler(500)
def error_500(error):
	return render_template('errors/500.html'), 500