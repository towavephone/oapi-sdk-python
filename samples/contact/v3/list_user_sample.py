# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.contact.v3 import *


def main():
	# 构建client
	client = lark.Client.builder() \
		.app_id("APP_ID") \
		.app_secret("APP_SECRET") \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: ListUserRequest = lark.contact.v3.ListUserRequest.builder() \
		.user_id_type("open_id") \
		.department_id_type("open_department_id") \
		.department_id("str") \
		.page_token("str") \
		.page_size(20) \
		.build()

	# 发起请求
	response: ListUserResponse = client.contact.v3.user.list(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.contact.v3.user.list failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()