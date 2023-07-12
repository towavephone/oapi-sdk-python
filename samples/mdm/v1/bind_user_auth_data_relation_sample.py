# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.mdm.v1 import *


def main():
	# 构建client
	client = lark.Client.builder() \
		.app_id("APP_ID") \
		.app_secret("APP_SECRET") \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: BindUserAuthDataRelationRequest = lark.mdm.v1.BindUserAuthDataRelationRequest.builder() \
		.user_id_type("user_id") \
		.request_body(lark.mdm.v1.UserAuthDataRelation.builder()
					  .root_dimension_type("zijie")
					  .sub_dimension_types([])
					  .authorized_user_ids([])
					  .uams_app_id("uams-tenant-test")
					  .build()) \
		.build()

	# 发起请求
	response: BindUserAuthDataRelationResponse = client.mdm.v1.user_auth_data_relation.bind(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.mdm.v1.user_auth_data_relation.bind failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()