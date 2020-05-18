from hyrobot.common import *
from lib.WEBAPI import apimgr


class C5:
    name = '客户 - API-0202'

    def teardown(self):
        apimgr.customer_del(self.addedCustomerId)

    def teststeps(self):
        r = apimgr.customer_add('武汉市桥西医院',
                                '13345679934',
                                "武汉市桥西医院北路")

        addret = r.json()

        self.addedCustomerId = addret['id']
        STEP(1, '删除一个客户信息')
        u = apimgr.customer_del(addret['id'])
        del_customer = u.json()
        CHECK_POINT('返回的ret',
                    del_customer["ret"] == 0)

        r = apimgr.customer_list()

        listRet = r.json()

        expected = {
            "ret": 0,
            "retlist": [],
            'total': 0
        }

        CHECK_POINT('返回的消息体数据正确',
                    expected == listRet)


class C6:
    name = '客户 - API-0203'

    def teardown(self):
        apimgr.customer_del(self.addedCustomerId)

    def teststeps(self):
        r = apimgr.customer_add('武汉市桥西医院',
                                '13345679934',
                                "武汉市桥西医院北路")

        addret = r.json()

        self.addedCustomerId = addret['id']
        STEP(1, '只修改手机号码')
        u = apimgr.update_customer(addret['id'],
                                   '武汉市桥西医院',
                                   '13600000000',
                                   "武汉市桥西医院北路")
        update = u.json()
        CHECK_POINT('返回的ret',
                    update["ret"] == 0)

        r = apimgr.customer_list()

        listret = r.json()

        expected = {
            "ret": 0,
            "retlist": [
                {
                    "id": addret['id'],
                    "name": "武汉市桥西医院",
                    "phonenumber": "13600000000",
                    "address": "武汉市桥西医院北路"
                }
            ],
            'total': 1
        }

        CHECK_POINT('返回的消息体数据正确',
                    expected == listret)


class C8:
    name = '客户 - API-0252'

    def teardown(self):
        apimgr.customer_del(self.addedCustomerId)

    def teststeps(self):
        r = apimgr.customer_add('武汉市桥西医院',
                                '13345679934',
                                "武汉市桥西医院北路")

        addret = r.json()

        self.addedCustomerId = addret['id']
        STEP(1, '删除一个已经存在的的用户')
        r = apimgr.customer_del(addret['id'])
        delret = r.json()
        CHECK_POINT('返回的ret',
                    delret["ret"] == 0)
        r = apimgr.customer_list()

        listret = r.json()
        STEP(2, '检查系统数据')
        CHECK_POINT('返回的消息体数据正确',
                    listret == {
                        "ret": 0,
                        "retlist": [],
                        'total': 0
                    })
