# from weakref import ref
import pytest 

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility

@pytest.mark.auth_neptune
class TestAuthorizeNeptune(object):
    @pytest.mark.login_neptune
    def test_login_neptune(self):
        req = RequestUtility('')
        req.login_neptune()