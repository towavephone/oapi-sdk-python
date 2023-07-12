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
	request: UpdateUserRequest = lark.contact.v3.UpdateUserRequest.builder() \
		.user_id("ou_7dab8a3d3cdcc9da365777c7ad535d62") \
		.user_id_type("open_id") \
		.department_id_type("open_department_id") \
		.request_body(lark.contact.v3.User.builder()
					  .name("张三")
					  .en_name("San Zhang")
					  .nickname("Alex Zhang")
					  .email("zhangsan@gmail.com")
					  .mobile("+41446681800")
					  .mobile_visible(False)
					  .gender(0)
					  .avatar_key("2500c7a9-5fff-4d9a-a2de-3d59614ae28g")
					  .department_ids([])
					  .leader_user_id("ou_7dab8a3d3cdcc9da365777c7ad535d62")
					  .city("杭州")
					  .country("CN")
					  .work_station("北楼-H34")
					  .join_time(2147483647)
					  .employee_no("1")
					  .employee_type(1)
					  .orders([])
					  .custom_attrs([])
					  .enterprise_email("demo@mail.com")
					  .job_title("xxxxx")
					  .is_frozen(False)
					  .build()) \
		.build()

	# 发起请求
	response: UpdateUserResponse = client.contact.v3.user.update(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.contact.v3.user.update failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()