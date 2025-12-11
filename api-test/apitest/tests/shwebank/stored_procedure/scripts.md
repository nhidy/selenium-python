# =========================== FO ===========================
# Folder chứa test scripts
cd api-test\apitest\tests\shwebank\stored_procedure\fo\

# DPT_OPN
py.test test_01_sp_dpt_opn.py --html=reports/test_01_sp_dpt_opn_results.html --self-contained-html
- `C#`: 
py.test test_01_sp_dpt_opn.py --html=reports/test_01_sp_dpt_opn_results_c#.html --self-contained-html
- `Stored procedure`: 
py.test test_01_sp_dpt_opn.py --html=reports/test_01_sp_dpt_opn_results_stored.html --self-contained-html

# DPT_APR
py.test test_02_sp_dpt_apr.py --html=reports/test_02_sp_dpt_apr_results.html --self-contained-html
- `C#`: 
py.test test_02_sp_dpt_apr.py --html=reports/test_02_sp_dpt_apr_results_c#.html --self-contained-html
- `Stored procedure`: 
py.test test_02_sp_dpt_apr.py --html=reports/test_02_sp_dpt_apr_results_stored.html --self-contained-html

# DPT_CDP
py.test test_03_sp_dpt_cdp.py --html=reports/test_03_sp_dpt_cdp_results.html --self-contained-html
- `C#`: 
py.test test_03_sp_dpt_cdp.py --html=reports/test_03_sp_dpt_cdp_results_c#.html --self-contained-html
- `Stored procedure`: 
py.test test_03_sp_dpt_cdp.py --html=reports/test_03_sp_dpt_cdp_results_stored.html --self-contained-html

# DPT_MDP
py.test test_04_sp_dpt_mdp.py --html=reports/test_04_sp_dpt_mdp_results.html --self-contained-html
- `C#`: 
py.test test_04_sp_dpt_mdp.py --html=reports/test_04_sp_dpt_mdp_results_c#.html --self-contained-html
- `Stored procedure`: 
py.test test_04_sp_dpt_mdp.py --html=reports/test_04_sp_dpt_mdp_results_stored.html --self-contained-html

# DPT_CWR
py.test test_05_sp_dpt_cwr.py --html=reports/test_05_sp_dpt_cwr_results.html --self-contained-html
- `C#`: 
py.test test_05_sp_dpt_cwr.py --html=reports/test_05_sp_dpt_cwr_results_c#.html --self-contained-html
- `Stored procedure`: 
py.test test_05_sp_dpt_cwr.py --html=reports/test_05_sp_dpt_cwr_results_stored.html --self-contained-html

# DPT_MWR
py.test test_06_sp_dpt_mwr.py --html=reports/test_06_sp_dpt_mwr_results.html --self-contained-html
- `C#`: 
py.test test_06_sp_dpt_mwr.py --html=reports/test_06_sp_dpt_mwr_results_c#.html --self-contained-html
- `Stored procedure`: 
py.test test_06_sp_dpt_mwr.py --html=reports/test_06_sp_dpt_mwr_results_stored.html --self-contained-html

# DPT_TRF
py.test test_07_sp_dpt_trf.py --html=reports/test_07_sp_dpt_trf_results.html --self-contained-html
- `C#`: 
py.test test_07_sp_dpt_trf.py --html=reports/test_07_sp_dpt_trf_results_c#.html --self-contained-html
- `Stored procedure`: 
py.test test_07_sp_dpt_trf.py --html=reports/test_07_sp_dpt_trf_results_stored.html --self-contained-html

# DPT_CWC
py.test test_08_sp_dpt_cwc.py --html=reports/test_08_sp_dpt_cwc_results.html --self-contained-html
- `C#`: 
py.test test_08_sp_dpt_cwc.py --html=reports/test_08_sp_dpt_cwc_results_c#.html --self-contained-html
- `Stored procedure`: 
py.test test_08_sp_dpt_cwc.py --html=reports/test_08_sp_dpt_cwc_results_stored.html --self-contained-html

# DPT_SBI
py.test test_09_sp_dpt_sbi.py --html=reports/test_09_sp_dpt_sbi_results.html --self-contained-html
- `C#`: 
py.test test_09_sp_dpt_sbi.py --html=reports/test_09_sp_dpt_sbi_results_c#.html --self-contained-html
- `Stored procedure`: 
py.test test_09_sp_dpt_sbi.py --html=reports/test_09_sp_dpt_sbi_results_stored.html --self-contained-html

# DPT_FBI
py.test test_11_sp_dpt_fbi.py --html=reports/test_11_sp_dpt_fbi_results.html --self-contained-html
- `C#`: 
py.test test_11_sp_dpt_fbi.py --html=reports/test_11_sp_dpt_fbi_results_c#.html --self-contained-html
- `Stored procedure`: 
py.test test_11_sp_dpt_fbi.py --html=reports/test_11_sp_dpt_fbi_results_stored.html --self-contained-html


# Test hàm
cd D:\2022_AutoTest\source-code\cbs-neptune-autotest\api-test\apitest\tests\shwebank\stored_procedure\fo\

py.test test_example.py --html=reports/test_example_results.html --self-contained-html

Link drive `CBS-SHWE_SP_ComparisonResults.xlsx`: https://docs.google.com/spreadsheets/d/1BFPa980E28jvYN2-XP2Qn6_V-C2H8S8l/edit?usp=sharing&ouid=115150936581368216240&rtpof=true&sd=true

