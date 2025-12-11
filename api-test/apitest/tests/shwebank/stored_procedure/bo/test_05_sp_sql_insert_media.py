import json
import pytest

from datetime import datetime
from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.stored_procedure.stored_procedure_helpers import StoredProcedureHelper
from apitest.src.payloads.stored_procedure.stored_procedure_payload import StoredProcedurePayload

sp_payload = StoredProcedurePayload()

# data test valid
file_upload_id=1501
media_name='cbimage.png'
customer_code='11001699'
reference_type='C'
other='097543435345'
media_status='N'
media_type='img'
open_date='2023-09-11T00:00:00'
last_update_date='2023-09-11T00:00:00'
infor1='C1'
infor2='API TEST'
# data test invalid

@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user1']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.SP_SQL_INSERT_MEDIA
class Test_SP_SQL_INSERT_MEDIA(object):

    def test_sp_sql_insert_media_001_success(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.SQL_INSERT_MEDIA(
            file_upload_id=file_upload_id,
            media_name=media_name,
            customer_code=customer_code,
            reference_type=reference_type,
            other=other,
            media_status=media_status,
            media_type=media_type,
            open_date=open_date,
            last_update_date=last_update_date,
            infor1=infor1,
            infor2=infor2
        )
        rs = sp_helper.SQL_INSERT_MEDIA(fields_data)
        step_code_01 = 'SQL_INSERT_MEDIA'
        data_actual_01 = RequestUtility.get_p2_content_response_by_step_code(rs, step_code_01)
        print(json.dumps(data_actual_01, indent=4, sort_keys=False))
        step_code_02 = 'CMS_MOVE_TO_USER_MEDIA'
        data_actual_02 = RequestUtility.get_p2_content_response_by_step_code(rs, step_code_02)
        print(json.dumps(data_actual_02, indent=4, sort_keys=False))
        step_code_03 = 'CTM_UPDATE_MEDIA_UPLOAD_ID'
        data_actual_03 = RequestUtility.get_p2_content_response_by_step_code(rs, step_code_03)
        print(json.dumps(data_actual_03, indent=4, sort_keys=False))
        assert '', f"Expected: ..., Actual: response Json:"