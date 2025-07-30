# CBS-Neptune-AutoTest



## Window server information
- Remote server 226 (use VPN HMC):
- Ip: 192.168.1.226
- User: jwellet
- Pass: R&DHCM

## Unbutu server information
- SSH server (use VPN CUS):
```
ssh root@27.3.1.113
Pass: 1
```

- URL go to project
```
cd /root/jits/cbs-neptune-autotest
python3 -m venv venv
source venv/bin/activate
```

- Install modules webui_test and build source
```
cd /root/jits/cbs-neptune-autotest/ui-test
python3 setup.py install 
```
- Output install
```
...
Successfully built webui_test
Installing collected packages: webui_test
Successfully installed webui_test-2.0.0
```

- Uninstall modules webui_test
```
cd /root/jits/cbs-neptune-autotest/ui-test
python3 -m pip uninstall webui_test
```
- Output uninstall
```
 Successfully uninstalled webui_test-2.0.0
```

- Run test UI
```
cd /root/jits/cbs-neptune-autotest/ui-test/tests
python3 run.py
```
**Note:** in the `run.py` file, the `headless` parameter must be `True`

- Get report
Share folder: https://hcm.jits.com.vn:8062/rndhcm/department/-/issues/171#note_79831
```
\\27.3.1.113
```
