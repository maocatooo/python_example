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
from Tea.core import TeaCore

from alibabacloud_alidns20150109.client import Client as Alidns20150109Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_alidns20150109 import models as alidns_20150109_models
from alibabacloud_tea_console.client import Client as ConsoleClient
from alibabacloud_tea_util.client import Client as UtilClient


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
            access_key_id: str,
            access_key_secret: str,
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
        client = Sample.create_client(*args)
        describe_domain_records_request = alidns_20150109_models.DescribeDomainRecordsRequest(
            domain_name='maocat.cc'
        )
        resp = client.describe_domain_records(describe_domain_records_request)
        import json
        print(json.dumps(TeaCore.to_map(resp), indent=2))
        # ConsoleClient.log(UtilClient.to_jsonstring(TeaCore.to_map(resp)))

    @staticmethod
    async def main_async(
            args: List[str],
    ) -> None:
        client = Sample.create_client(*args)
        describe_domain_records_request = alidns_20150109_models.DescribeDomainRecordsRequest(
            domain_name='maocat.cc'
        )
        resp = await client.describe_domain_records_async(describe_domain_records_request)
        ConsoleClient.log(UtilClient.to_jsonstring(TeaCore.to_map(resp)))


if __name__ == '__main__':
    Sample.main([access_key_id,access_key_secret])