#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python2
# -*- coding:UTF-8 -*-
# import terminalcommandi

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import logging
from workflow import Workflow3

logger = None
if __name__ == '__main__':
    wf = Workflow3()
    log = wf.logger
    log.setLevel(logging.DEBUG)
    q = wf.args[0]
    log.debug(q)
    log.debug("环境变量{0}".format(os.environ))
    status = os.system(q)
    if q.__contains__('sj'):
        print '建龙快成司机打包完成 状态码：{0}'.format(status)
    elif q.__contains__('wl'):
        print "建龙快成物流打包完成 状态码:{0}".format(status)
    elif q.__contains__('grh'):
        print "高人汇打包完成 状态码：{0}".format(status)
    else:
        print "打包完毕"
