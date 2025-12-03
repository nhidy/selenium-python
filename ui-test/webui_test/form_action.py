from webui_test.case import *
from webui_test.actions.cash import CashActions
from webui_test.actions.credit import CreditActions
from webui_test.actions.customer import CustomerActions
from webui_test.actions.deposit import DepositActions
from webui_test.actions.overdraft import OverdraftActions
from webui_test.actions.stock import StockActions
from webui_test.actions.standing_instructions import StandingInstructionsActions
from webui_test.actions.sweeping import SweepingActions
from webui_test.actions.trade import TradeActions
from webui_test.actions.payment import PaymentActions
from webui_test.actions.mortgage import MortgageActions
from webui_test.actions.accounting import AccountingActions
from webui_test.actions.fixed_asset import FixedAssetActions
from webui_test.actions.treasury import TreasuryActions
from webui_test.actions.admin import AdminActions
from webui_test.actions.cardzone import CardzoneActions
from webui_test.actions.system_code_table import SystemCodeTableActions

class FormAction(
        CashActions,
        DepositActions,
        OverdraftActions,
        StockActions,
        StandingInstructionsActions,
        SweepingActions,
        CustomerActions,
        CreditActions,
        TradeActions,
        PaymentActions,
        MortgageActions,
        AccountingActions,
        FixedAssetActions,
        TreasuryActions,
        AdminActions,
        CardzoneActions,
        SystemCodeTableActions,
        TestCase
    ):
    pass