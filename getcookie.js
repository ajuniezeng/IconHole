[mitm] 

hostname = c.tieba.baidu.com



[rewrite_local]

# 获取贴吧Cookie
https?:\/\/(c\.tieba\.baidu\.com|180\.97\.\d+\.\d+)\/c\/s\/login url script-request-header https://raw.githubusercontent.com/Softlyx/QuantumultX/main/tieba.js