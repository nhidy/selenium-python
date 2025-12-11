import pytest 
import json

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.customer.customer_single_helpers import CustomerSingleHelper

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user1']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.test_request_customer
class TestRequest(object):
    @pytest.mark.test_request_customer
    def test_request_customer(self, user):
        helper = CustomerSingleHelper(user)
        payload = {
            "search_text": "",
            "page_size": 0,
            "page_index": 0
        }
        rs = helper.simple_search_customer_single(payload)
        print('RESPONSE' + '\n' + '\t', json.dumps(rs, indent=4, sort_keys=True))
        assert rs['items'], f"No data found. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}"