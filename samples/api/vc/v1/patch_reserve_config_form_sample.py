# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.vc.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: PatchReserveConfigFormRequest = PatchReserveConfigFormRequest.builder() \
        .reserve_config_id("omm_3c5dd7e09bac0c1758fcf9511bd1a771") \
        .user_id_type("user_id") \
        .request_body(PatchReserveConfigFormRequestBody.builder()
                      .scope_type(2)
                      .reserve_form_config(ReserveFormConfig.builder().build())
                      .build()) \
        .build()

    # 发起请求
    response: PatchReserveConfigFormResponse = client.vc.v1.reserve_config_form.patch(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.vc.v1.reserve_config_form.patch failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: PatchReserveConfigFormRequest = PatchReserveConfigFormRequest.builder() \
        .reserve_config_id("omm_3c5dd7e09bac0c1758fcf9511bd1a771") \
        .user_id_type("user_id") \
        .request_body(PatchReserveConfigFormRequestBody.builder()
                      .scope_type(2)
                      .reserve_form_config(ReserveFormConfig.builder().build())
                      .build()) \
        .build()

    # 发起请求
    response: PatchReserveConfigFormResponse = await client.vc.v1.reserve_config_form.apatch(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.vc.v1.reserve_config_form.apatch failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
