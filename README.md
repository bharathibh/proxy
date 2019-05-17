# Proxy

[![Build Status](https://travis-ci.org/bharathibh/proxy.svg?branch=master)](https://travis-ci.org/bharathibh/proxy)
### Demo
Unblock sites like facebook, twitter on your workplace on windows

![Proxy Demo](https://media.giphy.com/media/VGna5NWkXPa78SuqAX/giphy.gif 'Preview')

### How to
Download the zip from the following link
[cloud.zip](https://github.com/bharathibh/proxy/raw/master/cloud.zip)
Just run `cloud.exe` from the extracted content.

## Utils used
Thanks for these great tools
  - [Ultrasurf](https://ultrasurf.us/)
  - [ieproxy.exe](https://github.com/DanStevens/ieproxy)

## How it works!

**By redirecting all our requests to Ultrasurf server**

This simple tool will run in background and control Ultrasurf right from your system tray icon.
![Context Menu](https://i.ibb.co/f05gpBJ/context.png 'Context Menu')

  - this tool will download Ultrasurf and `ieproxy.exe` binaries on the windows' `%temp% / usurf` folder
  - then the it will start Ultrasurf in the background with no window
 
When **Connect**ing, it will download ultrasurf and `ieproxy.exe` into `%temp% / usurf` folder
When **Disconnect**ing, ultrasurf process will stop and System Proxy settings will be cleared by `ieproxy.exe`

**Note: If you're using proxy server for internet, then please update these varaibles**
- `ProxyHost`
- `ProxyPort`

on the file `%temp% / usurf / u.ini`

Please let me know if you have any suggestions or comments.
[![Twitter](http://i.imgur.com/tXSoThF.png)](https://twitter.com/bharathi_bh)
