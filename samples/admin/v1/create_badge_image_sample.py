# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.admin.v1 import *


def main():
	# 构建client
	client = lark.Client.builder() \
		.app_id("APP_ID") \
		.app_secret("APP_SECRET") \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	file = open("file_path", "rb")
	request: CreateBadgeImageRequest = lark.admin.v1.CreateBadgeImageRequest.builder() \
		.request_body(lark.admin.v1.CreateBadgeImageRequestBody.builder()
					  .image_file(file)
					  .image_type(1)
					  .build()) \
		.build()

	# 发起请求
	response: CreateBadgeImageResponse = client.admin.v1.badge_image.create(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.admin.v1.badge_image.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()