import random
import webui_test
import os
from datetime import datetime
from webui_test.logging import log

from webui_test.form_action import FormAction

# Get value from environment variable
RUN_ON_URL = os.getenv("TEST_CONFIG_RUN_ON_URL", "")
USERNAME_LOGIN = os.getenv("TEST_CONFIG_USERNAME_LOGIN", "")
PASSWORD_LOGIN = os.getenv("TEST_CONFIG_PASSWORD_LOGIN", "")
ONE_APP = os.getenv("TEST_CONFIG_ONE_APP", "")
CUSTOMER_CODE = os.getenv("TEST_CONFIG_CUSTOMER_CODE", "")
USERNAME_APPROVE = os.getenv("TEST_CONFIG_USERNAME_APPROVE", "")
PASSWORD_APPROVE = os.getenv("TEST_CONFIG_PASSWORD_APPROVE", "")
USERNAME_REVERSE = os.getenv("TEST_CONFIG_USERNAME_REVERSE", "")
PASSWORD_REVERSE = os.getenv("TEST_CONFIG_PASSWORD_REVERSE", "")

# path of folder content data_attached
main_path = '../../data_attached/'
# data test for customer
random_num = f"{random.randint(0, 99999):06}"
date_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
# personal information - add
business_line_personal = 'Personal'
title_personal = 'Mr'
customer_type_personal = 'Individual'
customer_sub_type_personal = 'Other'
first_name_personal = 'TEST AUTO'
last_name_personal = 'ADD personal ' + str(date_time)
full_name_personal = first_name_personal.upper() + ' ' + last_name_personal.upper()
father_name_personal = 'Father name'
gender_personal = 'Female'
date_of_birth_personal = '16/03/2000'
nationality_personal = 'Canadian'
paper_type_personal = 'National ID Number'
paper_number_personal = 'PP023' + random_num
resident_status_personal = 'Local'
home_01_personal = 'Home'
street_01_personal = 'Street'
ward_01_personal = 'Ward'
township_01_personal = 'Township'
home_02_personal = 'Home'
street_02_personal = 'Street'
ward_02_personal = 'Ward'
township_02_personal = 'Township'
name_01_personal = 'Name'
account_no_01_personal = '123456789'
name_02_personal = 'Name'
account_no_02_personal = '123456789'
mobile_phone_personal = '098645334'
employer_name_personal = 'Employer name'
occupation_personal = 'Other'
business_type_personal = 'Other'
reason_for_other_occupation_personal = 'Reason for other occupation personal'
reason_for_other_business_type_personal = 'Reason for other business type personal'
income_personal = 'Below 1,000,000 MMK'
credit_line_personal = '1,000,000,000.45'
currency_personal = 'MMK'
fx_limit_personal = '1,000,500,000.45'
currency_fx_personal = 'MMK'
# SME information - add
business_line_sme = 'SME'
customer_type_sme = 'Public Company'
full_name_sme = 'TEST AUTO ADD SME ' + str(date_time)
starting_date_of_company_sme = '16/03/2000'
nationality_sme = 'Canadian'
paper_type_sme = 'Company Registration'
paper_number_sme = 'PP523' + random_num
resident_status_sme = 'Foreigner'
home_01_sme = 'Home'
street_01_sme = 'Street'
ward_01_sme = 'Ward'
township_01_sme = 'Township'
home_02_sme = 'Home'
street_02_sme = 'Street'
ward_02_sme = 'Ward'
township_02_sme = 'Township'
name_01_sme = 'Name'
account_no_01_sme = '123456789'
name_02_sme = 'Name'
account_no_02_sme = '123456789'
mobile_phone_sme = '098645334'
employer_name_sme = 'Employer name'
country_of_income_sme = 'Brazil'
position_sme = 'Position is CEO'
credit_line_sme = '6,000,000,000.45'
currency_sme = 'MMK'
fx_limit_sme = '8,000,500,000.45'
currency_fx_sme = 'MMK'
# Corporate information - add
business_line_corporate = 'Corporate'
title_of_organization_corporate = 'School'
customer_type_corporate = 'Financial Institution/Non-Bank Financial Institution'
full_name_corporate = 'TEST AUTO ADD CORPORATE ' + str(date_time)
suffix_corporate = 'Dept.'
starting_date_of_company_corporate = '16/03/1999'
country_of_company_corporate = 'Armenia'
nationality_corporate = 'Bruneian'
paper_type_corporate = 'Other'
reason_for_other_paper_type_corporate = 'Reason for other paper type corporate'
paper_number_corporate = 'PP723' + random_num
tin_number_corporate = '043433444'
issue_date_of_paper_corporate = '16/03/1999'
issue_place_of_paper_corporate = 'Issue place of paper corporate'
expire_date_of_paper_corporate = '16/03/2099'
group_type_corporate = 'Managerial relationship'
group_sub_type_corporate = 'Partner of shareholder'
economic_sector_corporate = 'Other'
reason_for_other_economic_sector_corporate = 'Reason for other economic sector corporate'
sub_economic_sector_corporate = 'Other'
reason_for_other_sub_economic_sector_corporate = 'Reason for other sub economic sector corporate'
customer_segment_corporate = '3-VIP'
resident_status_corporate = 'Foreigner'
bank_identification_corporate = 'Shinhan'
fdi_info_corporate = 'FDI info corporate'
home_01_corporate = 'Home'
street_01_corporate = 'Street'
ward_01_corporate = 'Ward'
township_01_corporate = 'Township'
province_01_corporate = '12. Rakhine State'
home_02_corporate = 'Home'
street_02_corporate = 'Street'
ward_02_corporate = 'Ward'
township_02_corporate = 'Township'
province_02_corporate = '8. Magwe Division'
name_01_corporate = 'Name'
account_no_01_corporate = '123456789'
name_02_corporate = 'Name'
account_no_02_corporate = '123456789'
mobile_phone_corporate = '098645334'
employer_name_corporate = 'Employer name'
financial_institute_corporate = '3-Micro Finance'
isic_code_corporate = 'A011140'
classification_corporate = 'Vip'
country_of_income_corporate = 'Brazil'
staff_care_corporate = 'Cashier 006'
account_owner_referral_rm_corporate = 'Cashier 007'
account_operations_corporate = 'Cashier 008'
remark_field_to_add_corporate = 'Remark field to add corporate'
position_corporate = 'Position is Teprieu'
credit_line_corporate = '7,000,000,500.45'
currency_corporate = 'MMK'
mm_limit_corporate = '4,000,600,200.45'
currency_mm_corporate = 'MMK'
fx_limit_corporate = '9,000,500,500.45'
currency_fx_corporate = 'MMK'
# Institutional information - add
business_line_institutional = 'Institutional'
title_of_organization_institutional = 'School'
customer_type_institutional = 'Financial Institution/Non-Bank Financial Institution'
full_name_institutional = 'TEST AUTO ADD INSTITUTIONAL ' + str(date_time)
suffix_institutional = 'Dept.'
starting_date_of_company_institutional = '16/03/1999'
country_of_company_institutional = 'Armenia'
nationality_institutional = 'Bruneian'
paper_type_institutional = 'Other'
reason_for_other_paper_type_institutional = 'Reason for other paper type institutional'
paper_number_institutional = 'PP823' + random_num
tin_number_institutional = '043433444'
issue_date_of_paper_institutional = '16/03/1999'
issue_place_of_paper_institutional = 'Issue place of paper institutional'
expire_date_of_paper_institutional = '16/03/2099'
group_type_institutional = 'Managerial relationship'
group_sub_type_institutional = 'Partner of shareholder'
economic_sector_institutional = 'Other'
reason_for_other_economic_sector_institutional = 'Reason for other economic sector institutional'
sub_economic_sector_institutional = 'Other'
reason_for_other_sub_economic_sector_institutional = 'Reason for other sub economic sector institutional'
customer_segment_institutional = '3-VIP'
resident_status_institutional = 'Foreigner'
bank_identification_institutional = 'Shinhan'
fdi_info_institutional = 'FDI info institutional'
home_01_institutional = 'Home'
street_01_institutional = 'Street'
ward_01_institutional = 'Ward'
township_01_institutional = 'Township'
province_01_institutional = '12. Rakhine State'
home_02_institutional = 'Home'
street_02_institutional = 'Street'
ward_02_institutional = 'Ward'
township_02_institutional = 'Township'
province_02_institutional = '8. Magwe Division'
name_01_institutional = 'Name'
account_no_01_institutional = '123456789'
name_02_institutional = 'Name'
account_no_02_institutional = '123456789'
mobile_phone_institutional = '098645334'
employer_name_institutional = 'Employer name'
financial_institute_institutional = '3-Micro Finance'
isic_code_institutional = 'A011140'
classification_institutional = 'Vip'
country_of_income_institutional = 'Brazil'
staff_care_institutional = 'Cashier 006'
account_owner_referral_rm_institutional = 'Cashier 007'
account_operations_institutional = 'Cashier 008'
remark_field_to_add_institutional = 'Remark field to add institutional'
position_institutional = 'Position is Teprieu'
credit_line_institutional = '7,000,000,500.45'
currency_institutional = 'MMK'
mm_limit_institutional = '4,000,600,200.45'
currency_mm_institutional = 'MMK'
fx_limit_institutional = '9,000,500,500.45'
currency_fx_institutional = 'MMK'
# personal information - update
title_personal_update = 'Ms'
customer_sub_type_personal_update = 'Foreigner'
first_name_personal_update = 'TEST AUTO update'
last_name_personal_update = 'ADD personal up ' + str(date_time)
full_name_personal_update = first_name_personal_update.upper() + ' ' + last_name_personal_update.upper()
father_name_personal_update = 'Father name update'
gender_personal_update = 'Male'
date_of_birth_personal_update = '16/04/2002'
nationality_personal_update = 'Burkinabe'
# paper_number_personal_update = paper_number_personal
resident_status_personal_update = 'Diplomat'
home_01_personal_update = 'Home update'
street_01_personal_update = 'Street update'
ward_01_personal_update = 'Ward update'
township_01_personal_update = 'Township update'
home_02_personal_update = 'Home update'
street_02_personal_update = 'Street update'
ward_02_personal_update = 'Ward update'
township_02_personal_update = 'Township update'
name_01_personal_update = 'Name update'
account_no_01_personal_update = '123456999'
name_02_personal_update = 'Name update'
account_no_02_personal_update = '123456888'
mobile_phone_personal_update = '0986453333'
employer_name_personal_update = 'Employer name update'
occupation_personal_update = 'Other'
business_type_personal_update = 'Other'
reason_for_other_occupation_personal_update = 'Reason for other occupation personal update'
reason_for_other_business_type_personal_update = 'Reason for other business type personal update'
income_personal_update = '1,000,000 MMK to 2,500,000 MMK'
credit_line_personal_update = '2,000,050,000.45'
currency_personal_update = 'USD'
fx_limit_personal_update = '3,000,500,000.45'
currency_fx_personal_update = 'USD'
# data test media file
file_name_test = 'autotest_attach.jpg'
file_path_test = os.path.abspath(os.path.join(os.path.dirname(__file__), f'{main_path}{file_name_test}'))
business_line_test = 'Personal'
customer_name_test = full_name_personal_update
account_number_test = '000000000000'
dob_test=date_of_birth_personal_update
identification_test=paper_number_personal

class CustomerTest(FormAction):
    def get_url(self):
        return RUN_ON_URL

    def data_begin(self):
        # get username_reverse and password_reverse
        global username_approve, password_approve, username_reverse, password_reverse, username, password
        username_approve = USERNAME_APPROVE
        password_approve = PASSWORD_APPROVE
        username_reverse = USERNAME_REVERSE
        password_reverse = PASSWORD_REVERSE
        # get username and password
        username = USERNAME_LOGIN
        password = PASSWORD_LOGIN
        self.login(username, password, one_app=ONE_APP)
        global working_date, branch_code
        working_date = self.get_working_date()
        branch_code = self.get_logged_branch_code()

    def start_class(self):
        self.data_begin()

    def end_class(self):
        self.logout()

    def reset_browser(self):
        self.logout()
        self.restart_browser()
        self.data_begin()

# CUSTOMER PROFILE - CUSTOMER LINKAGE - CUSTOMER GROUP
    def test_001_customer_profile_add_personal_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global customer_code_personal_mask, customer_code_personal
        customer_code_personal_mask = self.customer_profile_add(
            business_line=business_line_personal,
            title=title_personal,
            customer_type=customer_type_personal,
            customer_sub_type=customer_sub_type_personal,
            first_name_en=first_name_personal,
            last_name_en=last_name_personal,
            full_name=full_name_personal,
            father_name=father_name_personal,
            gender=gender_personal,
            date_of_birth=date_of_birth_personal,
            nationality=nationality_personal,
            paper_type=paper_type_personal,
            paper_number=paper_number_personal,
            resident_status=resident_status_personal,
            home_01=home_01_personal,
            street_01=street_01_personal,
            ward_01=ward_01_personal,
            township_01=township_01_personal,
            home_02=home_02_personal,
            street_02=street_02_personal,
            ward_02=ward_02_personal,
            township_02=township_02_personal,
            name_01=name_01_personal,
            account_no_01=account_no_01_personal,
            name_02=name_02_personal,
            account_no_02=account_no_02_personal,
            mobile_phone=mobile_phone_personal,
            employer_name=employer_name_personal,
            occupation=occupation_personal,
            business_type=business_type_personal,
            reason_for_other_occupation=reason_for_other_occupation_personal,
            reason_for_other_business_type=reason_for_other_business_type_personal,
            income=income_personal,
            credit_line=credit_line_personal,
            currency=currency_personal,
            fx_limit=fx_limit_personal,
            currency_fx=currency_fx_personal
        )
        customer_code_personal = customer_code_personal_mask.replace('-', '')
        print('customer_code_personal no mask: ' + customer_code_personal)

    def test_002_customer_profile_add_sme_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global customer_code_sme_mask, customer_code_sme
        customer_code_sme_mask = self.customer_profile_add(
            business_line=business_line_sme,
            customer_type=customer_type_sme,
            full_name=full_name_sme,
            starting_date_of_company=starting_date_of_company_sme,
            nationality=nationality_sme,
            paper_type=paper_type_sme,
            paper_number=paper_number_sme,
            resident_status=resident_status_sme,
            home_01=home_01_sme,
            street_01=street_01_sme,
            ward_01=ward_01_sme,
            township_01=township_01_sme,
            home_02=home_02_sme,
            street_02=street_02_sme,
            ward_02=ward_02_sme,
            township_02=township_02_sme,
            name_01=name_01_sme,
            account_no_01=account_no_01_sme,
            name_02=name_02_sme,
            account_no_02=account_no_02_sme,
            mobile_phone=mobile_phone_sme,
            employer_name=employer_name_sme,
            country_of_income=country_of_income_sme,
            position=position_sme,
            credit_line=credit_line_sme,
            currency=currency_sme,
            fx_limit=fx_limit_sme,
            currency_fx=currency_fx_sme
        )
        customer_code_sme = customer_code_sme_mask.replace('-', '')
        print('customer_code_sme no mask: ' + customer_code_sme)

    def test_003_customer_profile_add_corporate_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global customer_code_corporate_mask, customer_code_corporate
        customer_code_corporate_mask = self.customer_profile_add(
            business_line=business_line_corporate,
            title_of_organization=title_of_organization_corporate,
            customer_type=customer_type_corporate,
            full_name=full_name_corporate,
            suffix=suffix_corporate,
            starting_date_of_company=starting_date_of_company_corporate,
            country_of_company=country_of_company_corporate,
            nationality=nationality_corporate,
            paper_type=paper_type_corporate,
            reason_for_other_paper_type=reason_for_other_paper_type_corporate,
            paper_number=paper_number_corporate,
            tin_number=tin_number_corporate,
            issue_date_of_paper=issue_date_of_paper_corporate,
            issue_place_of_paper=issue_place_of_paper_corporate,
            expire_date_of_paper=expire_date_of_paper_corporate,
            group_type=group_type_corporate,
            group_sub_type=group_sub_type_corporate,
            economic_sector=economic_sector_corporate,
            reason_for_other_economic_sector=reason_for_other_economic_sector_corporate,
            sub_economic_sector=sub_economic_sector_corporate,
            reason_for_other_sub_economic_sector=reason_for_other_sub_economic_sector_corporate,
            customer_segment=customer_segment_corporate,
            resident_status=resident_status_corporate,
            bank_identification=bank_identification_corporate,
            fdi_info=fdi_info_corporate,
            home_01=home_01_corporate,
            street_01=street_01_corporate,
            ward_01=ward_01_corporate,
            township_01=township_01_corporate,
            province_01=province_01_corporate,
            home_02=home_02_corporate,
            street_02=street_02_corporate,
            ward_02=ward_02_corporate,
            township_02=township_02_corporate,
            province_02=province_02_corporate,
            name_01=name_01_corporate,
            account_no_01=account_no_01_corporate,
            name_02=name_02_corporate,
            account_no_02=account_no_02_corporate,
            mobile_phone=mobile_phone_corporate,
            employer_name=employer_name_corporate,
            financial_institute=financial_institute_corporate,
            isic_code=isic_code_corporate,
            classification=classification_corporate,
            country_of_income=country_of_income_corporate,
            staff_care=staff_care_corporate,
            account_owner_referral_rm=account_owner_referral_rm_corporate,
            account_operations=account_operations_corporate,
            remark_field_to_add=remark_field_to_add_corporate,
            position=position_corporate,
            credit_line=credit_line_corporate,
            currency=currency_corporate,
            mm_limit=mm_limit_corporate,
            currency_mm=currency_mm_corporate,
            fx_limit=fx_limit_corporate,
            currency_fx=currency_fx_corporate
        )
        customer_code_corporate = customer_code_corporate_mask.replace('-', '')
        print('customer_code_corporate no mask: ' + customer_code_corporate)

    def test_004_customer_profile_add_institutional_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global customer_code_institutional_mask, customer_code_institutional
        customer_code_institutional_mask = self.customer_profile_add(
            business_line=business_line_institutional,
            title_of_organization=title_of_organization_institutional,
            customer_type=customer_type_institutional,
            full_name=full_name_institutional,
            suffix=suffix_institutional,
            starting_date_of_company=starting_date_of_company_institutional,
            country_of_company=country_of_company_institutional,
            nationality=nationality_institutional,
            paper_type=paper_type_institutional,
            reason_for_other_paper_type=reason_for_other_paper_type_institutional,
            paper_number=paper_number_institutional,
            tin_number=tin_number_institutional,
            issue_date_of_paper=issue_date_of_paper_institutional,
            issue_place_of_paper=issue_place_of_paper_institutional,
            expire_date_of_paper=expire_date_of_paper_institutional,
            group_type=group_type_institutional,
            group_sub_type=group_sub_type_institutional,
            economic_sector=economic_sector_institutional,
            reason_for_other_economic_sector=reason_for_other_economic_sector_institutional,
            sub_economic_sector=sub_economic_sector_institutional,
            reason_for_other_sub_economic_sector=reason_for_other_sub_economic_sector_institutional,
            customer_segment=customer_segment_institutional,
            resident_status=resident_status_institutional,
            bank_identification=bank_identification_institutional,
            fdi_info=fdi_info_institutional,
            home_01=home_01_institutional,
            street_01=street_01_institutional,
            ward_01=ward_01_institutional,
            township_01=township_01_institutional,
            province_01=province_01_institutional,
            home_02=home_02_institutional,
            street_02=street_02_institutional,
            ward_02=ward_02_institutional,
            township_02=township_02_institutional,
            province_02=province_02_institutional,
            name_01=name_01_institutional,
            account_no_01=account_no_01_institutional,
            name_02=name_02_institutional,
            account_no_02=account_no_02_institutional,
            mobile_phone=mobile_phone_institutional,
            employer_name=employer_name_institutional,
            financial_institute=financial_institute_institutional,
            isic_code=isic_code_institutional,
            classification=classification_institutional,
            country_of_income=country_of_income_institutional,
            staff_care=staff_care_institutional,
            account_owner_referral_rm=account_owner_referral_rm_institutional,
            account_operations=account_operations_institutional,
            remark_field_to_add=remark_field_to_add_institutional,
            position=position_institutional,
            credit_line=credit_line_institutional,
            currency=currency_institutional,
            mm_limit=mm_limit_institutional,
            currency_mm=currency_mm_institutional,
            fx_limit=fx_limit_institutional,
            currency_fx=currency_fx_institutional
        )
        customer_code_institutional = customer_code_institutional_mask.replace('-', '')
        print('customer_code_institutional no mask: ' + customer_code_institutional)

    def test_005_customer_profile_update_personal_pending_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        customer_code_actual_mask = self.customer_profile_update(
            customer_code=customer_code_personal_mask,
            title=title_personal_update,
            customer_sub_type=customer_sub_type_personal_update,
            first_name_en=first_name_personal_update,
            last_name_en=last_name_personal_update,
            full_name=full_name_personal_update,
            father_name=father_name_personal_update,
            gender=gender_personal_update,
            date_of_birth_starting_date_of_company=date_of_birth_personal_update,
            nationality=nationality_personal_update,
            resident_status=resident_status_personal_update,
            home_01=home_01_personal_update,
            street_01=street_01_personal_update,
            ward_01=ward_01_personal_update,
            township_01=township_01_personal_update,
            home_02=home_02_personal_update,
            street_02=street_02_personal_update,
            ward_02=ward_02_personal_update,
            township_02=township_02_personal_update,
            name_01=name_01_personal_update,
            account_no_01=account_no_01_personal_update,
            name_02=name_02_personal_update,
            account_no_02=account_no_02_personal_update,
            mobile_phone=mobile_phone_personal_update,
            employer_name=employer_name_personal_update,
            occupation=occupation_personal_update,
            business_type=business_type_personal_update,
            reason_for_other_occupation=reason_for_other_occupation_personal_update,
            reason_for_other_business_type=reason_for_other_business_type_personal_update,
            income=income_personal_update,
            credit_line=credit_line_personal_update,
            currency=currency_personal_update,
            fx_limit=fx_limit_personal_update,
            currency_fx=currency_fx_personal_update
        )
        self.assertEqual(customer_code_actual_mask, customer_code_personal_mask)

        self.customer_profile_view(
            customer_code=customer_code_personal_mask,
            business_line=business_line_personal,
            title=title_personal_update,
            customer_sub_type=customer_sub_type_personal_update,
            first_name_en=first_name_personal_update.upper(),
            last_name_en=last_name_personal_update.upper(),
            full_name=full_name_personal_update,
            father_name=father_name_personal_update.upper(),
            gender=gender_personal_update,
            date_of_birth_starting_date_of_company=date_of_birth_personal_update,
            nationality=nationality_personal_update,
            resident_status=resident_status_personal_update
        )
        customer_code_actual = customer_code_actual_mask.replace('-', '')
        print('customer_code_actual no mask: ' + customer_code_actual)

    def test_006_customer_profile_approve_corporate_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        ctm_apr_result = self.ctm_apr(
            customer_code=customer_code_corporate_mask,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        customer_code_mask=ctm_apr_result[1]
        self.assertEqual(customer_code_mask, customer_code_corporate_mask)

    def test_007_customer_linkage_update_pending_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        customer_code_actual_mask = self.customer_linkage_update(
            master_customer_code=customer_code_personal_mask,
            detail_customer_code=customer_code_corporate_mask,
            linkage_type='Or',
            linkage_description='Colleague_Colleague'
        )
        self.assertEqual(customer_code_actual_mask, customer_code_personal_mask)

        self.customer_linkage_view(
            master_customer_code=customer_code_personal_mask,
            linkage_description='Colleague_Colleague',
            linkage_status='Pending Approval'
        )
        customer_code_actual = customer_code_actual_mask.replace('-', '')
        print('customer_code_actual no mask: ' + customer_code_actual)

    def test_008_customer_profile_approve_personal_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        ctm_apr_result = self.ctm_apr(
            customer_code=customer_code_personal_mask,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        customer_code_mask=ctm_apr_result[1]
        self.assertEqual(customer_code_mask, customer_code_personal_mask)

    def test_009_customer_profile_update_personal_normal_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        customer_code_actual_mask = self.customer_profile_update(
            customer_code=customer_code_personal_mask,
            title=title_personal_update,
            customer_sub_type=customer_sub_type_personal_update,
            gender=gender_personal_update,
            date_of_birth_starting_date_of_company=date_of_birth_personal_update,
            nationality=nationality_personal_update,
            resident_status=resident_status_personal_update,
            name_01=name_01_personal_update,
            account_no_01=account_no_01_personal_update,
            name_02=name_02_personal_update,
            account_no_02=account_no_02_personal_update,
            employer_name=employer_name_personal_update,
            occupation=occupation_personal_update,
            business_type=business_type_personal_update,
            reason_for_other_occupation=reason_for_other_occupation_personal_update,
            reason_for_other_business_type=reason_for_other_business_type_personal_update,
            income=income_personal_update,
            credit_line=credit_line_personal_update,
            currency=currency_personal_update,
            fx_limit=fx_limit_personal_update,
            currency_fx=currency_fx_personal_update
        )
        self.assertEqual(customer_code_actual_mask, customer_code_personal_mask)

        customer_code_actual_mask = self.customer_approve_profile_modification_approve(
            customer_code=customer_code_personal_mask
        )
        self.assertEqual(customer_code_actual_mask, customer_code_personal_mask)

        self.customer_profile_view(
            customer_code=customer_code_personal_mask,
            business_line=business_line_personal,
            title=title_personal_update,
            customer_sub_type=customer_sub_type_personal_update,
            first_name_en=first_name_personal_update.upper(),
            last_name_en=last_name_personal_update.upper(),
            full_name=full_name_personal_update,
            father_name=father_name_personal_update.upper(),
            gender=gender_personal_update,
            date_of_birth_starting_date_of_company=date_of_birth_personal_update,
            nationality=nationality_personal_update,
            resident_status=resident_status_personal_update
        )
        customer_code_actual = customer_code_actual_mask.replace('-', '')
        print('customer_code_actual no mask: ' + customer_code_actual)

    def test_010_customer_linkage_update_normal_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        print('working_date: ' + working_date)
        customer_code_actual_mask = self.customer_linkage_update(
            master_customer_code=customer_code_personal_mask,
            linkage_description='Friend_Friend'
        )
        self.assertEqual(customer_code_actual_mask, customer_code_personal_mask)

        customer_code_actual_mask = self.customer_approve_linkage_modify_approve(
            master_customer_code=customer_code_personal_mask
        )
        self.assertEqual(customer_code_actual_mask, customer_code_personal_mask)

        self.customer_linkage_view(
            master_customer_code=customer_code_personal_mask,
            linkage_status='Normal',
            linkage_description='Friend_Friend'
        )
        customer_code_actual = customer_code_actual_mask.replace('-', '')
        print('customer_code_actual no mask: ' + customer_code_actual)

    def test_011_customer_group_update_pending_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        print('working_date: ' + working_date)
        customer_code_actual_mask = self.customer_relation_management_update(
            master_customer=customer_code_sme_mask,
            customer_code=customer_code_personal_mask,
            position='CEO of company'
        )
        self.assertEqual(customer_code_actual_mask, customer_code_sme_mask)

        self.customer_relation_management_view(
            master_customer=customer_code_sme_mask,
            group_status='Pending Approval'
        )
        customer_code_actual = customer_code_actual_mask.replace('-', '')
        print('customer_code_actual no mask: ' + customer_code_actual)

    def test_012_customer_group_update_normal_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        print('working_date: ' + working_date)
        customer_code_actual_mask = self.customer_relation_management_update(
            master_customer=customer_code_corporate_mask,
            customer_code=customer_code_personal_mask,
            position='CEO of company'
        )
        self.assertEqual(customer_code_actual_mask, customer_code_corporate_mask)

        customer_code_actual_mask = self.customer_approve_relation_management_modify_approve(
            master_customer=customer_code_corporate_mask
        )
        self.assertEqual(customer_code_actual_mask, customer_code_corporate_mask)

        self.customer_relation_management_view(
            master_customer=customer_code_corporate_mask,
            group_status='Normal'
        )
        customer_code_actual = customer_code_actual_mask.replace('-', '')
        print('customer_code_actual no mask: ' + customer_code_actual)

    def test_013_customer_profile_delete_personal_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        customer_code_delete = self.customer_profile_add(
            business_line=business_line_personal,
            title=title_personal,
            customer_type=customer_type_personal,
            customer_sub_type=customer_sub_type_personal,
            first_name_en=first_name_personal,
            last_name_en=last_name_personal,
            full_name=full_name_personal,
            father_name=father_name_personal,
            gender=gender_personal,
            date_of_birth=date_of_birth_personal,
            nationality=nationality_personal,
            paper_type=paper_type_personal,
            paper_number=f'DEL{paper_number_personal}',
            resident_status=resident_status_personal,
            home_01=home_01_personal,
            street_01=street_01_personal,
            ward_01=ward_01_personal,
            township_01=township_01_personal,
            home_02=home_02_personal,
            street_02=street_02_personal,
            ward_02=ward_02_personal,
            township_02=township_02_personal,
            name_01=name_01_personal,
            account_no_01=account_no_01_personal,
            name_02=name_02_personal,
            account_no_02=account_no_02_personal,
            mobile_phone=mobile_phone_personal,
            employer_name=employer_name_personal,
            occupation=occupation_personal,
            business_type=business_type_personal,
            reason_for_other_occupation=reason_for_other_occupation_personal,
            reason_for_other_business_type=reason_for_other_business_type_personal,
            income=income_personal,
            credit_line=credit_line_personal,
            currency=currency_personal,
            fx_limit=fx_limit_personal,
            currency_fx=currency_fx_personal
        )
        self.customer_profile_advanced_search(
            customer_code=customer_code_delete,
            date_of_birth_from=date_of_birth_personal,
            date_of_birth_to=date_of_birth_personal,
            # customer_status='Pending Approval',
            # branch_code='004 - Branch 004',
            open_date_from=working_date,
            open_date_to=working_date,
            paper_number=f'DEL{paper_number_personal}',
            full_name=full_name_personal,
            gender=gender_personal,
            nationality=nationality_personal,
        )
        self.assert_table_data('Customer code', 1, self.customer_code_mask(customer_code_delete))
        self.customer_profile_delete(
            customer_code=customer_code_delete,
        )

    def test_014_customer_profile_delete_sme_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        customer_code_delete = self.customer_profile_add(
            business_line=business_line_sme,
            customer_type=customer_type_sme,
            full_name=full_name_sme,
            starting_date_of_company=starting_date_of_company_sme,
            nationality=nationality_sme,
            paper_type=paper_type_sme,
            paper_number=f'DEL{paper_number_sme}',
            resident_status=resident_status_sme,
            home_01=home_01_sme,
            street_01=street_01_sme,
            ward_01=ward_01_sme,
            township_01=township_01_sme,
            home_02=home_02_sme,
            street_02=street_02_sme,
            ward_02=ward_02_sme,
            township_02=township_02_sme,
            name_01=name_01_sme,
            account_no_01=account_no_01_sme,
            name_02=name_02_sme,
            account_no_02=account_no_02_sme,
            mobile_phone=mobile_phone_sme,
            employer_name=employer_name_sme,
            country_of_income=country_of_income_sme,
            position=position_sme,
            credit_line=credit_line_sme,
            currency=currency_sme,
            fx_limit=fx_limit_sme,
            currency_fx=currency_fx_sme
        )
        self.customer_profile_advanced_search(
            customer_code=customer_code_delete,
            date_of_birth_from=starting_date_of_company_sme,
            date_of_birth_to=starting_date_of_company_sme,
            # customer_status='Pending Approval',
            # branch_code='004 - Branch 004',
            open_date_from=working_date,
            open_date_to=working_date,
            paper_number=f'DEL{paper_number_sme}',
            full_name=full_name_sme,
        )
        self.assert_table_data('Customer code', 1, self.customer_code_mask(customer_code_delete))
        self.customer_profile_delete(
            customer_code=customer_code_delete,
        )

    def test_015_customer_media_files_add_personal_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        customer_media_files_add_result = self.customer_media_files_add(
            file_path=file_path_test,
            customer_code=customer_code_personal_mask,
            business_line=business_line_test,
            customer_name=customer_name_test,
            account_number=account_number_test,
        )

    def test_016_customer_media_files_view_personal_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        customer_media_files_view_result = self.customer_media_files_view(
            customer_code=customer_code_personal_mask,
            business_line=business_line_test,
            customer_name=customer_name_test,
            account_number=account_number_test
        )

    def test_017_customer_media_files_update_personal_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        customer_media_files_update_result = self.customer_media_files_update(
            customer_code=customer_code_personal_mask,
            business_line=business_line_test,
            customer_name=customer_name_test,
            account_number=account_number_test,
        )

    def test_018_customer_media_files_approve_personal_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        customer_media_files_update_result = self.customer_media_files_approve(
            customer_code=customer_code_personal_mask,
        )

    def test_019_customer_media_files_get_information_personal_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        customer_media_files_update_result = self.customer_media_files_get_information(
            customer_code=customer_code_personal_mask,
            customer_name=customer_name_test,
            dob=dob_test,
            identification=identification_test
        )

    def test_020_customer_media_files_delete_personal_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.close_popup()
        customer_media_files_delete_result = self.customer_media_files_delete(
            customer_code=customer_code_personal_mask,
            media_name=file_name_test,
        )

if __name__ == '__main__': 
    webui_test.main()