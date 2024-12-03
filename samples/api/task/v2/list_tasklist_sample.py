# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.task.v2 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: ListTasklistRequest = ListTasklistRequest.builder() \
        .page_size(50) \
        .page_token("aWQ9NzEwMjMzMjMxMDE=") \
        .user_id_type("open_id") \
        .build()

    # 发起请求
    response: ListTasklistResponse = client.task.v2.tasklist.list(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.task.v2.tasklist.list failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: ListTasklistRequest = ListTasklistRequest.builder() \
        .page_size(50) \
        .page_token("aWQ9NzEwMjMzMjMxMDE=") \
        .user_id_type("open_id") \
        .build()

    # 发起请求
    response: ListTasklistResponse = await client.task.v2.tasklist.alist(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.task.v2.tasklist.alist failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
