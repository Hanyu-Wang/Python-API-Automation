# from hyrobot.common import *
# from lib.WEBAPI import apimgr
#
#
# def suite_setup():
#     INFO('初始化新增一个用户')
#     r = apimgr.customer_add('武汉市桥西医院',
#                             '13345679934',
#                             "武汉市桥西医院北路")
#
#     addret = r.json()
#
#     addedCustomerId = addret['id']
#     GSTORE['global_addid'] = addedCustomerId
#
#
# # def get_global_addid():
# #     return GSTORE['global_addid']
#
#
# def suite_teardown():
#     apimgr.customer_del(GSTORE['global_addid'])
