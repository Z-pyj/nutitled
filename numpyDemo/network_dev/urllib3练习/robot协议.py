from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
# 设置地址
rp.set_url('https://www.baidu.com/robots.txt')
# 读取文件并进行解析
rp.read()
# 表示User-Agent指示的引擎是否可以抓取这个url
print(rp.can_fetch('Baiduspider', 'https://www.baidu.com'))
print(rp.can_fetch('Baiduspider', 'https://www.baidu.com/homepage/'))
print(rp.can_fetch('Googlebot', 'https://www.baidu.com/homepage/'))
