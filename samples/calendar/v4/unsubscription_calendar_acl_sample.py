# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.calendar.v4 import *


def main():
	# 构建client
	client = lark.Client.builder() \
		.app_id("APP_ID") \
		.app_secret("APP_SECRET") \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: UnsubscriptionCalendarAclRequest = lark.calendar.v4.UnsubscriptionCalendarAclRequest.builder() \
		.calendar_id("feishu.cn_xxxxxxxxxx@group.calendar.feishu.cn") \
		.build()

	# 发起请求
	response: UnsubscriptionCalendarAclResponse = client.calendar.v4.calendar_acl.unsubscription(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.calendar.v4.calendar_acl.unsubscription failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()