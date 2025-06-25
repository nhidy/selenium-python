## Automation UI Testing tool

In general, the Bot is a wrapper around `Selenium`, helps to automate JWEBUI. Besides the basic features of Selenium, its provides additional features:
- APIs to test JWEBUI easly by finding the element by visible text, by value, by spcecific properties. These high-level APIs helps tester writes test cases easier. The scripts are shorter, easier to read.
- APIs to do comparisons between the JWEBUI screen elements with the expected results, eg.: compare the notification show after finish the transaction, the table row value,...
- APIs to automate chain of actions: login, logout, open transaction, close popup, close voucher, ...  
- The Bot can support the most common web browsers: Safari, Edge, Chrome, Firefox. 
- Can run on different OS: Linux, Windows, MacOS,...
- Configs for screen resolution. 
- Ships with its own copies of web drivers, so the testers don't need to download or config the needed drivers.
- Configs to run a specific test case, a test file or a whole test folder (test suite).
- Auto captures the screen if the test cases fail.