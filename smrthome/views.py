# -*- coding: latin-1 -*-

"""
URL routes declarations.

All views are currently declared here.

"""
import os

from flask import render_template, jsonify
from twilio.rest import TwilioRestClient

from smrthome import app, make_json_error
from cloudly import logger, cache

log = logger.init(__name__)
redis = cache.get_redis_connection()


@app.errorhandler(Exception)
def error_handler(error):
    return make_json_error(error)


@app.route('/')
def index():
    """A map with real-time tweets shown.
    Configuration options are set here and available to the client via the
    global variable `appConfig`, see templates/base.html.
    """
    webapp_config = {
    }
    return render_template('index.html', config=webapp_config)


@app.route('/doorbell')
def doorbell():
    if redis.get("doorbell") != "ringing":
        send_sms("La porte dit: on sonne.")
        # Don't send SMS too often.
        redis.set("doorbell", "ringing")
        redis.expire("doorbell", 60 * 2)
        status = "SMS sent successfully."
        http_status = 200
    else:
        status = "SMS already sent."
        http_status = 202
    return jsonify(status=status), http_status


def in_production():
    return os.environ.get("IS_PRODUCTION", "").lower() in ['true', 'yes']


def send_sms(message):
    account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    recipient_number = os.environ.get("TWILIO_RECIPIENT_NUMBER")
    twilio_number = os.environ.get("TWILIO_NUMBER")

    client = TwilioRestClient(account_sid, auth_token)
    message = client.sms.messages.create(body=message, to=recipient_number,
                                         from_=twilio_number)
    return message.sid
