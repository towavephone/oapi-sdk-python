# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.hire.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: ListEvaluationTaskRequest = ListEvaluationTaskRequest.builder() \
        .page_size(10) \
        .page_token("eyJvZmZzZXQiOjEwLCJ0aW1lc3RhbXAiOjE2Mjc1NTUyMjM2NzIsImlkIjpudWxsfQ==") \
        .user_id("ou_e6139117c300506837def50545420c6a") \
        .activity_status(1) \
        .user_id_type("user_id") \
        .build()

    # 发起请求
    response: ListEvaluationTaskResponse = client.hire.v1.evaluation_task.list(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.hire.v1.evaluation_task.list failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: ListEvaluationTaskRequest = ListEvaluationTaskRequest.builder() \
        .page_size(10) \
        .page_token("eyJvZmZzZXQiOjEwLCJ0aW1lc3RhbXAiOjE2Mjc1NTUyMjM2NzIsImlkIjpudWxsfQ==") \
        .user_id("ou_e6139117c300506837def50545420c6a") \
        .activity_status(1) \
        .user_id_type("user_id") \
        .build()

    # 发起请求
    response: ListEvaluationTaskResponse = await client.hire.v1.evaluation_task.alist(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.hire.v1.evaluation_task.alist failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
