# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.docx.v1 import *


def main():
	# 构建client
	client = lark.Client.builder() \
		.app_id("APP_ID") \
		.app_secret("APP_SECRET") \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: BatchDeleteDocumentBlockChildrenRequest = lark.docx.v1.BatchDeleteDocumentBlockChildrenRequest.builder() \
		.document_id("doxcnePuYufKa49ISjhD8Ih0ikh") \
		.block_id("doxcnO6UW6wAw2qIcYf4hZpFIth") \
		.document_revision_id(-1) \
		.client_token("fe599b60-450f-46ff-b2ef-9f6675625b97") \
		.request_body(lark.docx.v1.BatchDeleteDocumentBlockChildrenRequestBody.builder()
					  .start_index(0)
					  .end_index(1)
					  .build()) \
		.build()

	# 发起请求
	response: BatchDeleteDocumentBlockChildrenResponse = client.docx.v1.document_block_children.batch_delete(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.docx.v1.document_block_children.batch_delete failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()