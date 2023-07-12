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
	request: SearchEmployeeRequest = lark.corehr.v2.SearchEmployeeRequest.builder() \
		.page_size(100) \
		.page_token("6891251722631890445") \
		.user_id_type("open_id") \
		.department_id_type("open_department_id") \
		.request_body(lark.corehr.v2.SearchEmployeeRequestBody.builder()
					  .fields([])
					  .employment_id_list([])
					  .employee_number_list([])
					  .work_email("13312345678@qq.com")
					  .phone_number("16760342300")
					  .key_word("张三")
					  .employment_status("hired")
					  .employee_type_id("6971090097697521314")
					  .department_id_list([])
					  .direct_manager_id_list([])
					  .dotted_line_manager_id_list([])
					  .regular_employee_start_date_start("2020-01-01")
					  .regular_employee_start_date_end("2020-01-01")
					  .effective_time_start("2020-01-01")
					  .effective_time_end("2020-01-01")
					  .work_location_id_list_include_sub([])
					  .preferred_english_full_name_list([])
					  .preferred_local_full_name_list([])
					  .national_id_number_list([])
					  .phone_number_list([])
					  .email_address_list([])
					  .department_id_list_include_sub([])
					  .build()) \
		.build()

	# 发起请求
	response: SearchEmployeeResponse = client.corehr.v2.employee.search(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.corehr.v2.employee.search failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()