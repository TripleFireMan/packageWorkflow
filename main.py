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
        driverProjectPath = os.environ["driver_project_path"]
        logiticsProjectPath = os.environ["logistics_project_path"]
        msg = self.args[1]
        if self.args[0] == "pgy":
            wf.add_item(title="建龙快成司机端", subtitle="打包发布到蒲公英平台", arg="cd {0};fastlane pgy msg:{1} >> sj.log 2>&1".format(driverProjectPath, msg), valid=True, icon="icon/driver.png")
            wf.add_item(title="建龙快成物流端", subtitle="打包发布到蒲公英平台", arg="cd {0};fastlane pgy msg:{1} >> wl.log 2>&1".format(logiticsProjectPath, msg), valid=True, icon="icon/logicties.png")
            wf.send_feedback()
        elif self.args[0] == 'release':
            wf.add_item(title='发布【司机端】', subtitle="发布项目到appstore", arg="cd {0};fastlane release->&sj.log".format(driverProjectPath), valid=True, icon='icon/driver.png')
            wf.add_item(title='发布【物流端】', subtitle="发布项目到appstore", arg="cd {0};fastlane release->&wl.log".format(logiticsProjectPath), valid=True, icon='icon/logicties.png')
            wf.send_feedback()

def main(wf):
    app = App(wf)
    return app.run()


if __name__ == '__main__':
    wf = Workflow3()
    log = wf.logger
    sys.exit(wf.run(main))



