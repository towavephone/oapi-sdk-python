# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.calendar.v4 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: GetExchangeBindingRequest = GetExchangeBindingRequest.builder() \
        .exchange_binding_id("ZW1haWxfYWRtaW5fZXhhbXBsZUBvdXRsb29rLmNvbSBlbWFpbF9hY2NvdW50X2V4YW1wbGVAb3V0bG9vay5jb20=") \
        .user_id_type("user_id") \
        .build()

    # 发起请求
    response: GetExchangeBindingResponse = client.calendar.v4.exchange_binding.get(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.calendar.v4.exchange_binding.get failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: GetExchangeBindingRequest = GetExchangeBindingRequest.builder() \
        .exchange_binding_id("ZW1haWxfYWRtaW5fZXhhbXBsZUBvdXRsb29rLmNvbSBlbWFpbF9hY2NvdW50X2V4YW1wbGVAb3V0bG9vay5jb20=") \
        .user_id_type("user_id") \
        .build()

    # 发起请求
    response: GetExchangeBindingResponse = await client.calendar.v4.exchange_binding.aget(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.calendar.v4.exchange_binding.aget failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
