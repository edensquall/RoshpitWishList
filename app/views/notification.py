import datetime
import json
import urllib
from urllib.request import Request

from flask import render_template, Blueprint, request, current_app, flash, url_for
from flask_login import login_required, current_user
from werkzeug.utils import redirect

from app.forms import SettingsForm
from app.models.notify import Notify
from app.models.user import User
from app.services.base_notification_service import BaseNotificationService

notification = Blueprint('notification', __name__, url_prefix='/notification')


@notification.route('/settings', methods=['GET', 'POST'])
@login_required
def settings(notification_service: BaseNotificationService):
    obj = notification_service.get_user_settings(User(id=current_user.id))

    form = SettingsForm(obj=obj)

    if request.method == 'POST' and form.validate_on_submit():
        user = User(
            id=current_user.id,
            name=form.name.data,
            email=form.email.data,
            is_notification=form.is_notification.data,
            notification_method=form.notification_method.data,
            modify_date=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )

        notification_service.edit_user_settings(user)

        flash('Save success', 'success')
        return redirect(url_for('wish_list.index'))

    return render_template('notification/settings.html', title='Settings', form=form, current_user=current_user,
                           redirect_uri=current_app.config['CALLBACK_URL'],
                           client_id=current_app.config['CLIENT_ID'],
                           client_secret=current_app.config['CLIENT_SECRET'])


@notification.route('/set_notify', methods=['GET', 'POST'])
def set_notify(notification_service: BaseNotificationService):
    code = request.args.get('code')
    state = request.args.get('state')

    url = 'https://notify-bot.line.me/oauth/token'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = urllib.parse.urlencode({'grant_type': 'authorization_code',
                                   'code': code,
                                   'redirect_uri': current_app.config['CALLBACK_URL'],
                                   'client_id': current_app.config['CLIENT_ID'],
                                   'client_secret': current_app.config['CLIENT_SECRET']}).encode('ascii')

    req = urllib.request.Request(url, data, headers)
    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read().decode('utf-8'))

        if result and result['status'] == 200:
            notification_service.add_new_notify(Notify(
                id=result['access_token'],
                user_id=current_user.id,
                create_date=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                modify_date=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            ))

    return '<script>window.close()</script>'
