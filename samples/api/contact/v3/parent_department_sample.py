# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.contact.v3 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: ParentDepartmentRequest = ParentDepartmentRequest.builder() \
        .user_id_type("user_id") \
        .department_id_type("open_department_id") \
        .department_id("od-4e6ac4d14bcd5071a37a39de902c7141") \
        .page_token(
        "AQD9/Rn9eij9Pm39ED40/RD/cIFmu77WxpxPB/2oHfQLZ%2BG8JG6tK7%2BZnHiT7COhD2hMSICh/eBl7cpzU6JEC3J7COKNe4jrQ8ExwBCR") \
        .page_size(20) \
        .build()

    # 发起请求
    response: ParentDepartmentResponse = client.contact.v3.department.parent(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.contact.v3.department.parent failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


# 异步方式
async def amain():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: ParentDepartmentRequest = ParentDepartmentRequest.builder() \
        .user_id_type("user_id") \
        .department_id_type("open_department_id") \
        .department_id("od-4e6ac4d14bcd5071a37a39de902c7141") \
        .page_token(
        "AQD9/Rn9eij9Pm39ED40/RD/cIFmu77WxpxPB/2oHfQLZ%2BG8JG6tK7%2BZnHiT7COhD2hMSICh/eBl7cpzU6JEC3J7COKNe4jrQ8ExwBCR") \
        .page_size(20) \
        .build()

    # 发起请求
    response: ParentDepartmentResponse = await client.contact.v3.department.aparent(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.contact.v3.department.aparent failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
