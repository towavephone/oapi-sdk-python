# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.hire.v1 import *


def main():
	# 构建client
	client = lark.Client.builder() \
		.app_id("APP_ID") \
		.app_secret("APP_SECRET") \
		.log_level(lark.LogLevel.DEBUG) \
		.build()

	# 构造请求对象
	request: UpdateConfigJobRequest = lark.hire.v1.UpdateConfigJobRequest.builder() \
		.job_id("6960663240925956660") \
		.user_id_type("user_id") \
		.request_body(lark.hire.v1.JobConfig.builder()
					  .offer_apply_schema_id("6960663240925956573")
					  .offer_process_conf("6960663240925956572")
					  .recommended_evaluator_id_list([])
					  .update_option_list([])
					  .assessment_template_biz_id("6960663240925956571")
					  .interview_round_conf_list([])
					  .jr_id_list([])
					  .interview_registration_schema_id("6930815272790114324")
					  .interview_round_type_conf_list([])
					  .related_job_id_list([])
					  .interview_appointment_config(InterviewAppointmentConfig.builder().build())
					  .build()) \
		.build()

	# 发起请求
	response: UpdateConfigJobResponse = client.hire.v1.job.update_config(request)

	# 处理失败返回
	if not response.success():
		lark.logger.error(
			f"client.hire.v1.job.update_config failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
		return

	# 处理业务结果
	lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
	main()