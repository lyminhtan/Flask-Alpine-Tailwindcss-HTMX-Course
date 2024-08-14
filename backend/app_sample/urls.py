from flask import Blueprint
bp = Blueprint('sample', __name__, cli_group=None, url_prefix='/')
from . import views
