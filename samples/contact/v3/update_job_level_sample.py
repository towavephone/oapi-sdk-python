# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.contact.v3 import *


def main():
	# 构建client
	client = lark.Client.builder() \
		.app_id("APP_ID") \
		.app_secret("APP_SECRET") \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: UpdateJobLevelRequest = lark.contact.v3.UpdateJobLevelRequest.builder() \
		.job_level_id("mga5oa8ayjlp9rb") \
		.request_body(lark.contact.v3.JobLevel.builder()
					  .name("高级专家")
					  .description("公司内部中高级职称，有一定专业技术能力的人员")
					  .order(200)
					  .status(True)
					  .i18n_name([])
					  .i18n_description([])
					  .build()) \
		.build()

	# 发起请求
	response: UpdateJobLevelResponse = client.contact.v3.job_level.update(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.contact.v3.job_level.update failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()