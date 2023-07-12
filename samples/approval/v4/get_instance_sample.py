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
	request: GetInstanceRequest = lark.approval.v4.GetInstanceRequest.builder() \
		.instance_id("81D31358-93AF-92D6-7425-01A5D67C4E71") \
		.locale("zh-CN") \
		.user_id("f7cb567e") \
		.user_id_type("user_id") \
		.build()

	# 发起请求
	response: GetInstanceResponse = client.approval.v4.instance.get(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.approval.v4.instance.get failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()