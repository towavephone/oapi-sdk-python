# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.wiki.v2 import *


def main():
	# 构建client
	client = lark.Client.builder() \
		.app_id("APP_ID") \
		.app_secret("APP_SECRET") \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: ListSpaceNodeRequest = lark.wiki.v2.ListSpaceNodeRequest.builder() \
		.space_id("6946843325487906839") \
		.page_size(10) \
		.page_token("6946843325487456878") \
		.parent_node_token("wikcnKQ1k3p******8Vabce") \
		.build()

	# 发起请求
	response: ListSpaceNodeResponse = client.wiki.v2.space_node.list(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.wiki.v2.space_node.list failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()