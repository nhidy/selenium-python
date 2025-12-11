from ..utilities.requestUtility import RequestUtility

class AuthHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def login(self, payload):
        return self.requests_utility.post_admin(f'api/Authenticate/GetToken', payload)

    def generate(self, payload):
        return self.requests_utility.post_admin(f'api/Authenticate/Generate', payload)

    def login_approve(self, payload):
        return self.requests_utility.post_admin(f'', payload)
        # auth/AuthenicationApprove

    def logout(self, payload):
        return self.requests_utility.post_admin(f'', payload)
        # auth/logout

    def keep_alive(self, payload):
        return self.requests_utility.post_admin(f'', payload)
        # auth/KeepAlive

    def login_sql_injection(self, payload):
        return self.requests_utility.post_admin(f'', payload)
        # auth/authenticate