ALL_OK = True, {"error_code": 100, "message": "All ok."}


def checkcp(data, user_result):
    return ALL_OK


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
        checker=checkcp,
        function_name="checkio"
    ).on_ready)
