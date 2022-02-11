from flask import Blueprint
from app.controllers import series_controller


bp = Blueprint('series', __name__, url_prefix='/series')


bp.get('')(series_controller.get_series)
bp.get('/<int:id>')(series_controller.select_by_id)
bp.post('')(series_controller.create_series)
 