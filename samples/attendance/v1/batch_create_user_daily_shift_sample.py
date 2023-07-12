# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.attendance.v1 import *


def main():
	# 构建client
	client = lark.Client.builder() \
		.app_id("APP_ID") \
		.app_secret("APP_SECRET") \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: BatchCreateUserDailyShiftRequest = lark.attendance.v1.BatchCreateUserDailyShiftRequest.builder() \
		.employee_type("employee_id") \
		.request_body(lark.attendance.v1.BatchCreateUserDailyShiftRequestBody.builder()
					  .user_daily_shifts([])
					  .operator_id("dd31248a")
					  .build()) \
		.build()

	# 发起请求
	response: BatchCreateUserDailyShiftResponse = client.attendance.v1.user_daily_shift.batch_create(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.attendance.v1.user_daily_shift.batch_create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()