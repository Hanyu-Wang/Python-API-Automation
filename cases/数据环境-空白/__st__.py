from hyrobot.common import *
from lib.WEBAPI import apimgr


def suite_setup():
    INFO('初始化清除客户、药品、订单')
    apimgr.mgr_login()
    apimgr.order_del_all()
    apimgr.customer_del_all()
    apimgr.medicine_del_all()
