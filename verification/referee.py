def checker(data, user_result):
    return True, {'error_code': 100, 'message': 'good'}


from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.io import CheckiOReferee
from checkio.referees.cover_codes import unwrap_args

from tests import TESTS


api.add_listener(
    ON_CONNECT,
    CheckiOReferee(
        tests=TESTS,
        cover_code={
            'python-27': unwrap_args,
            'python-3': unwrap_args,
        },
        checker=checker,
        function_name='checkio'
    ).on_ready)
