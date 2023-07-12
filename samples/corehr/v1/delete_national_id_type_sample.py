# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.corehr.v1 import *


def main():
	# 构建client
	client = lark.Client.builder() \
		.app_id("APP_ID") \
		.app_secret("APP_SECRET") \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: DeleteNationalIdTypeRequest = lark.corehr.v1.DeleteNationalIdTypeRequest.builder() \
		.national_id_type_id("27837817381") \
		.build()

	# 发起请求
	response: DeleteNationalIdTypeResponse = client.corehr.v1.national_id_type.delete(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.corehr.v1.national_id_type.delete failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()