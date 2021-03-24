# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys

from typing import List

from alibabacloud_alidns20150109.client import Client as Alidns20150109Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_alidns20150109 import models as alidns_20150109_models
access_key_id=''
access_key_secret=''
region_id='cn-hangzhou'
# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys

from typing import List

from alibabacloud_alidns20150109.client import Client as Alidns20150109Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_alidns20150109 import models as alidns_20150109_models


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
            access_key_id1: str,
            access_key_secret1: str,
    ) -> Alidns20150109Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # 您的AccessKey ID,
            access_key_id=access_key_id,
            # 您的AccessKey Secret,
            access_key_secret=access_key_secret
        )
        # 访问的域名
        config.endpoint = 'dns.aliyuncs.com'
        return Alidns20150109Client(config)

    @staticmethod
    def main(
            args: List[str],
    ) -> None:
        client = Sample.create_client('accessKeyId', 'accessKeySecret')
        set_domain_record_status_request = alidns_20150109_models.SetDomainRecordStatusRequest(
            record_id='17673832614947840',
            status='Disable' # Enable: 启用解析  Disable: 暂停解析
        )
        # 复制代码运行请自行打印 API 的返回值
        client.set_domain_record_status(set_domain_record_status_request)

    @staticmethod
    async def main_async(
            args: List[str],
    ) -> None:
        client = Sample.create_client('accessKeyId', 'accessKeySecret')
        set_domain_record_status_request = alidns_20150109_models.SetDomainRecordStatusRequest(
            record_id='17673832614947840',
            status='Disable'
        )
        # 复制代码运行请自行打印 API 的返回值
        await client.set_domain_record_status_async(set_domain_record_status_request)


if __name__ == '__main__':
    Sample.main([access_key_id, access_key_secret])