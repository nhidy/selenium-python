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

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user3']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.test_admin_service
class TestAdminService(object):

    @pytest.mark.simple_search_branch
    def test_001_simple_search_branch(self, user):
        global total_count
        helper = AdminHelper(user)
        fields_data = admin_payload.simple_search(
            page_size=5
        )
        rs = helper.ADM_SIMPLE_SEARCH_BRANCH(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            total_count = rs['total_count']
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            if len(rs['items']) > 0:
                assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'branch_code' in rs['items'][0], f'Key \"branch_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'branch_name' in rs['items'][0], f'Key \"branch_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'branch_address' in rs['items'][0], f'Key \"branch_address\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'base_currency_code' in rs['items'][0], f'Key \"base_currency_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                assert 'is_online' in rs['items'][0], f'Key \"is_online\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                # for i in range(len(rs['items'])): 
                #     check_data_type(rs['items'][i])
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'