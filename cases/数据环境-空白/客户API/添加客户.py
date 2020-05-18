from hyrobot.common import *
from lib.WEBAPI import apimgr


class C1:
    name = '客户 - API-0151'

    # 清除方法
    def teardown(self):
        apimgr.customer_del(self.addedCustomerId)

    def teststeps(self):
        STEP(1, '添加一个客户')
        r = apimgr.customer_add('武汉市桥西医院',
                                '13345679934',
                                "武汉市桥西医院北路")

        addret = r.json()

        self.addedCustomerId = addret['id']

        CHECK_POINT('返回的ret值=0',
                    addret['ret'] == 0)

        STEP(2, '检查系统数据')

        r = apimgr.customer_list()

        listRet = r.json()

        expected = {
            "ret": 0,
            "retlist": [
                {
                    "address": "武汉市桥西医院北路",
                    "id": addret['id'],
                    "name": "武汉市桥西医院",
                    "phonenumber": "13345679934"
                }
            ],
            'total': 1
        }

        CHECK_POINT('返回的消息体数据正确',
                    expected == listRet)


class C3:
    name = '客户 - API-0153'

    def teststeps(self):
        STEP(1, '添加一个客户')
        r = apimgr.customer_add2({
            "phonenumber": "13345679934",
            "address": "南京市鼓楼北路"
        })

        addRet = r.json()

        CHECK_POINT('返回的ret',
                    addRet == {
                        "ret": 1,
                        "msg": "请求消息参数错误",
                    })

        STEP(2, '检查系统数据')

        r = apimgr.customer_list()

        listRet = r.json()

        CHECK_POINT('返回的消息体数据正确',
                    listRet == {
                        "ret": 0,
                        "retlist": [],
                        'total': 0
                    })


class C4:
    name = '客户 - API-0201'

    def teststeps(self):
        r = apimgr.update_customer(100, 'suzhou', 17600000000, 'jiangsu')
        updateRet = r.json()
        CHECK_POINT('返回的ret',
                    updateRet == {
                        "ret": 1,
                        "msg": "客户ID不存在",
                    })
        r = apimgr.customer_list()

        listRet = r.json()

        CHECK_POINT('返回的消息体数据正确',
                    listRet == {
                        "ret": 0,
                        "retlist": [],
                        'total': 0
                    })


class C7:
    name = '客户 - API-0251'

    def teststeps(self):
        r = apimgr.customer_del(10000)
        del_customer = r.json()
        CHECK_POINT('返回的ret',
                    del_customer == {
                        "ret": 1,
                        "msg": "客户ID不存在",
                    })
        r = apimgr.customer_list()

        listRet = r.json()

        CHECK_POINT('返回的消息体数据正确',
                    listRet == {
                        "ret": 0,
                        "retlist": [],
                        'total': 0
                    })
