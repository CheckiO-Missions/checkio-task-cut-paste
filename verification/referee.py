def cpchecker(data, user_result):
    try:
        solver = compile(user_result, '<string>', 'eval')
        stripe = eval(solver)
        if any((type(stripe) != str,
                len(stripe) != sum(len(ribbon) for ribbon in data),
                any(a not in '01' for a in stripe),
                any(a == b for a, b in zip(stripe, stripe[1:])))):
            return False
        cuts = sum(a == b for ribbon in data for a, b in zip(ribbon, ribbon[1:]))
        commutator = [[False] * len(ribbon) for ribbon in data]
        data = ['0' * len(ribbon) for ribbon in data]
        res = eval(solver)
        if '1' in res:
            return False
        targets = []
        for i, ribbon in enumerate(data):
            ribbon = list(ribbon)
            for j in range(len(ribbon)):
                ribbon[j] = '1'
                data[i] = ''.join(ribbon)
                res = eval(solver)
                if res.count('1') != 1:
                    return False
                k = res.index('1')
                targets.append(k)
                commutator[i][j], ribbon[j] = k, '0'
            data[i] = ''.join(ribbon)
        targets.sort()
        if targets != list(range(len(stripe))):
            return False
        for i, switches in enumerate(commutator):
            for a, b in zip(switches, switches[1:]):
                cuts -= abs(a - b) != 1
        return not cuts
    except Exception:
        return False


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
        checker=cpchecker,
        function_name='checkio'
    ).on_ready)
