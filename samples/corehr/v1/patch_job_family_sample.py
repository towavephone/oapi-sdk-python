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
	request: PatchJobFamilyRequest = lark.corehr.v1.PatchJobFamilyRequest.builder() \
		.job_family_id("1616161616") \
		.client_token("12454646") \
		.request_body(lark.corehr.v1.JobFamily.builder()
					  .name([])
					  .active(True)
					  .parent_id("4698020757495316313")
					  .effective_time("2020-05-01 00:00:00")
					  .expiration_time("2020-05-02 00:00:00")
					  .code("123456")
					  .custom_fields([])
					  .build()) \
		.build()

	# 发起请求
	response: PatchJobFamilyResponse = client.corehr.v1.job_family.patch(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.corehr.v1.job_family.patch failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()