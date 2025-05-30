#!/bin/sh

polipo proxyAddress="0.0.0.0" proxyPort=5000 socksParentProxy=127.0.0.1:9050 socksProxyType=socks5 diskCacheRoot='' disableLocalInterface=true localDocumentRoot='' disableConfiguration=true dnsUseGethostbyname='yes' logSyslog=true daemonise=true disableVia=true allowedPorts='1-65535' tunnelAllowedPorts='1-65535'

/usr/bin/tor -f /etc/torrc
