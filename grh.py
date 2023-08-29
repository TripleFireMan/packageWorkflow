#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python2
# -*- coding:UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import time
import logging
import json
from  workflow import Workflow3
log = None

class App(object):
    def __init__(self,wf):
        self.wf = wf
        self.query = None
        self.args = None
    def run(self):
        self.args = self.wf.args
        log.setLevel(logging.DEBUG)
        log.debug("self.args:{0}".format(self.args))
        log.debug(wf.alfred_env)
        log.debug(wf.settings)
        grh_project_path = os.environ["grh_project_path"]
        msg = self.args[1]
        wf.add_item(title="高人汇咨询", subtitle="打包发布到蒲公英平台", arg="cd {0};fastlane grh_zx >> grh.log 2>&1".format(grh_project_path, msg), valid=True, icon="icon/icon-40.png")
        wf.send_feedback()



def main(wf):
    app = App(wf)
    return app.run()


if __name__ == '__main__':
    wf = Workflow3()
    log = wf.logger
    sys.exit(wf.run(main))



