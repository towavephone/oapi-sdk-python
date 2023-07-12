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
	request: ListFreebusyRequest = lark.calendar.v4.ListFreebusyRequest.builder() \
		.user_id_type("user_id") \
		.request_body(lark.calendar.v4.ListFreebusyRequestBody.builder()
					  .time_min("2020-10-28T12:00:00+08:00")
					  .time_max("2020-12-28T12:00:00+08:00")
					  .user_id("ou_xxxxxxxxxx")
					  .room_id("omm_xxxxxxxxxx")
					  .build()) \
		.build()

	# 发起请求
	response: ListFreebusyResponse = client.calendar.v4.freebusy.list(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.calendar.v4.freebusy.list failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()