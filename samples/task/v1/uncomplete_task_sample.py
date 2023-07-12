# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.task.v1 import *


def main():
	# 构建client
	client = lark.Client.builder() \
		.app_id("APP_ID") \
		.app_secret("APP_SECRET") \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: UncompleteTaskRequest = lark.task.v1.UncompleteTaskRequest.builder() \
		.task_id("bb54ab99-d360-434f-bcaa-a4cc4c05840e") \
		.build()

	# 发起请求
	response: UncompleteTaskResponse = client.task.v1.task.uncomplete(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.task.v1.task.uncomplete failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()