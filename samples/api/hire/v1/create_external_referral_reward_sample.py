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
    request: CreateExternalReferralRewardRequest = CreateExternalReferralRewardRequest.builder() \
        .user_id_type("user_id") \
        .request_body(ExternalReward.builder()
                      .referral_user_id("on_94a1ee5551019f18cd73d9f111898cf2")
                      .create_user_id("on_94a1ee5551019f18cd73d9f111898cf2")
                      .confirm_user_id("on_94a1ee5551019f18cd73d9f111898cf2")
                      .pay_user_id("on_94a1ee5551019f18cd73d9f111898cf2")
                      .external_id("6930815272790114324")
                      .application_id("6930815272790114325")
                      .talent_id("6930815272790114326")
                      .job_id("6930815272790114327")
                      .reason("首次推荐")
                      .rule_type(1)
                      .bonus(BonusAmount.builder().build())
                      .stage(1)
                      .create_time("1704720275000")
                      .confirm_time("1704720275000")
                      .pay_time("1704720275001")
                      .onboard_time("1704720275002")
                      .conversion_time("1704720275003")
                      .comment("已发放")
                      .build()) \
        .build()

    # 发起请求
    response: CreateExternalReferralRewardResponse = client.hire.v1.external_referral_reward.create(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.hire.v1.external_referral_reward.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: CreateExternalReferralRewardRequest = CreateExternalReferralRewardRequest.builder() \
        .user_id_type("user_id") \
        .request_body(ExternalReward.builder()
                      .referral_user_id("on_94a1ee5551019f18cd73d9f111898cf2")
                      .create_user_id("on_94a1ee5551019f18cd73d9f111898cf2")
                      .confirm_user_id("on_94a1ee5551019f18cd73d9f111898cf2")
                      .pay_user_id("on_94a1ee5551019f18cd73d9f111898cf2")
                      .external_id("6930815272790114324")
                      .application_id("6930815272790114325")
                      .talent_id("6930815272790114326")
                      .job_id("6930815272790114327")
                      .reason("首次推荐")
                      .rule_type(1)
                      .bonus(BonusAmount.builder().build())
                      .stage(1)
                      .create_time("1704720275000")
                      .confirm_time("1704720275000")
                      .pay_time("1704720275001")
                      .onboard_time("1704720275002")
                      .conversion_time("1704720275003")
                      .comment("已发放")
                      .build()) \
        .build()

    # 发起请求
    response: CreateExternalReferralRewardResponse = await client.hire.v1.external_referral_reward.acreate(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.hire.v1.external_referral_reward.acreate failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
