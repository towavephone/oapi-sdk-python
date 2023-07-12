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
	request: PutTopNoticeChatTopNoticeRequest = lark.im.v1.PutTopNoticeChatTopNoticeRequest.builder() \
		.chat_id("oc_5ad11d72b830411d72b836c20") \
		.request_body(lark.im.v1.PutTopNoticeChatTopNoticeRequestBody.builder()
					  .chat_top_notice([])
					  .build()) \
		.build()

	# 发起请求
	response: PutTopNoticeChatTopNoticeResponse = client.im.v1.chat_top_notice.put_top_notice(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.im.v1.chat_top_notice.put_top_notice failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()