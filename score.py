from flask import Blueprint, render_template, send_file
import locale

from qrcodeutil import generate_qr_code
import parameters as pm

score = Blueprint('score', __name__)

locale.setlocale(locale.LC_NUMERIC, 'en_US.UTF-8')


@score.route('/score/<nation>/<int:userscore>')
def get_score_nation(nation, userscore):
    formatted_score = locale.format_string('%d', userscore, grouping=True)

    if nation == 'fire':
        return render_template('fogo-score.html', score=formatted_score.replace(',', '.'))
    elif nation == 'earth':
        return render_template('terra-score.html', score=formatted_score.replace(',', '.'))
    elif nation == 'water':
        return render_template('agua-score.html', score=formatted_score.replace(',', '.'))
    elif nation == 'air':
        return render_template('ar-score.html', score=formatted_score.replace(',', '.'))


@score.route('/qr/<nation>/<userscore>')
def get_qrcode_score(nation, userscore):
    qr_image = generate_qr_code(pm.BASE_URL + '/score/' + nation + '/' + userscore)
    return send_file(qr_image, mimetype='image/png')
