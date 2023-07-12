# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.application.v6 import *


def main():
	# 构建client
	client = lark.Client.builder() \
		.app_id("APP_ID") \
		.app_secret("APP_SECRET") \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: CheckWhiteBlackListApplicationVisibilityRequest = lark.application.v6.CheckWhiteBlackListApplicationVisibilityRequest.builder() \
		.app_id("cli_a3a3d00b40b8d01b") \
		.user_id_type("open_id") \
		.department_id_type("department_id") \
		.request_body(lark.application.v6.CheckWhiteBlackListApplicationVisibilityRequestBody.builder()
					  .user_ids([])
					  .department_ids([])
					  .group_ids([])
					  .build()) \
		.build()

	# 发起请求
	response: CheckWhiteBlackListApplicationVisibilityResponse = client.application.v6.application_visibility.check_white_black_list(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.application.v6.application_visibility.check_white_black_list failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()