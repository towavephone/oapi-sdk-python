# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.bitable.v1 import *


def main():
	# 构建client
	client = lark.Client.builder() \
		.app_id("APP_ID") \
		.app_secret("APP_SECRET") \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: BatchUpdateAppTableRecordRequest = lark.bitable.v1.BatchUpdateAppTableRecordRequest.builder() \
		.app_token("appbcbWCzen6D8dezhoCH2RpMAh") \
		.table_id("tblsRc9GRRXKqhvW") \
		.user_id_type("user_id") \
		.request_body(lark.bitable.v1.BatchUpdateAppTableRecordRequestBody.builder()
					  .records([])
					  .build()) \
		.build()

	# 发起请求
	response: BatchUpdateAppTableRecordResponse = client.bitable.v1.app_table_record.batch_update(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.bitable.v1.app_table_record.batch_update failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()