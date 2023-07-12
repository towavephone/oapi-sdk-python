# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.approval.v4 import *


def main():
	# 构建client
	client = lark.Client.builder() \
		.app_id("APP_ID") \
		.app_secret("APP_SECRET") \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: QueryTaskRequest = lark.approval.v4.QueryTaskRequest.builder() \
		.page_size(100) \
		.page_token("1") \
		.user_id("example_user_id") \
		.topic("1") \
		.user_id_type("user_id") \
		.build()

	# 发起请求
	response: QueryTaskResponse = client.approval.v4.task.query(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.approval.v4.task.query failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()