# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.im.v1 import *


def main():
	# 构建client
	client = lark.Client.builder() \
		.app_id("APP_ID") \
		.app_secret("APP_SECRET") \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: SearchChatRequest = lark.im.v1.SearchChatRequest.builder() \
		.user_id_type("user_id") \
		.query("abc") \
		.page_token("dmJCRHhpd3JRbGV1VEVNRFFyTitRWDY5ZFkybmYrMEUwMUFYT0VMMWdENEtuYUhsNUxGMDIwemtvdE5ORjBNQQ==") \
		.page_size(20) \
		.build()

	# 发起请求
	response: SearchChatResponse = client.im.v1.chat.search(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.im.v1.chat.search failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()