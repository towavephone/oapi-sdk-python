# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.application.v6 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: ListApplicationRequest = ListApplicationRequest.builder() \
        .page_size(50) \
        .page_token(
        "AQD9/Rn9eij9Pm39ED40/dk53s4Ebp882DYfFaPFbz00L4CMZJrqGdzNyc8BcZtDbwVUvRmQTvyMYicnGWrde9X56TgdBuS+JKiSIkdexPw=") \
        .user_id_type("str") \
        .lang("zh_cn") \
        .status(0) \
        .payment_type(0) \
        .owner_type(0) \
        .build()

    # 发起请求
    response: ListApplicationResponse = client.application.v6.application.list(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.application.v6.application.list failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: ListApplicationRequest = ListApplicationRequest.builder() \
        .page_size(50) \
        .page_token(
        "AQD9/Rn9eij9Pm39ED40/dk53s4Ebp882DYfFaPFbz00L4CMZJrqGdzNyc8BcZtDbwVUvRmQTvyMYicnGWrde9X56TgdBuS+JKiSIkdexPw=") \
        .user_id_type("str") \
        .lang("zh_cn") \
        .status(0) \
        .payment_type(0) \
        .owner_type(0) \
        .build()

    # 发起请求
    response: ListApplicationResponse = await client.application.v6.application.alist(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.application.v6.application.alist failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
