import webui_test
from datetime import datetime
from webui_test.running.config import BrowserConfig

# t = datetime.datetime.today()
# print('Thoi gian hien tai truoc: ', t)
# future = datetime.datetime(t.year, t.month, t.day, 3, 0)
# if t.hour >= 3:
# 	future += datetime.timedelta(days=1)
# print('Thoi gian can chay: ', future)
# print('Thoi gian doi: ', (future-t).total_seconds())
# time.sleep((future-t).total_seconds())
# t2 = datetime.datetime.today()
# print('Thoi gian hien tai sau: ', t2)
browser='edge'
# browser='firefox'
# browser='chrome'
headless=False
if __name__ == '__main__':
# ----------------------------------------- ALL SHWE FO -----------------------------------------
    # webui_test.main(path="./test_dir/shwebank_posting/test_open_saving_and_deposit_withdrawal.py", browser=browser, debug=False, report=f"test_open_saving_and_deposit_withdrawal_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html", headless=headless)
    # webui_test.main(path="./test_dir/shwebank_posting/test_open_saving_and_deposit_cardzone.py", browser=browser, debug=False, report=f"test_open_saving_and_deposit_cardzone_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html", headless=headless)
    # webui_test.main(path="./test_dir/shwebank_posting/test_open_saving_and_deposit_withdrawal_diff_branch.py", browser=browser, debug=False, report=f"test_open_saving_and_deposit_withdrawal_diff_branch_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html", headless=headless)
    # webui_test.main(path="./test_dir/shwebank_posting/test_open_saving_and_deposit_withdrawal_diff_branch_reverse.py", browser=browser, debug=False, report=f"test_open_saving_and_deposit_withdrawal_diff_branch_reverse_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html", headless=headless)


    # webui_test.main(path="./test_dir/shwebank_integration/test_add_customer_and_open_deposit_account.py", browser=browser, debug=False, report=f"test_add_customer_and_open_deposit_account_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_integration/test_add_customer_and_open_deposit_account.py", browser=browser, debug=False, headless=headless, window_size="2340,1940", report=f"test_add_customer_and_open_deposit_account_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_integration/test_add_customer_and_open_deposit_account.py", browser=browser, debug=False, headless=headless, window_size="2340,740", report=f"test_add_customer_and_open_deposit_account_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_integration/test_add_customer_and_open_deposit_account.py", browser=browser, debug=False, headless=headless, window_size="1340,840", report=f"test_add_customer_and_open_deposit_account_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_integration/test_add_customer_and_open_deposit_account.py", browser=browser, debug=False, headless=headless, report=f"test_add_customer_and_open_deposit_account_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_integration/test_add_customer_and_open_deposit_account.py", browser=browser, debug=False, headless=headless, report=f"test_add_customer_and_open_deposit_account_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_integration/test_add_customer_and_open_deposit_account.py", browser=browser, debug=False, headless=headless, report=f"test_add_customer_and_open_deposit_account_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    

    # webui_test.main(path="./test_dir/shwebank_performance/deposit/test_account_information.py", browser=browser, debug=False, headless=headless, report=f"test_account_information_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")

    # webui_test.main(path="./test_dir/shwebank_performance/deposit/test_account_information_cashier003_10.py", browser=browser, debug=False, headless=headless, report=f"test_account_information_cashier003_10_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    

    # webui_test.main(path="./test_dir/shwebank_integration/test_method.py", browser=browser, debug=False, headless=headless, report=f"test_method_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_integration/test_method.py", browser=browser, debug=False, headless=headless, report=f"test_method_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_integration/test_method.py", browser=browser, debug=False, headless=headless, report=f"test_method_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")

    # webui_test.main(path="./test_dir/shwebank_integration/test_method.py", browser=browser, debug=False, headless=headless, report=f"test_method_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")


# ---------------------------------- FO - DEPOSIT - DATA GET FROM EXCEL FILE ----------------------------------
    # webui_test.main(path="./test_dir/shwebank_fo/deposit_xlsx/test_01_dpt_opn.py", browser=browser, debug=False, headless=headless, report=f"test_01_dpt_opn_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/deposit_xlsx/test_02_dpt_apr.py", browser=browser, debug=False, headless=headless, report=f"test_02_dpt_apr_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/deposit_xlsx/test_02_dpt_rej.py", browser=browser, debug=False, headless=headless, report=f"test_02_dpt_rej_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/deposit_xlsx/test_03_dpt_cdp.py", browser=browser, debug=False, headless=headless, report=f"test_03_dpt_cdp_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")

# ---------------------------------- FO - DEPOSIT ----------------------------------
    # webui_test.main(path="./test_dir/shwebank_fo/deposit/test_01_dpt_opn.py", browser=browser, debug=False, headless=headless, report=f"test_01_dpt_opn_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/deposit/test_02_dpt_apr.py", browser=browser, debug=False, headless=headless, report=f"test_02_dpt_apr_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/deposit/test_02_dpt_rej.py", browser=browser, debug=False, headless=headless, report=f"test_02_dpt_rej_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/deposit/test_03_dpt_cdp.py", browser=browser, debug=False, headless=headless, report=f"test_03_dpt_cdp_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/deposit/test_03_dpt_mdp.py", browser=browser, debug=False, headless=headless, report=f"test_03_dpt_mdp_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/deposit/test_04_dpt_trf.py", browser=browser, debug=False, headless=headless, report=f"test_04_dpt_trf_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/deposit/test_05_dpt_cwr.py", browser=browser, debug=False, headless=headless, report=f"test_05_dpt_cwr_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/deposit/test_05_dpt_mwr.py", browser=browser, debug=False, headless=headless, report=f"test_05_dpt_mwr_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/deposit/test_06_dpt_cas.py", browser=browser, debug=False, headless=headless, report=f"test_06_dpt_cas_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/deposit/test_07_dpt_blk.py", browser=browser, debug=False, headless=headless, report=f"test_07_dpt_blk_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/deposit/test_08_dpt_rls.py", browser=browser, debug=False, headless=headless, report=f"test_08_dpt_rls_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/deposit/test_09_dpt_ifc.py", browser=browser, debug=False, headless=headless, report=f"test_09_dpt_ifc_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/deposit/test_10_dpt_cip.py", browser=browser, debug=False, headless=headless, report=f"test_10_dpt_cip_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/deposit/test_10_dpt_dip.py", browser=browser, debug=False, headless=headless, report=f"test_10_dpt_dip_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/deposit/test_10_dpt_mip.py", browser=browser, debug=False, headless=headless, report=f"test_10_dpt_mip_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/deposit/test_11_dpt_emk.py", browser=browser, debug=False, headless=headless, report=f"test_11_dpt_emk_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/deposit/test_12_dpt_erl.py", browser=browser, debug=False, headless=headless, report=f"test_12_dpt_erl_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/deposit/test_13_dpt_fee.py", browser=browser, debug=False, headless=headless, report=f"test_13_dpt_fee_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/deposit/test_13_dpt_foc.py", browser=browser, debug=False, headless=headless, report=f"test_13_dpt_foc_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/deposit/test_14_dpt_rctm.py", browser=browser, debug=False, headless=headless, report=f"test_14_dpt_rctm_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/deposit/test_15_dpt_cls.py", browser=browser, debug=False, headless=headless, report=f"test_15_dpt_cls_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/deposit/test_15_dpt_dls.py", browser=browser, debug=False, headless=headless, report=f"test_15_dpt_dls_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/deposit/test_15_dpt_mls.py", browser=browser, debug=False, headless=headless, report=f"test_15_dpt_mls_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/deposit/test_16_dpt_his.py", browser=browser, debug=False, headless=headless, report=f"test_16_dpt_his_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")


# ---------------------------------- FO - ACCOUNTING ----------------------------------
    # webui_test.main(path="./test_dir/shwebank_fo/accounting/test_01_act_fee.py", browser=browser, debug=False, headless=headless, report=f"test_01_act_fee_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/accounting/test_02_act_gfee.py", browser=browser, debug=False, headless=headless, report=f"test_02_act_gfee_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/accounting/test_03_act_man.py", browser=browser, debug=False, headless=headless, report=f"test_03_act_man_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")

# ---------------------------------- FO - CUSTOMER ----------------------------------
    # webui_test.main(path="./test_dir/shwebank_fo/customer/test_01_ctm_apr.py", browser=browser, debug=False, headless=headless, report=f"test_01_ctm_apr_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/customer/test_02_ctm_ccn.py", browser=browser, debug=False, headless=headless, report=f"test_02_ctm_ccn_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/customer/test_03_ctm_cpn.py", browser=browser, debug=False, headless=headless, report=f"test_03_ctm_cpn_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/customer/test_04_ctm_cas.py", browser=browser, debug=False, headless=headless, report=f"test_04_ctm_cas_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")

# ---------------------------------- FO - STOCK ----------------------------------
    # webui_test.main(path="./test_dir/shwebank_fo/stock/test_01_dpt_srg.py", browser=browser, debug=False, headless=headless, report=f"test_01_dpt_srg_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/stock/test_02_dpt_sab.py", browser=browser, debug=False, headless=headless, report=f"test_02_dpt_sab_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/stock/test_03_dpt_sra.py", browser=browser, debug=False, headless=headless, report=f"test_03_dpt_sra_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/stock/test_03_dpt_ccr.py", browser=browser, debug=False, headless=headless, report=f"test_03_dpt_ccr_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/stock/test_04_dpt_sat.py", browser=browser, debug=False, headless=headless, report=f"test_04_dpt_sat_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/stock/test_05_dpt_crt.py", browser=browser, debug=False, headless=headless, report=f"test_05_dpt_crt_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")

# ---------------------------------- FO - STOCK - CHEQUE ----------------------------------
    # webui_test.main(path="./test_dir/shwebank_fo/stock/test_06_dpt_cis.py", browser=browser, debug=False, headless=headless, report=f"test_06_dpt_cis_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/stock/test_07_dpt_cei.py", browser=browser, debug=False, headless=headless, report=f"test_07_dpt_cei_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/stock/test_08_dpt_rec.py", browser=browser, debug=False, headless=headless, report=f"test_08_dpt_rec_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/stock/test_09_dpt_cdt.py", browser=browser, debug=False, headless=headless, report=f"test_09_dpt_cdt_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/stock/test_09_dpt_cwc.py", browser=browser, debug=False, headless=headless, report=f"test_09_dpt_cwc_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/stock/test_09_dpt_cwm.py", browser=browser, debug=False, headless=headless, report=f"test_09_dpt_cwm_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/stock/test_10_dpt_cts.py", browser=browser, debug=False, headless=headless, report=f"test_10_dpt_cts_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/stock/test_11_dpt_ciq.py", browser=browser, debug=False, headless=headless, report=f"test_11_dpt_ciq_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/stock/test_12_dpt_sls.py", browser=browser, debug=False, headless=headless, report=f"test_12_dpt_sls_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")

# ---------------------------------- FO - STOCK - PASSBOOK FOR SAVINGS ----------------------------------
    # webui_test.main(path="./test_dir/shwebank_fo/stock/test_06_dpt_sbi.py", browser=browser, debug=False, headless=headless, report=f"test_06_dpt_sbi_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")

# ---------------------------------- FO - STOCK - PASSBOOK FOR FIXED DEPOSIT ----------------------------------
    # webui_test.main(path="./test_dir/shwebank_fo/stock/test_06_dpt_fbi.py", browser=browser, debug=False, headless=headless, report=f"test_06_dpt_fbi_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")

# ---------------------------------- FO - STOCK - RECEIPT FOR PREPAID FIXED DEPOSIT ----------------------------------
    # webui_test.main(path="./test_dir/shwebank_fo/stock/test_06_dpt_cer.py", browser=browser, debug=False, headless=headless, report=f"test_06_dpt_cer_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")

# ---------------------------------- FO - STOCK - PAYMENT ORDER ----------------------------------
    # webui_test.main(path="./test_dir/shwebank_fo/stock/test_06_dpt_poi.py", browser=browser, debug=False, headless=headless, report=f"test_06_dpt_poi_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/stock/test_07_dpt_pow.py", browser=browser, debug=False, headless=headless, report=f"test_07_dpt_pow_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/stock/test_07_dpt_rpo.py", browser=browser, debug=False, headless=headless, report=f"test_07_dpt_rpo_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")

# ---------------------------------- FO - STOCK - GIFT CHEQUE ----------------------------------
    # webui_test.main(path="./test_dir/shwebank_fo/stock/test_06_dpt_cci.py", browser=browser, debug=False, headless=headless, report=f"test_06_dpt_cci_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/stock/test_07_dpt_ccw.py", browser=browser, debug=False, headless=headless, report=f"test_07_dpt_ccw_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/stock/test_07_dpt_rcc.py", browser=browser, debug=False, headless=headless, report=f"test_07_dpt_rcc_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")

# ---------------------------------- FO - MORTGAGE ----------------------------------
    # webui_test.main(path="./test_dir/shwebank_fo/mortgage/test_01_mtg_opn.py", browser=browser, debug=False, headless=headless, report=f"test_01_mtg_opn_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/mortgage/test_02_mtg_apr.py", browser=browser, debug=False, headless=headless, report=f"test_02_mtg_apr_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")

# ---------------------------------- FO - TREASURY - FOREX ----------------------------------
    # webui_test.main(path="./test_dir/shwebank_fo/treasury/test_01_tfx_ofo.py", browser=browser, debug=False, headless=headless, report=f"test_01_tfx_ofo_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/treasury/test_02_tfx_fac.py", browser=browser, debug=False, headless=headless, report=f"test_02_tfx_fac_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/treasury/test_02_tfx_fca.py", browser=browser, debug=False, headless=headless, report=f"test_02_tfx_fca_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/treasury/test_02_tfx_oaa.py", browser=browser, debug=False, headless=headless, report=f"test_02_tfx_oaa_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")

# ---------------------------------- FO - TRADE FINANCE ----------------------------------
    # webui_test.main(path="./test_dir/shwebank_fo/trade_finance/test_01_trd_sni.py", browser=browser, debug=False, headless=headless, report=f"test_01_trd_sni_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/trade_finance/test_02_trd_document_attachment.py", browser=browser, debug=False, headless=headless, report=f"test_02_trd_document_attachment_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/trade_finance/test_02_trd_siv.py", browser=browser, debug=False, headless=headless, report=f"test_02_trd_siv_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/trade_finance/test_03_trd_sbx.py", browser=browser, debug=False, headless=headless, report=f"test_03_trd_sbx_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/trade_finance/test_05_trd_scl.py", browser=browser, debug=False, headless=headless, report=f"test_05_trd_scl_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/trade_finance/test_02_trd_gsc.py", browser=browser, debug=False, headless=headless, report=f"test_02_trd_gsc_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/trade_finance/test_04_trd_rsc.py", browser=browser, debug=False, headless=headless, report=f"test_04_trd_rsc_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_fo/trade_finance/test_03_trd_fcc.py", browser=browser, debug=False, headless=headless, report=f"test_03_trd_fcc_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")

# ---------------------------------- FO - OTHERS ----------------------------------
    # webui_test.main(path="./test_dir/shwebank_fo/others/test_01_fx_transaction.py", browser=browser, debug=False, headless=headless, report=f"test_01_fx_transaction_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")

# ---------------------------------- FO - CASH ----------------------------------
    # webui_test.main(path="./test_dir/shwebank_fo/cash/test_csh_dnm.py", browser=browser, debug=False, headless=headless, report=f"test_csh_dnm_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")

# ---------------------------------- BO - CUSTOMER ----------------------------------
    # webui_test.main(path="./test_dir/shwebank_bo/customer/test_01_customer_profile.py", browser=browser, debug=False, headless=headless, report=f"test_01_customer_profile_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")


# ---------------------------------- BO - DEPOSIT ----------------------------------
    # webui_test.main(path="./test_dir/shwebank_bo/deposit/test_01_catalogue_definition.py", browser=browser, debug=False, headless=headless, report=f"test_01_catalogue_definition_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_bo/deposit/test_02_account_information.py", browser=browser, debug=False, headless=headless, report=f"test_02_account_information_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_bo/deposit/test_03_account_linkage.py", browser=browser, debug=False, headless=headless, report=f"test_03_account_linkage_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_bo/deposit/test_04_stock_inventory.py", browser=browser, debug=False, headless=headless, report=f"test_04_stock_inventory_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")


# ---------------------------------- BO - ACCOUNTING ----------------------------------
    # webui_test.main(path="./test_dir/shwebank_bo/accounting/test_01_bank_account_definition.py", browser=browser, debug=False, headless=headless, report=f"test_01_bank_account_definition_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")

# ---------------------------------- REGRESSION TEST ----------------------------------
    # webui_test.main(path="./test_dir/shwebank_regression/test_regression.py", browser=browser, debug=False, headless=headless, report=f"test_regression_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_regression/test_regression_forex.py", browser=browser, debug=False, headless=headless, report=f"test_regression_forex_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_regression/test_regression_trade.py", browser=browser, debug=False, headless=headless, report=f"test_regression_trade_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_regression/test_regression_trade_no_approve.py", browser=browser, debug=False, headless=headless, report=f"test_regression_trade_no_approve_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    
    # webui_test.main(path="./test_dir/shwebank_regression/test_regression_issue_4237.py", browser=browser, debug=False, headless=headless, report=f"test_regression_issue_4237_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_regression/test_01_regression_customer.py", browser=browser, debug=False, headless=headless, report=f"test_01_regression_customer_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_regression/test_02_regression_deposit_current.py", browser=browser, debug=False, headless=headless, report=f"test_02_regression_deposit_current_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_regression/test_03_regression_deposit_s1_savings.py", browser=browser, debug=False, headless=headless, report=f"test_03_regression_deposit_s1_savings_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_regression/test_04_regression_deposit_t1_fd_no_rollover.py", browser=browser, debug=False, headless=headless, report=f"test_04_regression_deposit_t1_fd_no_rollover_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_regression/test_04_regression_deposit_t1_fd_pri_plus_int_rollover.py", browser=browser, debug=False, headless=headless, report=f"test_04_regression_deposit_t1_fd_pri_plus_int_rollover_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    webui_test.main(path="./test_dir/shwebank_regression/test_04_regression_deposit_t1_fd_pri_rollover_only.py", browser=browser, debug=False, headless=headless, report=f"test_04_regression_deposit_t1_fd_pri_rollover_only_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_regression/test_02_regression_deposit_current_new.py", browser=browser, debug=False, headless=headless, report=f"test_02_regression_deposit_current_new_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_regression/test_regression_mortgage.py", browser=browser, debug=False, headless=headless, report=f"test_regression_mortgage_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_regression/test_regression_fixed_asset.py", browser=browser, debug=False, headless=headless, report=f"test_regression_fixed_asset_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_regression/test_regression_credit.py", browser=browser, debug=False, headless=headless, report=f"test_regression_credit_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_regression/test_regression_payment.py", browser=browser, debug=False, headless=headless, report=f"test_regression_payment_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_regression/test_regression_deposit_payment_order.py", browser=browser, debug=False, headless=headless, report=f"test_regression_deposit_payment_order_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
    # webui_test.main(path="./test_dir/shwebank_regression/test_regression_deposit_gift_cheque.py", browser=browser, debug=False, headless=headless, report=f"test_regression_deposit_gift_cheque_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")


# ---------------------------------- REGRESSION TEST 117 ----------------------------------
    # webui_test.main(path="./test_dir/shwebank_regression/test_regression_117.py", browser=browser, debug=False, headless=headless, report=f"test_regression_117_{browser}_result_" + datetime.now().strftime('%d%m%Y_%H%M%S') + ".html")
