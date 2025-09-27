class WebUI_Test: 
    driver = None
    timeout = 10
    debug = False

class BrowserConfig:
    name = None
    report_path = None
    headless = False
    window_size = '1900,1080'
    run_file = True
    url_env = None
    is_old = 'N' # N: run on new UI (default); Y: run on old UI
    on_server = 'Y' # Y: run on server; N: run on local
    app_name = None

# S: view mode is "Status", N: view mode is "Normal"
class F8Config:
    view_mode = None

class WaitConfig: 
    timeout_implicitly = 1
    timeout_explicit = 30