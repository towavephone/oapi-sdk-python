# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.hire.v1 import *


def main():
	# 构建client
	client = lark.Client.builder() \
		.app_id("APP_ID") \
		.app_secret("APP_SECRET") \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: ListJobRequirementRequest = lark.hire.v1.ListJobRequirementRequest.builder() \
		.page_token("1231231987") \
		.page_size(1) \
		.job_id("6001") \
		.create_time_begin("1658980233000") \
		.create_time_end("1658980233000") \
		.update_time_begin("1658980233000") \
		.update_time_end("1658980233000") \
		.user_id_type("open_id") \
		.department_id_type("open_department_id") \
		.build()

	# 发起请求
	response: ListJobRequirementResponse = client.hire.v1.job_requirement.list(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.hire.v1.job_requirement.list failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()