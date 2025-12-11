import pytest 
import json


from apitest.src.configs import USER_LOGIN
from apitest.src.utilities.requestUtility import RequestUtility
from apitest.src.helpers.accounting.account_chart_helpers import AccountChartHelper
from apitest.src.helpers.accounting.account_clearing_helpers import AccountClearingHelper
from apitest.src.helpers.accounting.account_common_helpers import AccountCommonHelper
from apitest.src.helpers.accounting.account_group_detail_helpers import AccountGroupDetailHelper
from apitest.src.helpers.accounting.account_group_helpers import AccountGroupHelper
from apitest.src.helpers.accounting.account_mapping_detail_helpers import AccountMappingDetailHelper
from apitest.src.helpers.accounting.account_mapping_helpers import AccountMappingHelper
from apitest.src.helpers.accounting.extension_account_helpers import ExtensionAccountHelper
from apitest.src.helpers.accounting.foreign_exchange_account_helpers import ForeignExchangeAccountHelper
from apitest.src.helpers.accounting.group_of_account_helpers import GroupOfAccountHelper
from apitest.src.helpers.admin.branch_helpers import BranchHelper
from apitest.src.helpers.admin.calendar_helpers import CalendarHelper
from apitest.src.helpers.admin.code_list_helpers import CodeListHelper
from apitest.src.helpers.admin.company_helpers import CompanyHelper
from apitest.src.helpers.admin.country_helpers import CountryHelper
from apitest.src.helpers.admin.currency_helpers import CurrencyHelper
from apitest.src.helpers.admin.department_helpers import DepartmentHelper
from apitest.src.helpers.admin.role_of_user_helpers import RoleOfUserHelper
from apitest.src.helpers.admin.user_account_helpers import UserAccountHelper
from apitest.src.helpers.admin.user_limit_helpers import UserLimitHelper
from apitest.src.helpers.admin.user_policy_helpers import UserPolicyHelper
from apitest.src.helpers.admin.user_right_helpers import UserRightHelper
from apitest.src.helpers.admin.user_role_helpers import UserRoleHelper
from apitest.src.helpers.cash.cash_list_helpers import CashListHelper
from apitest.src.helpers.cash.cash_statement_helpers import CashStatementHelper
from apitest.src.helpers.cash.cash_transaction_helpers import CashTransactionHelper
from apitest.src.helpers.cash.denomination_balance_helpers import DenominationBalanceHelper
from apitest.src.helpers.cash.denomination_helpers import DenominationHelper
from apitest.src.helpers.cash.denomination_statement_helpers import DenominationStatementHelper
from apitest.src.helpers.cash.denomination_transaction_helpers import DenominationTransactionHelper
from apitest.src.helpers.credit.credit_account_helpers import CreditAccountHelper
from apitest.src.helpers.credit.credit_approve_account_helpers import CreditApproveAccountHelper
from apitest.src.helpers.credit.credit_catalog_helpers import CreditCatalogHelper
from apitest.src.helpers.credit.group_limit_helpers import GroupLimitHelper
from apitest.src.helpers.credit.product_limit_helpers import ProductLimitHelper
from apitest.src.helpers.credit.sub_product_limit_helpers import SubProductLimitHelper
from apitest.src.helpers.customer.customer_group_helpers import CustomerGroupHelper
from apitest.src.helpers.customer.customer_linkage_helpers import CustomerLinkageHelper
from apitest.src.helpers.customer.customer_media_helpers import CustomerMediaHelper
from apitest.src.helpers.customer.customer_single_helpers import CustomerSingleHelper
from apitest.src.helpers.deposit.clearing_check_helpers import ClearingCheckHelper
from apitest.src.helpers.deposit.deposit_account_helpers import DepositAccountHelper
from apitest.src.helpers.deposit.deposit_approve_account_helpers import DepositApproveAccountHelper
from apitest.src.helpers.deposit.deposit_catalog_helpers import DepositCatalogHelper
from apitest.src.helpers.deposit.stock_inventory_helpers import StockInventoryHelper
from apitest.src.helpers.deposit.stock_status_helpers import StockStatusHelper
from apitest.src.helpers.deposit.stock_transaction_helpers import StockTransactionHelper
from apitest.src.helpers.fixed_asset.fixed_asset_account_helpers import FixedAssetAccountHelper
from apitest.src.helpers.fixed_asset.fixed_asset_catalog_helpers import FixedAssetCatalogHelper
from apitest.src.helpers.foreign_exchange.foreign_exchange_helpers import ForeignExchangeHelper
from apitest.src.helpers.ifc.ifc_auto_fee_helpers import IFCAutoFeeHelper
from apitest.src.helpers.ifc.ifc_balance_helpers import IFCBalanceHelper
from apitest.src.helpers.ifc.ifc_definition_helpers import IFCDefinitionHelper
from apitest.src.helpers.ifc.ifc_tariff_helpers import IFCTariffHelper
from apitest.src.helpers.ifc.ifc_transaction_helpers import IFCTransactionHelper
from apitest.src.helpers.ifc.tariff_helpers import TariffHelper
from apitest.src.helpers.mortgage.mortgage_account_helpers import MortgageAccountHelper
from apitest.src.helpers.mortgage.mortgage_balance_helpers import MortgageBalanceHelper
from apitest.src.helpers.mortgage.mortgage_catalog_helpers import MortgageCatalogHelper
from apitest.src.helpers.mortgage.mortgage_history_helpers import MortgageHistoryHelper
from apitest.src.helpers.mortgage.mortgage_transaction_helpers import MortgageTransactionHelper
from apitest.src.helpers.payment.account_linkage_helpers import AccountLinkageHelper
from apitest.src.helpers.payment.correspondent_bank_helpers import CorrespondentBankHelper
from apitest.src.helpers.payment.fund_transfer_via_fast_helpers import FundTransferViaFastHelper
from apitest.src.helpers.payment.instruction_group_helpers import InstructionGroupHelper
from apitest.src.helpers.payment.instruction_item_helpers import InstructionItemHelper
from apitest.src.helpers.payment.payment_catalog_helpers import PaymentCatalogHelper
from apitest.src.helpers.payment.payment_queue_for_inward_helpers import PaymentQueueForInwardHelper
from apitest.src.helpers.payment.payment_queue_for_outward_helpers import PaymentQueueForOutwardHelper
from apitest.src.helpers.payment.po_management_helpers import PoManagementHelper
# from apitest.src.helpers.neptune_helpers import NeptuneHelper

from apitest.src.payloads.accounting.account_chart_payload import AccountChartPayload
from apitest.src.payloads.accounting.account_clearing_payload import AccountClearingPayload
from apitest.src.payloads.accounting.account_common_payload import AccountCommonPayload
from apitest.src.payloads.accounting.account_group_detail_payload import AccountGroupDetailPayload
from apitest.src.payloads.accounting.account_group_payload import AccountGroupPayload
from apitest.src.payloads.accounting.account_mapping_detail_payload import AccountMappingDetailPayload
from apitest.src.payloads.accounting.account_mapping_payload import AccountMappingPayload
from apitest.src.payloads.accounting.extension_account_payload import ExtensionAccountPayload
from apitest.src.payloads.accounting.foreign_exchange_account_payload import ForeignExchangeAccountPayload
from apitest.src.payloads.accounting.group_of_account_payload import GroupOfAccountPayload
from apitest.src.payloads.admin.branch_payload import BranchPayload
from apitest.src.payloads.admin.calendar_payload import CalendarPayload
from apitest.src.payloads.admin.code_list_payload import CodeListPayload
from apitest.src.payloads.admin.company_payload import CompanyPayload
from apitest.src.payloads.admin.country_payload import CountryPayload
from apitest.src.payloads.admin.currency_payload import CurrencyPayload
from apitest.src.payloads.admin.department_payload import DepartmentPayload
from apitest.src.payloads.admin.role_of_user_payload import RoleOfUserPayload
from apitest.src.payloads.admin.user_account_payload import UserAccountPayload
from apitest.src.payloads.admin.user_limit_payload import UserLimitPayload
from apitest.src.payloads.admin.user_policy_payload import UserPolicyPayload
from apitest.src.payloads.admin.user_right_payload import UserRightPayload
from apitest.src.payloads.admin.user_role_payload import UserRolePayload
from apitest.src.payloads.cash.cash_list_payload import CashListPayload
from apitest.src.payloads.cash.cash_statement_payload import CashStatementPayload
from apitest.src.payloads.cash.cash_transaction_payload import CashTransactionPayload
from apitest.src.payloads.cash.denomination_balance_payload import DenominationBalancePayload
from apitest.src.payloads.cash.denomination_payload import DenominationPayload
from apitest.src.payloads.cash.denomination_statement_payload import DenominationStatementPayload
from apitest.src.payloads.cash.denomination_transaction_payload import DenominationTransactionPayload
from apitest.src.payloads.credit.credit_account_payload import CreditAccountPayload
from apitest.src.payloads.credit.credit_approve_account_payload import CreditApproveAccountPayload
from apitest.src.payloads.credit.credit_catalog_payload import CreditCatalogPayload
from apitest.src.payloads.credit.group_limit_payload import GroupLimitPayload
from apitest.src.payloads.credit.product_limit_payload import ProductLimitPayload
from apitest.src.payloads.credit.sub_product_limit_payload import SubProductLimitPayload
from apitest.src.payloads.customer.customer_group_payload import CustomerGroupPayload
from apitest.src.payloads.customer.customer_linkage_payload import CustomerLinkagePayload
from apitest.src.payloads.customer.customer_single_payload import CustomerSinglePayload
from apitest.src.payloads.deposit.clearing_check_payload import ClearingCheckPayload
from apitest.src.payloads.deposit.deposit_account_payload import DepositAccountPayload
from apitest.src.payloads.deposit.deposit_approve_account_payload import DepositApproveAccountPayload
from apitest.src.payloads.deposit.deposit_catalog_payload import DepositCatalogPayload
from apitest.src.payloads.deposit.stock_inventory_payload import StockInventoryPayload
from apitest.src.payloads.deposit.stock_status_payload import StockStatusPayload
from apitest.src.payloads.deposit.stock_transaction_payload import StockTransactionPayload
from apitest.src.payloads.fixed_asset.fixed_asset_account_payload import FixedAssetAccountPayload
from apitest.src.payloads.fixed_asset.fixed_asset_catalog_payload import FixedAssetCatalogPayload
from apitest.src.payloads.foreign_exchange.foreign_exchange_payload import ForeignExchangePayload
from apitest.src.payloads.ifc.ifc_auto_fee_payload import IFCAutoFeePayload
from apitest.src.payloads.ifc.ifc_balance_payload import IFCBalancePayload
from apitest.src.payloads.ifc.ifc_definition_payload import IFCDefinitionPayload
from apitest.src.payloads.ifc.ifc_tariff_payload import IFCTariffPayload
from apitest.src.payloads.ifc.ifc_transaction_payload import IFCTransactionPayload
from apitest.src.payloads.ifc.tariff_payload import TariffPayload
from apitest.src.payloads.mortgage.mortgage_account_payload import MortgageAccountPayload
from apitest.src.payloads.mortgage.mortgage_balance_payload import MortgageBalancePayload
from apitest.src.payloads.mortgage.mortgage_catalog_payload import MortgageCatalogPayload
from apitest.src.payloads.mortgage.mortgage_history_payload import MortgageHistoryPayload
from apitest.src.payloads.mortgage.mortgage_transaction_payload import MortgageTransactionPayload
from apitest.src.payloads.payment.account_linkage_payload import AccountLinkagePayload
from apitest.src.payloads.payment.correspondent_bank_payload import CorrespondentBankPayload
from apitest.src.payloads.payment.fund_transfer_via_fast_payload import FundTransferViaFastPayload
from apitest.src.payloads.payment.instruction_group_payload import InstructionGroupPayload
from apitest.src.payloads.payment.instruction_item_payload import InstructionItemPayload
from apitest.src.payloads.payment.payment_catalog_payload import PaymentCatalogPayload
from apitest.src.payloads.payment.payment_queue_for_inward_payload import PaymentQueueForInwardPayload
from apitest.src.payloads.payment.payment_queue_for_outward_payload import PaymentQueueForOutwardPayload
from apitest.src.payloads.payment.po_management_payload import PoManagementPayload


account_chart_payload = AccountChartPayload()
account_clearing_payload = AccountClearingPayload()
account_common_payload = AccountCommonPayload()
account_group_detail_payload = AccountGroupDetailPayload()
account_group_payload = AccountGroupPayload()
account_mapping_detail_payload = AccountMappingDetailPayload()
account_mapping_payload = AccountMappingPayload()
extension_account_payload = ExtensionAccountPayload()
foreign_exchange_account_payload = ForeignExchangeAccountPayload()
group_of_account_payload = GroupOfAccountPayload()
branch_payload = BranchPayload()
calendar_payload = CalendarPayload()
code_list_payload = CodeListPayload()
company_payload = CompanyPayload()
country_payload = CountryPayload()
currency_payload = CurrencyPayload()
department_payload = DepartmentPayload()
role_of_user_payload = RoleOfUserPayload()
user_account_payload = UserAccountPayload()
user_limit_payload = UserLimitPayload()
user_policy_payload = UserPolicyPayload()
user_right_payload = UserRightPayload()
user_role_payload = UserRolePayload()
cash_list_payload = CashListPayload()
cash_statement_payload = CashStatementPayload()
cash_transaction_payload = CashTransactionPayload()
denomination_balance_payload = DenominationBalancePayload()
denomination_payload = DenominationPayload()
denomination_statement_payload = DenominationStatementPayload()
denomination_transaction_payload = DenominationTransactionPayload()
credit_account_payload = CreditAccountPayload()
credit_approve_account_payload = CreditApproveAccountPayload()
credit_catalog_payload = CreditCatalogPayload()
group_limit_payload = GroupLimitPayload()
product_limit_payload = ProductLimitPayload()
sub_product_limit_payload = SubProductLimitPayload()
customer_group_payload = CustomerGroupPayload()
customer_linkage_payload = CustomerLinkagePayload()
customer_single_payload = CustomerSinglePayload()
clearing_check_payload = ClearingCheckPayload()
deposit_account_payload = DepositAccountPayload()
deposit_approve_account_payload = DepositApproveAccountPayload()
deposit_catalog_payload = DepositCatalogPayload()
stock_inventory_payload = StockInventoryPayload()
stock_status_payload = StockStatusPayload()
stock_transaction_payload = StockTransactionPayload()
fixed_asset_account_payload = FixedAssetAccountPayload()
fixed_asset_catalog_payload = FixedAssetCatalogPayload()
foreign_exchange_payload = ForeignExchangePayload()
ifc_auto_fee_payload = IFCAutoFeePayload()
ifc_balance_payload = IFCBalancePayload()
ifc_definition_payload = IFCDefinitionPayload()
ifc_tariff_payload = IFCTariffPayload()
ifc_transaction_payload = IFCTransactionPayload()
tariff_payload = TariffPayload()
mortgage_account_payload = MortgageAccountPayload()
mortgage_balance_payload = MortgageBalancePayload()
mortgage_catalog_payload = MortgageCatalogPayload()
mortgage_history_payload = MortgageHistoryPayload()
mortgage_transaction_payload = MortgageTransactionPayload()
account_linkage_payload = AccountLinkagePayload()
correspondent_bank_payload = CorrespondentBankPayload()
fund_transfer_via_fast_payload = FundTransferViaFastPayload()
instruction_group_payload = InstructionGroupPayload()
instruction_item_payload = InstructionItemPayload()
payment_catalog_payload = PaymentCatalogPayload()
payment_queue_for_inward_payload = PaymentQueueForInwardPayload()
payment_queue_for_outward_payload = PaymentQueueForOutwardPayload()
po_management_payload = PoManagementPayload()

expected_status = 'Completed'
@pytest.fixture(scope='session')
def user():
    user_service = USER_LOGIN['user1']
    req = RequestUtility(user_service)
    req.login_neptune()
    req.login_service()
    return req


@pytest.mark.test_search_response_neptune
class TestSearchResponseNeptune(object):
# ============================= accounting =============================
    @pytest.mark.simple_search_account_chart
    def test_simple_search_account_chart(self, user):
        helper = AccountChartHelper(user)
        payload = account_chart_payload.simple_search(
            page_size=10
        )
        rs = helper.ACT_ACCHRT_SER_SIMPLE(fields_data=payload)

        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.advanced_search_account_chart
    def test_advanced_search_account_chart(self, user):
        helper = AccountChartHelper(user)
        payload = account_chart_payload.advanced_search(
            page_size=10
        )
        rs = helper.ACT_ACCHRT_SER_ADVANCE(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.simple_search_account_clearing
    def test_simple_search_account_clearing(self, user):
        helper = AccountClearingHelper(user)
        payload = account_clearing_payload.simple_search(
            page_size=10
        )
        rs = helper.ACT_ACCLR_SER_SIMPLE(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.advanced_search_account_clearing
    def test_advanced_search_account_clearing(self, user):
        helper = AccountClearingHelper(user)
        payload = account_clearing_payload.advanced_search(
            page_size=10
        )
        rs = helper.ACT_ACCLR_SER_ADVANCE(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.simple_search_account_common
    def test_simple_search_account_common(self, user):
        helper = AccountCommonHelper(user)
        payload = account_common_payload.simple_search(
            page_size=10
        )
        rs = helper.ACT_ACCOM_SER_SIMPLE(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.advanced_search_account_common
    def test_advanced_search_account_common(self, user):
        helper = AccountCommonHelper(user)
        payload = account_common_payload.advanced_search(
            page_size=10
        )
        rs = helper.ACT_ACCOM_SER_ADVANCE(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.simple_search_account_group_detail
    def test_simple_search_account_group_detail(self, user):
        helper = AccountGroupDetailHelper(user)
        payload = account_group_detail_payload.simple_search(
            page_size=10
        )
        rs = helper.ACT_ACGRPDEFDTL_SER_SIMPLE(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.advanced_search_account_group_detail
    def test_advanced_search_account_group_detail(self, user):
        helper = AccountGroupDetailHelper(user)
        payload = account_group_detail_payload.advanced_search(
            page_size=10
        )
        rs = helper.ACT_ACGRPDEFDTL_SER_ADVANCE(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.simple_search_account_group
    def test_simple_search_account_group(self, user):
        helper = AccountGroupHelper(user)
        payload = account_group_payload.simple_search(
            page_size=10
        )
        rs = helper.ACT_ACGRPDEF_SER_SIMPLE(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.advanced_search_account_group
    def test_advanced_search_account_group(self, user):
        helper = AccountGroupHelper(user)
        payload = account_group_payload.advanced_search(
            page_size=10
        )
        rs = helper.ACT_ACGRPDEF_SER_ADVANCE(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.simple_search_account_mapping
    def test_simple_search_account_mapping(self, user):
        helper = AccountMappingHelper(user)
        payload = account_mapping_payload.simple_search(
            page_size=10
        )
        rs = helper.ACT_ACMAP_SER_SIMPLE(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.advanced_search_account_mapping
    def test_advanced_search_account_mapping(self, user):
        helper = AccountMappingHelper(user)
        payload = account_mapping_payload.advanced_search(
            page_size=10
        )
        rs = helper.ACT_ACMAP_SER_ADVANCE(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.simple_search_extension_account
    def test_simple_search_extension_account(self, user):
        helper = ExtensionAccountHelper(user)
        payload = extension_account_payload.simple_search(
            page_size=10
        )
        rs = helper.ACT_ACGLDEF_SER_SIMPLE(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.advanced_search_extension_account
    def test_advanced_search_extension_account(self, user):
        helper = ExtensionAccountHelper(user)
        payload = extension_account_payload.advanced_search(
            page_size=10
        )
        rs = helper.ACT_ACGLDEF_SER_ADVANCE(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.simple_search_foreign_exchange_account
    def test_simple_search_foreign_exchange_account(self, user):
        helper = ForeignExchangeAccountHelper(user)
        payload = foreign_exchange_account_payload.simple_search(
            page_size=10
        )
        rs = helper.ACT_FXCLR_SER_SIMPLE(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.advanced_search_foreign_exchange_account
    def test_advanced_search_foreign_exchange_account(self, user):
        helper = ForeignExchangeAccountHelper(user)
        payload = foreign_exchange_account_payload.advanced_search(
            page_size=10
        )
        rs = helper.ACT_FXCLR_SER_ADVANCE(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.simple_search_group_of_account
    def test_simple_search_group_of_account(self, user):
        helper = GroupOfAccountHelper(user)
        payload = group_of_account_payload.simple_search(
            page_size=10
        )
        rs = helper.ACT_ACGRP_SER_SIMPLE(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.advanced_search_group_of_account
    def test_advanced_search_group_of_account(self, user):
        helper = GroupOfAccountHelper(user)
        payload = group_of_account_payload.advanced_search(
            page_size=10
        )
        rs = helper.ACT_ACGRP_SER_ADVANCE(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


# ============================= admin =============================
    @pytest.mark.simple_search_branch
    def test_simple_search_branch(self, user):
        helper = BranchHelper(user)
        payload = branch_payload.simple_search(
            page_size=10
        )
        rs = helper.ADM_SIMPLE_SEARCH_BRANCH(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.advanced_search_branch
    def test_advanced_search_branch(self, user):
        helper = BranchHelper(user)
        payload = branch_payload.advanced_search(
            page_size=10
        )
        rs = helper.ADM_ADVANCED_SEARCH_BRANCH(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.simple_search_code_list
    def test_simple_search_code_list(self, user):
        helper = CodeListHelper(user)
        payload = code_list_payload.simple_search(
            page_size=10
        )
        rs = helper.ADM_SIMPLE_SEARCH_CODE_LIST(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.advanced_search_code_list
    def test_advanced_search_code_list(self, user):
        helper = CodeListHelper(user)
        payload = code_list_payload.advanced_search(
            page_size=10
        )
        rs = helper.ADM_ADVANCED_SEARCH_CODE_LIST(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.simple_search_company
    def test_simple_search_company(self, user):
        helper = CompanyHelper(user)
        payload = company_payload.simple_search(
            page_size=10
        )
        rs = helper.ADM_SIMPLE_SEARCH_COMPANY(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.advanced_search_company
    def test_advanced_search_company(self, user):
        helper = CompanyHelper(user)
        payload = company_payload.advanced_search(
            page_size=10
        )
        rs = helper.ADM_ADVANCED_SEARCH_COMPANY(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.simple_search_country
    def test_simple_search_country(self, user):
        helper = CountryHelper(user)
        payload = country_payload.simple_search(
            page_size=10
        )
        rs = helper.ADM_SIMPLE_SEARCH_COUNTRY(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.advanced_search_country
    def test_advanced_search_country(self, user):
        helper = CountryHelper(user)
        payload = country_payload.advanced_search(
            page_size=10
        )
        rs = helper.ADM_ADVANCED_SEARCH_COUNTRY(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.simple_search_currency
    def test_simple_search_currency(self, user):
        helper = CurrencyHelper(user)
        payload = currency_payload.simple_search(
            page_size=10
        )
        rs = helper.ADM_SIMPLE_SEARCH_CURRENCY(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.advanced_search_currency
    def test_advanced_search_currency(self, user):
        helper = CurrencyHelper(user)
        payload = currency_payload.advanced_search(
            page_size=10
        )
        rs = helper.ADM_ADVANCED_SEARCH_CURRENCY(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.simple_search_department
    def test_simple_search_department(self, user):
        helper = DepartmentHelper(user)
        payload = department_payload.simple_search(
            page_size=10
        )
        rs = helper.ADM_SIMPLE_SEARCH_DEPARTMENT(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.advanced_search_department
    def test_advanced_search_department(self, user):
        helper = DepartmentHelper(user)
        payload = department_payload.advanced_search(
            page_size=10
        )
        rs = helper.ADM_ADVANCED_SEARCH_DEPARTMENT(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.simple_search_user_account
    def test_simple_search_user_account(self, user):
        helper = UserAccountHelper(user)
        payload = user_account_payload.simple_search(
            page_size=10
        )
        rs = helper.ADM_SIMPLE_SEARCH_USER_ACCOUNT(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.advanced_search_user_account
    def test_advanced_search_user_account(self, user):
        helper = UserAccountHelper(user)
        payload = user_account_payload.advanced_search(
            page_size=10
        )
        rs = helper.ADM_ADVANCED_SEARCH_USER_ACCOUNT(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.simple_search_user_policy
    def test_simple_search_user_policy(self, user):
        helper = UserPolicyHelper(user)
        payload = user_policy_payload.simple_search(
            page_size=10
        )
        rs = helper.ADM_SIMPLE_SEARCH_USER_POLICY(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.advanced_search_user_policy
    def test_advanced_search_user_policy(self, user):
        helper = UserPolicyHelper(user)
        payload = user_policy_payload.advanced_search(
            page_size=10
        )
        rs = helper.ADM_ADVANCED_SEARCH_USER_POLICY(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

# ============================= cash =============================
    @pytest.mark.simple_search_denomination
    def test_simple_search_denomination(self, user):
        helper = DenominationHelper(user)
        payload = denomination_payload.simple_search(
            page_size=10
        )
        rs = helper.CSH_DENOM_SER_SIMPLE(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.advanced_search_denomination
    def test_advanced_search_denomination(self, user):
        helper = DenominationHelper(user)
        payload = denomination_payload.advanced_search(
            page_size=10
        )
        rs = helper.CSH_DENOM_SER_ADVANCE(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

# ============================= credit =============================
    @pytest.mark.simple_search_credit_account
    def test_simple_search_credit_account(self, user):
        helper = CreditAccountHelper(user)
        payload = credit_account_payload.simple_search(
            page_size=10
        )
        rs = helper.CRD_SEARCH_SP_CREDIT(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.advanced_search_credit_account
    def test_advanced_search_credit_account(self, user):
        helper = CreditAccountHelper(user)
        payload = credit_account_payload.advanced_search(
            page_size=10
        )
        rs = helper.CRD_SEARCH_ADV_CREDIT(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    # @pytest.mark.simple_search_credit_approve_account
    # def test_simple_search_credit_approve_account(self, user):
    #     helper = CreditApproveAccountHelper(user)
    #     payload = credit_approve_account_payload.simple_search(
    #         page_size=10
    #     )
    #     rs = helper.(payload)
    #     assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    # @pytest.mark.advance_search_credit_approve_account
    # def test_advance_search_credit_approve_account(self, user):
    #     helper = CreditApproveAccountHelper(user)
    #     payload = credit_approve_account_payload.advanced_search(
    #         page_size=10
    #     )
    #     rs = helper.(payload)
    #     assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.simple_search_credit_catalog
    def test_simple_search_credit_catalog(self, user):
        helper = CreditCatalogHelper(user)
        payload = credit_catalog_payload.simple_search(
            page_size=10
        )
        rs = helper.CRD_SEARCH_SP_CRDCAT(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.advanced_search_credit_catalog
    def test_advanced_search_credit_catalog(self, user):
        helper = CreditCatalogHelper(user)
        payload = credit_catalog_payload.advanced_search(
            page_size=10
        )
        rs = helper.CRD_SEARCH_ADV_CRDCAT(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.simple_search_group_limit
    def test_simple_search_group_limit(self, user):
        helper = GroupLimitHelper(user)
        payload = group_limit_payload.simple_search(
            page_size=10
        )
        rs = helper.CRD_SEARCH_SP_CRDGRPLM(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.advanced_search_group_limit
    def test_advanced_search_group_limit(self, user):
        helper = GroupLimitHelper(user)
        payload = group_limit_payload.advanced_search(
            page_size=10
        )
        rs = helper.CRD_SEARCH_ADV_CRDGRPLM(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.simple_search_product_limit
    def test_simple_search_product_limit(self, user):
        helper = ProductLimitHelper(user)
        payload = product_limit_payload.simple_search(
            page_size=10
        )
        rs = helper.CRD_SEARCH_SP_CRDPL(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.advanced_search_product_limit
    def test_advanced_search_product_limit(self, user):
        helper = ProductLimitHelper(user)
        payload = product_limit_payload.advanced_search(
            page_size=10
        )
        rs = helper.CRD_SEARCH_ADV_CRDPL(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.simple_search_sub_product_limit
    def test_simple_search_sub_product_limit(self, user):
        helper = SubProductLimitHelper(user)
        payload = sub_product_limit_payload.simple_search(
            page_size=10
        )
        rs = helper.CRD_SEARCH_SP_CRDSPL(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.advanced_search_sub_product_limit
    def test_advanced_search_sub_product_limit(self, user):
        helper = SubProductLimitHelper(user)
        payload = sub_product_limit_payload.advanced_search(
            page_size=10
        )
        rs = helper.CRD_SEARCH_ADV_CRDSPL(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


# ============================= customer =============================
    @pytest.mark.simple_search_customer_single
    def test_simple_search_customer_single(self, user):
        helper = CustomerSingleHelper(user)
        payload = customer_single_payload.simple_search(
            page_size=10
        )
        rs = helper.SQL_SEARCH_CTM(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.advanced_search_customer_single
    def test_advanced_search_customer_single(self, user):
        helper = CustomerSingleHelper(user)
        payload = customer_single_payload.advanced_search(
            page_size=10
        )
        rs = helper.SQL_ADSEARCH_CTM(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.simple_search_customer_group
    def test_simple_search_customer_group(self, user):
        helper = CustomerGroupHelper(user)
        payload = customer_group_payload.simple_search(
            page_size=10
        )
        rs = helper.SQL_SEARCH_CTMGRP(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.advanced_search_customer_group
    def test_advanced_search_customer_group(self, user):
        helper = CustomerGroupHelper(user)
        payload = customer_group_payload.advanced_search(
            page_size=10
        )
        rs = helper.SQL_ADSEARCH_CTMGRP(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.simple_search_customer_linkage
    def test_simple_search_customer_linkage(self, user):
        helper = CustomerLinkageHelper(user)
        payload = customer_linkage_payload.simple_search(
            page_size=10
        )
        rs = helper.SQL_SEARCH_CTMLKG(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.advanced_search_customer_linkage
    def test_advanced_search_customer_linkage(self, user):
        helper = CustomerLinkageHelper(user)
        payload = customer_linkage_payload.advanced_search(
            page_size=10
        )
        rs = helper.SQL_ADSEARCH_CTMLKG(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


# ============================= deposit =============================
    @pytest.mark.simple_search_deposit_account
    def test_simple_search_deposit_account(self, user):
        helper = DepositAccountHelper(user)
        payload = deposit_account_payload.simple_search(
            page_size=10
        )
        rs = helper.DPT_SEARCH_DEPOSIT(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.advanced_search_deposit_account
    def test_advanced_search_deposit_account(self, user):
        helper = DepositAccountHelper(user)
        payload = deposit_account_payload.advanced_search(
            page_size=10
        )
        rs = helper.DPT_ADSEARCH_DEPOSIT(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    # @pytest.mark.simple_search_deposit_approve_account
    # def test_simple_search_deposit_approve_account(self, user):
    #     helper = DepositApproveAccountHelper(user)
    #     payload = deposit_approve_account_payload.simple_search(
    #         page_size=10
    #     )
    #     rs = helper.(payload)
    #     assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    # @pytest.mark.advanced_search_deposit_approve_account
    # def test_advanced_search_deposit_approve_account(self, user):
    #     helper = DepositApproveAccountHelper(user)
    #     payload = deposit_approve_account_payload.advanced_search(
    #         page_size=10
    #     )
    #     rs = helper.(payload)
    #     assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.simple_search_deposit_catalog
    def test_simple_search_deposit_catalog(self, user):
        helper = DepositCatalogHelper(user)
        payload = deposit_catalog_payload.simple_search(
            page_size=10
        )
        rs = helper.DPT_SEARCH_CATALOG(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.advanced_search_deposit_catalog
    def test_advanced_search_deposit_catalog(self, user):
        helper = DepositCatalogHelper(user)
        payload = deposit_catalog_payload.advanced_search(
            page_size=10
        )
        rs = helper.DPT_ADSEARCH_CATALOG(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.simple_search_stock_inventory
    def test_simple_search_stock_inventory(self, user):
        helper = StockInventoryHelper(user)
        payload = stock_inventory_payload.simple_search(
            page_size=10
        )
        rs = helper.DPT_SEARCH_STOCKINVENTORY(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.advanced_search_stock_inventory
    def test_advanced_search_stock_inventory(self, user):
        helper = StockInventoryHelper(user)
        payload = stock_inventory_payload.advanced_search(
            page_size=10
        )
        rs = helper.DPT_ADSEARCH_STOCKINVENTORY(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

# ============================= fixed_asset =============================
    @pytest.mark.simple_search_fixed_asset_account
    def test_simple_search_fixed_asset_account(self, user):
        helper = FixedAssetAccountHelper(user)
        payload = fixed_asset_account_payload.simple_search(
            page_size=10
        )
        rs = helper.SQL_SEARCH_FACACT(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.advanced_search_fixed_asset_account
    def test_advanced_search_fixed_asset_account(self, user):
        helper = FixedAssetAccountHelper(user)
        payload = fixed_asset_account_payload.advanced_search(
            page_size=10
        )
        rs = helper.SQL_ADSEARCH_FACACT(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.simple_search_fixed_asset_catalog
    def test_simple_search_fixed_asset_catalog(self, user):
        helper = FixedAssetCatalogHelper(user)
        payload = fixed_asset_catalog_payload.simple_search(
            page_size=10
        )
        rs = helper.SQL_SEARCH_FACCAT(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.advanced_search_fixed_asset_catalog
    def test_advanced_search_fixed_asset_catalog(self, user):
        helper = FixedAssetCatalogHelper(user)
        payload = fixed_asset_catalog_payload.advanced_search(
            page_size=10
        )
        rs = helper.SQL_ADSEARCH_FACCAT(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


# ============================= foreign_exchange =============================

# ============================= ifc =============================
    @pytest.mark.simple_search_ifc_auto_fee
    def test_simple_search_ifc_auto_fee(self, user):
        helper = IFCAutoFeeHelper(user)
        payload = ifc_auto_fee_payload.simple_search(
            page_size=10
        )
        rs = helper.IFC_SEARCH_IFCAUTOFEE(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.advanced_search_ifc_auto_fee
    def test_advanced_search_ifc_auto_fee(self, user):
        helper = IFCAutoFeeHelper(user)
        payload = ifc_auto_fee_payload.advanced_search(
            page_size=10
        )
        rs = helper.IFC_ADSEARCH_IFCAUTOFEE(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.simple_search_ifc_definition
    def test_simple_search_ifc_definition(self, user):
        helper = IFCDefinitionHelper(user)
        payload = ifc_definition_payload.simple_search(
            page_size=10
        )
        rs = helper.IFC_SEARCH_IFC(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.advanced_search_ifc_definition
    def test_advanced_search_ifc_definition(self, user):
        helper = IFCDefinitionHelper(user)
        payload = ifc_definition_payload.advanced_search(
            page_size=10
        )
        rs = helper.IFC_ADSEARCH_IFC(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.simple_search_tariff
    def test_simple_search_tariff(self, user):
        helper = TariffHelper(user)
        payload = tariff_payload.simple_search(
            page_size=10
        )
        rs = helper.IFC_SEARCH_TARIFF(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.advanced_search_tariff
    def test_advanced_search_tariff(self, user):
        helper = TariffHelper(user)
        payload = tariff_payload.advanced_search(
            page_size=10
        )
        rs = helper.IFC_ADSEARCH_TARIFF(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'


# ============================= mortgage =============================
    @pytest.mark.simple_search_mortgage_account
    def test_simple_search_mortgage_account(self, user):
        helper = MortgageAccountHelper(user)
        payload = mortgage_account_payload.simple_search(
            page_size=10
        )
        rs = helper.MTG_SIMPLE_SEARCH_MORTGAGE_ACCOUNT(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.advanced_search_mortgage_account
    def test_advanced_search_mortgage_account(self, user):
        helper = MortgageAccountHelper(user)
        payload = mortgage_account_payload.advanced_search(
            page_size=10
        )
        rs = helper.MTG_ADVANCED_SEARCH_MORTGAGE_ACCOUNT(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.simple_search_mortgage_catalog
    def test_simple_search_mortgage_catalog(self, user):
        helper = MortgageCatalogHelper(user)
        payload = mortgage_catalog_payload.simple_search(
            page_size=10
        )
        rs = helper.MTG_SIMPLE_SEARCH_MORTGAGE_CATALOG(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.advanced_search_mortgage_catalog
    def test_advanced_search_mortgage_catalog(self, user):
        helper = MortgageCatalogHelper(user)
        payload = mortgage_catalog_payload.advanced_search(
            page_size=10
        )
        rs = helper.MTG_ADVANCED_SEARCH_MORTGAGE_CATALOG(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

# ============================= payment =============================
    @pytest.mark.simple_search_account_linkage
    def test_simple_search_account_linkage(self, user):
        helper = AccountLinkageHelper(user)
        payload = account_linkage_payload.simple_search(
            page_size=10
        )
        rs = helper.PMT_SEARCH_SP_ACLINKAGE(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.advanced_search_account_linkage
    def test_advanced_search_account_linkage(self, user):
        helper = AccountLinkageHelper(user)
        payload = account_linkage_payload.advanced_search(
            page_size=10
        )
        rs = helper.PMT_SEARCH_ADV_ACLINKAGE(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.simple_search_correspondent_bank
    def test_simple_search_correspondent_bank(self, user):
        helper = CorrespondentBankHelper(user)
        payload = correspondent_bank_payload.simple_search(
            page_size=10
        )
        rs = helper.PMT_SEARCH_SP_AGENTBANK(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.advanced_search_correspondent_bank
    def test_advanced_search_correspondent_bank(self, user):
        helper = CorrespondentBankHelper(user)
        payload = correspondent_bank_payload.advanced_search(
            page_size=10
        )
        rs = helper.PMT_SEARCH_ADV_AGENTBANK(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    # @pytest.mark.simple_search_fund_transfer_via_fast
    # def test_simple_search_fund_transfer_via_fast(self, user):
    #     helper = FundTransferViaFastHelper(user)
    #     payload = fund_transfer_via_fast_payload.simple_search(
    #         page_size=10
    #     )
    #     rs = helper.(payload)
    #     assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    # @pytest.mark.advanced_search_fund_transfer_via_fast
    # def test_advanced_search_fund_transfer_via_fast(self, user):
    #     helper = FundTransferViaFastHelper(user)
    #     payload = fund_transfer_via_fast_payload.advanced_search(
    #         page_size=10
    #     )
    #     rs = helper.(payload)
    #     assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.simple_search_payment_catalog
    def test_simple_search_payment_catalog(self, user):
        helper = PaymentCatalogHelper(user)
        payload = payment_catalog_payload.simple_search(
            page_size=10
        )
        rs = helper.PMT_SEARCH_SP_PMTCAT(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    @pytest.mark.advanced_search_payment_catalog
    def test_advanced_search_payment_catalog(self, user):
        helper = PaymentCatalogHelper(user)
        payload = payment_catalog_payload.advanced_search(
            page_size=10
        )
        rs = helper.PMT_SEARCH_ADV_PMTCAT(payload)
        assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
        assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    # @pytest.mark.simple_search_payment_queue_for_inward
    # def test_simple_search_payment_queue_for_inward(self, user):
    #     helper = PaymentQueueForInwardHelper(user)
    #     payload = payment_queue_for_inward_payload.simple_search(
    #         page_size=10
    #     )
    #     rs = helper.(payload)
    #     assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    # @pytest.mark.advanced_search_payment_queue_for_inward
    # def test_advanced_search_payment_queue_for_inward(self, user):
    #     helper = PaymentQueueForInwardHelper(user)
    #     payload = payment_queue_for_inward_payload.advanced_search(
    #         page_size=10
    #     )
    #     rs = helper.(payload)
    #     assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    # @pytest.mark.simple_search_payment_queue_for_outward
    # def test_simple_search_payment_queue_for_outward(self, user):
    #     helper = PaymentQueueForOutwardHelper(user)
    #     payload = payment_queue_for_outward_payload.simple_search(
    #         page_size=10
    #     )
    #     rs = helper.(payload)
    #     assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    # @pytest.mark.advanced_search_payment_queue_for_outward
    # def test_advanced_search_payment_queue_for_outward(self, user):
    #     helper = PaymentQueueForOutwardHelper(user)
    #     payload = payment_queue_for_outward_payload.advanced_search(
    #         page_size=10
    #     )
    #     rs = helper.(payload)
    #     assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'

    # @pytest.mark.simple_search_po_management
    # def test_simple_search_po_management(self, user):
    #     helper = PoManagementHelper(user)
    #     payload = po_management_payload.simple_search(
    #         page_size=10
    #     )
    #     rs = helper.(payload)
    #     assert 'total_count' in rs, f'Key \"total_count\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'total_pages' in rs, f'Key \"total_pages\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'has_next_page' in rs, f'Key \"has_next_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'has_previous_page' in rs, f'Key \"has_previous_page\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'items' in rs, f'Key \"items\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'page_index' in rs, f'Key \"page_index\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'
    #     assert 'page_size' in rs, f'Key \"page_size\" does not exist. Response Json: {json.dumps(rs, indent=4, sort_keys=True)}'