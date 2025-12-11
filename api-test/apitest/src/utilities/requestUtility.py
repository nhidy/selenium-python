import requests 
import json 
import uuid 
import logging as logger 
import time
import datetime
import pyodbc
import pandas as pd

from apitest.src.configs import NEPTUNE_URL, NEPTUNE_LOGINNAME, NEPTUNE_PASSWORD, SERVICE_URL, STATIC_TOKEN_NEPTUNE, OPENAPI_URL, STATIC_TOKEN_CZ, STATIC_TOKEN_MO, DB_INFO
# , STATIC_TOKEN_DI, STATIC_TOKEN_PG, STATIC_TOKEN_BI, STATIC_TOKEN_MU, STATIC_TOKEN_CB, STATIC_TOKEN_CQ, STATIC_TOKEN_LO

class RequestUtility(object):
    def __init__(self, ssn):
        self.neptune_url = NEPTUNE_URL
        self.neptune_loginname = NEPTUNE_LOGINNAME
        self.neptune_password = NEPTUNE_PASSWORD
        self.openapi_url = OPENAPI_URL
        self.token = ''
        self.auth_token = ''
        self.auth_openapi_token = ''
        self.s = requests.Session()
        self.ssn = ssn
        self.admin_url = SERVICE_URL['adm']
        self.customer_url = SERVICE_URL['ctm']
        self.accounting_url = SERVICE_URL['act']
        self.cash_url = SERVICE_URL['csh']
        self.credit_url = SERVICE_URL['crd']
        self.deposit_url = SERVICE_URL['dpt']
        self.fixed_asset_url = SERVICE_URL['fac']
        self.fx_url = SERVICE_URL['fx']
        self.ifc_url = SERVICE_URL['ifc']
        self.mortgage_url = SERVICE_URL['mtg']
        self.payment_url = SERVICE_URL['pmt']
        self.statis_token_neptune = STATIC_TOKEN_NEPTUNE
        self.statis_token_cz = STATIC_TOKEN_CZ
        self.statis_token_mo = STATIC_TOKEN_MO
        # self.statis_token_di = STATIC_TOKEN_DI
        # self.statis_token_pg = STATIC_TOKEN_PG
        # self.statis_token_bi = STATIC_TOKEN_BI
        # self.statis_token_mu = STATIC_TOKEN_MU
        # self.statis_token_cb = STATIC_TOKEN_CB
        # self.statis_token_cq = STATIC_TOKEN_CQ
        # self.statis_token_lo = STATIC_TOKEN_LO
        self.db_info = DB_INFO

    @property 
    def uid(self):
        return uuid.uuid4().hex 

    @property
    def login_headers(self):
        headers = {
            'content-type': "application/json"
        }
        return headers

    @property 
    def headers(self):
        headers = {
            'content-type': "application/json",
            'authorization': "Bearer " + self.token
            # 'authorization': "Bearer " + self.statis_token_neptune
        }
        return headers

    @property 
    def openapi_headers_cz(self):
        openapi_headers_cz = {
            'content-type': "application/json",
            'authorization': "Bearer " + self.statis_token_cz
        }
        return openapi_headers_cz

    @property 
    def openapi_headers_mo(self):
        openapi_headers_mo = {
            'content-type': "application/json",
            'authorization': "Bearer " + self.statis_token_mo
        }
        return openapi_headers_mo

    def close(self):
        self.s.close()

    def logging_log(self, link, data):
        loggering = logger.getLogger('LOG')
        loggering.setLevel(logger.DEBUG)
        file_logger = logger.FileHandler('log_test.log')
        format = logger.Formatter('[%(asctime)s] - [%(levelname)s] - %(message)s', '%Y-%m-%d %H:%M:%S')
        file_logger.setFormatter(format)
        loggering.addHandler(file_logger)
        loggering.debug(link + ' - ' + str(data))
        loggering.removeHandler(file_logger)

    def log(self, note, data):
        logger.getLogger('SmartfileTest').debug('\n' + note + '\n' + '\t' + str(data))

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, f"Bad HTTP status code. Expected {self.expected_status_code}, Actual status code: {self.status_code}, URL: {self.url}, Response Json: {json.dumps(self.rs_json, indent=4, sort_keys=True)}"

    def assert_p2_status(self):
        assert self.p2_status == 'Completed', f"Bad p2_status. Expected \'Completed\', Actual status: {self.p2_status}, URL: {self.url}, Response Json: {json.dumps(self.rs_json, indent=4, sort_keys=True)}"

    def assert_execute_status(self):
        assert self.execute_status == 'COMPLETED', f"Bad execute status. Expected \'COMPLETED\', Actual status: {self.execute_status}, URL: {self.url}, Response Json: {json.dumps(self.rs_json, indent=4, sort_keys=True)}"

    def get(self, url, payload=None, expected_status=None, headers=None):
        self.url = f'{url}'

        if not expected_status:
            expected_status = 200

        if not headers: 
            headers = self.headers

        data = json.dumps(payload)
        rs_api = self.s.get(url=self.url, data=data, headers=headers, verify=False)
        self.origin_response = rs_api
        self.status_code = rs_api.status_code 
        self.expected_status_code = expected_status
        self.assert_status_code()
        self.rs_json = rs_api.json()
        # self.logging_log(self.url, self.rs_json)
        return self.rs_json

    def post(self, url, payload=None, expected_status=None, headers=None):
        self.url = f'{url}'

        if not expected_status:
            expected_status = 200
        
        if not headers:
            headers = self.headers

        data = json.dumps(payload)
        # self.logging_log(self.url, data)
        rs_api = self.s.post(self.url, data=data, headers=headers, verify=False)
        self.origin_response = rs_api
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status
        self.assert_status_code()
        self.rs_json = rs_api.json()
        # self.logging_log(self.url, self.rs_json)
        return self.rs_json

    def put(self, url, payload=None, expected_status=None, headers=None):
        self.url = f'{url}'

        if not expected_status:
            expected_status = 200
        
        if not headers:
            headers = self.headers

        data = json.dumps(payload)
        rs_api = self.s.put(self.url, data=data, headers=headers, verify=False)
        self.origin_response = rs_api
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status
        self.assert_status_code()
        self.rs_json = rs_api.json()
        # self.logging_log(self.url, self.rs_json)
        return self.rs_json

    def delete(self, url, payload=None, expected_status=None, headers=None):
        self.url = f'{url}'

        if not expected_status:
            expected_status = 200
        
        if not headers:
            headers = self.headers

        data = json.dumps(payload)
        rs_api = self.s.delete(self.url, data=data, headers=headers, verify=False)
        self.origin_response = rs_api
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status
        self.assert_status_code()
        self.rs_json = rs_api.json()
        # self.logging_log(self.url, self.rs_json)
        return self.rs_json

# config neptune
    def post_neptune(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.neptune_url}{endpoint}'
        return self.post(self.url, payload=payload, expected_status=expected_status, headers=headers)

    def get_neptune(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.neptune_url}{endpoint}'
        return self.get(self.url, payload=payload, expected_status=expected_status, headers=headers)

    def put_neptune(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.neptune_url}{endpoint}'
        return self.put(self.url, payload=payload, expected_status=expected_status, headers=headers)

    def delete_neptune(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.neptune_url}{endpoint}'
        return self.delete(self.url, payload=payload, expected_status=expected_status, headers=headers)

# config openAPI
    def post_openapi(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.openapi_url}{endpoint}'
        return self.post(self.url, payload=payload, expected_status=expected_status, headers=headers)

    def get_openapi(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.openapi_url}{endpoint}'
        return self.get(self.url, payload=payload, expected_status=expected_status, headers=headers)

# config admin
    def post_admin(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.admin_url}{endpoint}'
        return self.post(self.url, payload=payload, expected_status=expected_status, headers=headers)

    def get_admin(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.admin_url}{endpoint}'
        return self.get(self.url, payload=payload, expected_status=expected_status, headers=headers)

    def put_admin(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.admin_url}{endpoint}'
        return self.put(self.url, payload=payload, expected_status=expected_status, headers=headers)

    def delete_admin(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.admin_url}{endpoint}'
        return self.delete(self.url, payload=payload, expected_status=expected_status, headers=headers)

# config customer
    def post_customer(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.customer_url}{endpoint}'
        return self.post(self.url, payload=payload, expected_status=expected_status, headers=headers)

    def get_customer(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.customer_url}{endpoint}'
        return self.get(self.url, payload=payload, expected_status=expected_status, headers=headers)

    def put_customer(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.customer_url}{endpoint}'
        return self.put(self.url, payload=payload, expected_status=expected_status, headers=headers)

    def delete_customer(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.customer_url}{endpoint}'
        return self.delete(self.url, payload=payload, expected_status=expected_status, headers=headers)

# config accounting
    def post_accounting(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.accounting_url}{endpoint}'
        return self.post(self.url, payload=payload, expected_status=expected_status, headers=headers)

    def get_accounting(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.accounting_url}{endpoint}'
        return self.get(self.url, payload=payload, expected_status=expected_status, headers=headers)

    def put_accounting(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.accounting_url}{endpoint}'
        return self.put(self.url, payload=payload, expected_status=expected_status, headers=headers)

    def delete_accounting(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.accounting_url}{endpoint}'
        return self.delete(self.url, payload=payload, expected_status=expected_status, headers=headers)

# config cash
    def post_cash(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.cash_url}{endpoint}'
        return self.post(self.url, payload=payload, expected_status=expected_status, headers=headers)

    def get_cash(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.cash_url}{endpoint}'
        return self.get(self.url, payload=payload, expected_status=expected_status, headers=headers)

    def put_cash(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.cash_url}{endpoint}'
        return self.put(self.url, payload=payload, expected_status=expected_status, headers=headers)

    def delete_cash(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.cash_url}{endpoint}'
        return self.delete(self.url, payload=payload, expected_status=expected_status, headers=headers)

# config credit
    def post_credit(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.credit_url}{endpoint}'
        return self.post(self.url, payload=payload, expected_status=expected_status, headers=headers)

    def get_credit(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.credit_url}{endpoint}'
        return self.get(self.url, payload=payload, expected_status=expected_status, headers=headers)

    def put_credit(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.credit_url}{endpoint}'
        return self.put(self.url, payload=payload, expected_status=expected_status, headers=headers)

    def delete_credit(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.credit_url}{endpoint}'
        return self.delete(self.url, payload=payload, expected_status=expected_status, headers=headers)

# config deposit
    def post_deposit(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.deposit_url}{endpoint}'
        return self.post(self.url, payload=payload, expected_status=expected_status, headers=headers)

    def get_deposit(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.deposit_url}{endpoint}'
        return self.get(self.url, payload=payload, expected_status=expected_status, headers=headers)

    def put_deposit(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.deposit_url}{endpoint}'
        return self.put(self.url, payload=payload, expected_status=expected_status, headers=headers)

    def delete_deposit(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.deposit_url}{endpoint}'
        return self.delete(self.url, payload=payload, expected_status=expected_status, headers=headers)

# config fixed asset
    def post_fixed_asset(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.fixed_asset_url}{endpoint}'
        return self.post(self.url, payload=payload, expected_status=expected_status, headers=headers)

    def get_fixed_asset(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.fixed_asset_url}{endpoint}'
        return self.get(self.url, payload=payload, expected_status=expected_status, headers=headers)

    def put_fixed_asset(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.fixed_asset_url}{endpoint}'
        return self.put(self.url, payload=payload, expected_status=expected_status, headers=headers)

    def delete_fixed_asset(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.fixed_asset_url}{endpoint}'
        return self.delete(self.url, payload=payload, expected_status=expected_status, headers=headers)

# config fx
    def post_fx(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.fx_url}{endpoint}'
        return self.post(self.url, payload=payload, expected_status=expected_status, headers=headers)

    def get_fx(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.fx_url}{endpoint}'
        return self.get(self.url, payload=payload, expected_status=expected_status, headers=headers)

    def put_fx(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.fx_url}{endpoint}'
        return self.put(self.url, payload=payload, expected_status=expected_status, headers=headers)

    def delete_fx(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.fx_url}{endpoint}'
        return self.delete(self.url, payload=payload, expected_status=expected_status, headers=headers)

# config mortgage
    def post_mortgage(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.mortgage_url}{endpoint}'
        return self.post(self.url, payload=payload, expected_status=expected_status, headers=headers)

    def get_mortgage(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.mortgage_url}{endpoint}'
        return self.get(self.url, payload=payload, expected_status=expected_status, headers=headers)

    def put_mortgage(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.mortgage_url}{endpoint}'
        return self.put(self.url, payload=payload, expected_status=expected_status, headers=headers)

    def delete_mortgage(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.mortgage_url}{endpoint}'
        return self.delete(self.url, payload=payload, expected_status=expected_status, headers=headers)

# config payment
    def post_payment(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.payment_url}{endpoint}'
        return self.post(self.url, payload=payload, expected_status=expected_status, headers=headers)

    def get_payment(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.payment_url}{endpoint}'
        return self.get(self.url, payload=payload, expected_status=expected_status, headers=headers)

    def put_payment(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.payment_url}{endpoint}'
        return self.put(self.url, payload=payload, expected_status=expected_status, headers=headers)

    def delete_payment(self, endpoint, payload=None, expected_status=None, headers=None):
        self.url = f'{self.payment_url}{endpoint}'
        return self.delete(self.url, payload=payload, expected_status=expected_status, headers=headers)

# login neptune
    def login_neptune(self):
        body = {
            'user_code': self.neptune_loginname,
            'password': self.neptune_password
        }

        res = self.post_neptune(endpoint='api/auth/get-token', payload=body, expected_status=200, headers=self.login_headers)
        # self.log('Respone: ', res)
        self.token = res['data']['token']

# get info step 1
    def get_execution_info_res_body(self, workflow_id, fields_data):
        body = {
            "workflowid": workflow_id,
            "lang": "en",
            "token": self.auth_token,
            "reference_id": str(uuid.uuid4()),
            "fields": fields_data
        }

        res = self.post_neptune(endpoint='api/workflow/execute', payload=body)
        self.execute_status = res['status']
        self.assert_execute_status()

        execution_id = res['execution_id']
        time_number = 0
        while (time_number < 60):
            time_number += 1
            res = self.get_neptune(endpoint=f'api/workflow/get-execution-info/{execution_id}')
            status = res['execution_steps'][0]['p2_status']
            if status == 'Completed':
                break
            time.sleep(1)

        self.execution_info = res
        self.p2_status = status
        return self.execution_info

# get info step 1
    def get_p2_content_response_data(self, workflow_id, fields_data):
        response_data=None
        body = {
            "workflowid": workflow_id,
            "lang": "en",
            "token": self.auth_token,
            "reference_id": str(uuid.uuid4()),
            "fields": fields_data
        }
        # print('body: ', body)
        res = self.post_neptune(endpoint='api/workflow/execute', payload=body)
        # print('res: ', res)
        self.execute_status = res['status']
        # check execute status
        self.assert_execute_status()
        # get execution id and get execution info
        execution_id = res['execution_id']
        time_number = 0
        # waiting process
        while (time_number < 60):
            time_number += 1
            res = self.get_neptune(endpoint=f'api/workflow/get-execution-info/{execution_id}')
            status = res['execution_steps'][0]['p2_status']
            if status == 'Completed':
                break
            time.sleep(1)
        # check p2_status lock res['execution_steps'][0]
        self.p2_status = status
        self.assert_p2_status()
        # check p2_status lock res['execution_steps'][1]
        if len(res['execution_steps']) > 1:
            # waiting process ['execution_steps'][1]
            # print('Len of execution_steps: ', len(res['execution_steps']))
            while (time_number < 60):
                time_number += 1
                res = self.get_neptune(endpoint=f'api/workflow/get-execution-info/{execution_id}')
                status = res['execution_steps'][len(res['execution_steps'])-1]['p2_status']
                if status == 'Completed':
                    break
                time.sleep(1)
            if status != 'Completed':
                self.p2_status = status
                self.assert_p2_status()
            response_data = res['execution_steps'][1]['p2_content']['response']['data']
        else:
            response_data = res['execution_steps'][0]['p2_content']['response']['data']
        # return p2_content response data
        return response_data

# get response
    def get_response_data(self, workflow_id, fields_data, reversal_execution_id=None, approved_execution_id=None):
        response_data=None
        if not reversal_execution_id:
            reversal_execution_id=''
        if not approved_execution_id:
            approved_execution_id=''
        body = {
            "workflowid": workflow_id,
            "lang": "en",
            "token": self.auth_token,
            "reversal_execution_id": reversal_execution_id,
            "approved_execution_id": approved_execution_id,
            "reference_id": str(uuid.uuid4()),
            "fields": fields_data
        }
        # send request message
        res = self.post_neptune(endpoint='api/workflow/execute', payload=body)
        # get status response
        self.execute_status = res['status']
        # check execute status
        if self.execute_status != 'COMPLETED':
            print("Data response for execute_status NOT 'COMPLETED'")
            return res
        self.assert_execute_status()
        # get execution id and get execution info
        execution_id = res['execution_id']
        time_number = 0
        # waiting process, 60s
        while (time_number < 60):
            res = self.get_neptune(endpoint=f'api/workflow/get-execution-info/{execution_id}')
            execution_steps = res['execution_steps']
            # Check conditions to break the loop
            all_completed = all(step.get("p2_status") == "Completed" for step in execution_steps)
            any_failed = any(step.get("p2_status") == "Failed" for step in execution_steps)
            # Output the result
            if all_completed or any_failed:
            # if all_completed:
                # print("Breaking loop: All steps completed or at least one failed.")
                response_data = res
                break
            else:
                # print("Waiting: Not all steps completed, and no failures yet.")
                time.sleep(1)
                time_number += 1
                # print(f"time_number: {time_number}")
                if time_number == 59:
                    response_data = res
        return response_data

# reload cache
    def reload_cache(self):
        res = self.post_neptune('api/cache/reload')
        status = res['status']
        assert status == 'COMPLETED', f"Reload cache failed. Expected \'COMPLETED\', Actual status: {status}, URL: {self.url}, Response Json: {json.dumps(res, indent=4, sort_keys=True)}"

# login service
    def login_service(self):
        # self.reload_cache()
        workflow_id = 'UMG_LOGIN'
        fields_data = {
            "username": self.ssn['username'],
            "password": self.ssn['password']
        }
        res = self.get_execution_info_res_body(workflow_id, fields_data)
        # self.log('self.p2_status', self.p2_status)
        self.assert_p2_status()
        self.auth_token = res['execution_steps'][0]['p2_content']['response']['data']['login']['token']
        return self.auth_token
        
        # payload = {
        #     "username": self.ssn['username'],
        #     "password": self.ssn['password']
        # }
        # res = self.post_admin('api/Authenticate/GetToken', payload=payload)
        # self.auth_token = res['token']
        # return self.auth_token



    def openapi_login_cz(self):
        payload = {
            "lang": "en",
            "fields": {
                "username": self.ssn['username'],
                "password": self.ssn['password']
            }
        }
        res = self.post_openapi('execute/UMG_LOGIN', payload=payload, headers=self.openapi_headers_cz)
        self.auth_openapi_token_cz = res['data']['token']
        return self.auth_openapi_token_cz

    def openapi_get_response_data_cz(self, workflow_id, fields_data):
        body = {
            "lang": "en",
            "token": self.auth_openapi_token_cz,
            "reference_id": str(uuid.uuid4()),
            "reference_code": "",
            "business_code": "",
            "tran_date": "",
            "description": "",
            "fields": fields_data
        }
        # print('body: ', body)
        res = self.post_openapi(endpoint='execute/' + workflow_id, payload=body, headers=self.openapi_headers_cz)
        # print('res get_openapi_response_data: ', res)
        self.response = res
        # return response data
        return self.response

    def openapi_reverse_by_execution_id_cz(self, execution_id, transaction_date):
        body = {
            "token": self.auth_openapi_token_cz,
            "transaction_id": execution_id,
            "transaction_date": transaction_date
        }
        # print('body: ', body)
        res = self.post_openapi(endpoint='reverse', payload=body, headers=self.openapi_headers_cz)
        # print('res get_openapi_response_data: ', res)
        self.response = res
        # return response data
        return self.response

    def openapi_reverse_by_reference_id_cz(self, reference_id):
        body = {
            "token": self.auth_openapi_token_cz,
            "reference_id": reference_id
        }
        # print('body: ', body)
        res = self.post_openapi(endpoint='reverse-by-reference-id', payload=body, headers=self.openapi_headers_cz)
        # print('res get_openapi_response_data: ', res)
        self.response = res
        # return response data
        return self.response

    def openapi_login_mo(self):
        payload = {
            "lang": "en",
            "fields": {
                "username": self.ssn['username'],
                "password": self.ssn['password']
            }
        }
        res = self.post_openapi('execute/UMG_LOGIN', payload=payload, headers=self.openapi_headers_mo)
        self.auth_openapi_token_mo = res['data']['token']
        return self.auth_openapi_token_mo

    def openapi_get_response_data_mo(self, workflow_id, fields_data):
        body = {
            "lang": "en",
            "token": self.auth_openapi_token_mo,
            "reference_id": str(uuid.uuid4()),
            "reference_code": "",
            "business_code": "",
            "tran_date": "",
            "description": "",
            "fields": fields_data
        }
        # print('body: ', body)
        res = self.post_openapi(endpoint='execute/' + workflow_id, payload=body, headers=self.openapi_headers_mo)
        # print('res get_openapi_response_data: ', res)
        self.response = res
        # return response data
        return self.response

    def openapi_reverse_by_execution_id_mo(self, execution_id, transaction_date):
        body = {
            "token": self.auth_openapi_token_mo,
            "transaction_id": execution_id,
            "transaction_date": transaction_date
        }
        # print('body: ', body)
        res = self.post_openapi(endpoint='reverse', payload=body, headers=self.openapi_headers_mo)
        # print('res get_openapi_response_data: ', res)
        self.response = res
        # return response data
        return self.response

    def openapi_reverse_by_reference_id_mo(self, reference_id):
        body = {
            "token": self.auth_openapi_token_mo,
            "reference_id": reference_id
        }
        # print('body: ', body)
        res = self.post_openapi(endpoint='reverse-by-reference-id', payload=body, headers=self.openapi_headers_mo)
        # print('res get_openapi_response_data: ', res)
        self.response = res
        # return response data
        return self.response

    def query_db(sql_query, server=None, username=None, password=None, driver="SQL Server Native Client 11.0"):
        """
        Executes an SQL query and returns the result as a pandas DataFrame.

        Parameters:
        - sql_query: str, the SQL query to execute.
        - server: str, the database server address (default: DB_INFO['server']).
        - username: str, the username for the database (default: DB_INFO['username']).
        - password: str, the password for the database (default: DB_INFO['password']).
        - driver: str, the ODBC driver to use (default: "SQL Server Native Client 11.0").

        Returns:
        - pd.DataFrame containing the query results.

        Raises:
        - ValueError if the SQL query is invalid or connection fails.
        """
        # Use default credentials if not provided
        server = server or DB_INFO['server']
        username = username or DB_INFO['username']
        password = password or DB_INFO['password']
        try:
            connection = pyodbc.connect(
                f"DRIVER={{{driver}}};SERVER={server};UID={username};PWD={password}"
            )
            dataframe = pd.read_sql_query(sql_query, connection) # Execute the query and fetch results into a DataFrame
            return dataframe
        except Exception as e:
            raise ValueError(f"Database query failed: {e}")
        finally:
            try:
                connection.close() # Ensure the connection is closed
            except Exception as close_error:
                print(f"Error while closing the connection: {close_error}")

    def update_db(sql_query):
        server=DB_INFO['server']
        username=DB_INFO['username']
        password=DB_INFO['password']
        try:
            connection = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER='+server+';UID='+username+';PWD='+ password)
            cursor = connection.cursor()
            cursor.execute(sql_query)
            connection.commit()
        except Exception as e:
            print(f"Error execute update: {e}")
        finally:
            try:
                connection.close() # Ensure the connection is closed
            except Exception as close_error:
                print(f"Error while closing the connection: {close_error}")

# get p2_content_response_by_step_code
    def get_p2_content_response_by_step_code(response_data, step_code):
        # Find the first step with the matching step_code
        data = next((step for step in response_data.get("execution_steps", []) if step.get("step_code") == step_code), None)
        # Output the result
        if data:
            if ('response' in data['p2_content']):
                print(f"Data response available for step code '{step_code}'")
                return data['p2_content']['response']
            else:
                print(f"No key 'response' in 'p2_content' for step code '{step_code}'")
                return None
        else:
            print(f"No data response available for step code '{step_code}'")
            return None

# get p2_content_postings_by_step_code
    def get_p2_content_postings_by_step_code(response_data, step_code):
        # Find the first step with the matching step_code
        data = next((step for step in response_data.get("execution_steps", []) if step.get("step_code") == step_code), None)
        # Output the result
        if data:
            if ('postings' in data['p2_content']['request']['request_header']['tx_context']):
                print(f"Data postings available for step code '{step_code}'")
                return data['p2_content']['request']['request_header']['tx_context']['postings']
            else:
                print(f"No key 'postings' in 'tx_context' for step code '{step_code}'")
                return None
        else:
            print(f"No data postings available for step code '{step_code}'")
            return None

# get p2_content_account_balances_by_step_code
    def get_p2_content_account_balances_by_step_code(response_data, step_code):
        # Find the first step with the matching step_code
        data = next((step for step in response_data.get("execution_steps", []) if step.get("step_code") == step_code), None)
        # Output the result
        if data:
            if ('account_balances' in data['p2_content']['request']['request_header']['tx_context']):
                print(f"Data account_balances available for step code '{step_code}'")
                return data['p2_content']['request']['request_header']['tx_context']['account_balances']
            else:
                print(f"No key 'account_balances' in 'tx_context' for step code '{step_code}'")
                return None
        else:
            print(f"No data account_balances available for step code '{step_code}'")
            return None
