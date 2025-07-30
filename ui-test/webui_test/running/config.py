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

# S: view mode is "Status", N: view mode is "Normal"
class F8Config:
	view_mode = 'N'

class WaitConfig: 
	timeout_implicitly = 1
	timeout_explicit = 30