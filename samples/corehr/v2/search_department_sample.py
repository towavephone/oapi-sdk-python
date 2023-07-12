# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.corehr.v2 import *


def main():
	# 构建client
	client = lark.Client.builder() \
		.app_id("APP_ID") \
		.app_secret("APP_SECRET") \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: SearchDepartmentRequest = lark.corehr.v2.SearchDepartmentRequest.builder() \
		.page_size(100) \
		.page_token("6891251722631890445") \
		.user_id_type("open_id") \
		.department_id_type("open_department_id") \
		.request_body(lark.corehr.v2.SearchDepartmentRequestBody.builder()
					  .manager_list([])
					  .department_id_list([])
					  .name_list([])
					  .parent_department_id("7094136522860922222")
					  .code_list([])
					  .fields([])
					  .build()) \
		.build()

	# 发起请求
	response: SearchDepartmentResponse = client.corehr.v2.department.search(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.corehr.v2.department.search failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()