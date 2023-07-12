# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.drive.v1 import *


def main():
	# 构建client
	client = lark.Client.builder() \
		.app_id("APP_ID") \
		.app_secret("APP_SECRET") \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: UploadFinishMediaRequest = lark.drive.v1.UploadFinishMediaRequest.builder() \
		.request_body(lark.drive.v1.UploadFinishMediaRequestBody.builder()
					  .upload_id("7111211691345512356")
					  .block_num(1)
					  .build()) \
		.build()

	# 发起请求
	response: UploadFinishMediaResponse = client.drive.v1.media.upload_finish(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.drive.v1.media.upload_finish failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()