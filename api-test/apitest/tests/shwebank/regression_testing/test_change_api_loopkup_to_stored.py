from datetime import datetime
import json
import random
import pytest
import time

from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility

from apitest.src.helpers.common.common_helpers import CommonHelper
from apitest.src.payloads.common.common_payload import CommonPayload

common_payload = CommonPayload()

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user3']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.test_change_api_loopkup_to_stored
class TestChangeApiLoopkupToStored(object):

    @pytest.mark.adm_lookup_user_account_by_branchid
    def test_001_adm_lookup_user_account_by_branchid(self, user):
        global total_count
        helper = CommonHelper(user)
        fields_data = common_payload.adm_lookup_user_account_by_branchid(
            page_size=5
        )
        rs = helper.ADM_LOOKUP_USER_ACCOUNT_BY_BRANCHID(fields_data)
        try:
            assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            total_count = rs['total_count']
            assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            # if len(rs['items']) > 0:
            #     assert 'id' in rs['items'][0], f'Key \"id\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            #     assert 'branch_code' in rs['items'][0], f'Key \"branch_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            #     assert 'branch_name' in rs['items'][0], f'Key \"branch_name\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            #     assert 'branch_address' in rs['items'][0], f'Key \"branch_address\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            #     assert 'base_currency_code' in rs['items'][0], f'Key \"base_currency_code\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
            #     assert 'is_online' in rs['items'][0], f'Key \"is_online\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
                # for i in range(len(rs['items'])): 
                #     check_data_type(rs['items'][i])
        except:
            assert False, f'Something\'s wrong. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'