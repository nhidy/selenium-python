from datetime import datetime
import json
import random
import pytest
import time

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.admin.admin_helpers import AdminHelper
from apitest.src.payloads.admin.admin_payload import AdminPayload
admin_payload = AdminPayload()
from apitest.src.helpers.customer.customer_single_helpers import CustomerSingleHelper
from apitest.src.payloads.customer.customer_single_payload import CustomerSinglePayload
customer_single_payload = CustomerSinglePayload()
from apitest.src.helpers.customer.approve_modify_customer_helpers import ApproveModifyCustomerHelper
from apitest.src.payloads.customer.approve_modify_customer_payload import ApproveModifyCustomerPayload
approve_modify_customer_payload = ApproveModifyCustomerPayload()

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user3']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.test_customer_and_deposit_service
class TestCustomerAndDepositService(object):

    @pytest.mark.simple_search_branch
    def test_001_simple_search_branch(self, user):
        helper = AdminHelper(user)
        fields_data = admin_payload.simple_search(
            page_size=5
        )
        rs = helper.ADM_SIMPLE_SEARCH_BRANCH(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'branch_code' in rs['items'][0], f'Key \"branch_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'branch_name' in rs['items'][0], f'Key \"branch_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'branch_address' in rs['items'][0], f'Key \"branch_address\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'base_currency_code' in rs['items'][0], f'Key \"base_currency_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'is_online' in rs['items'][0], f'Key \"is_online\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'