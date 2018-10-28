from flask import render_template,current_app

from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    current_app.logger.info('info')
    current_app.logger.error('error')
    return render_template('index.html')
