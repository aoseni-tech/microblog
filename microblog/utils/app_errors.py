from flask import render_template,json

def handle_exception(e):
    """ReturnError page for for HTTP errors."""
    return render_template('error_page.html', error=e), 404
