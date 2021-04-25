# -*- coding: UTF-8 -*-
# Code generated by lark suite oapi sdk gen

from typing import List, Dict, Any
from ....utils.dt import to_json_decorator
import attr




@to_json_decorator
@attr.s
class EventLocation(object):
    name = attr.ib(type=str, default=None, metadata={'json': 'name'})
    address = attr.ib(type=str, default=None, metadata={'json': 'address'})
    latitude = attr.ib(type=float, default=None, metadata={'json': 'latitude'})
    longitude = attr.ib(type=float, default=None, metadata={'json': 'longitude'})


@to_json_decorator
@attr.s
class Vchat(object):
    meeting_url = attr.ib(type=str, default=None, metadata={'json': 'meeting_url'})


@to_json_decorator
@attr.s
class TimeInfo(object):
    date = attr.ib(type=str, default=None, metadata={'json': 'date'})
    timestamp = attr.ib(type=str, default=None, metadata={'json': 'timestamp'})
    timezone = attr.ib(type=str, default=None, metadata={'json': 'timezone'})


@to_json_decorator
@attr.s
class EventSearchFilter(object):
    start_time = attr.ib(type=TimeInfo, default=None, metadata={'json': 'start_time'})
    end_time = attr.ib(type=TimeInfo, default=None, metadata={'json': 'end_time'})
    user_ids = attr.ib(type=List[str], default=None, metadata={'json': 'user_ids'})
    room_ids = attr.ib(type=List[str], default=None, metadata={'json': 'room_ids'})
    chat_ids = attr.ib(type=List[str], default=None, metadata={'json': 'chat_ids'})


@to_json_decorator
@attr.s
class Schema(object):
    ui_name = attr.ib(type=str, default=None, metadata={'json': 'ui_name'})
    ui_status = attr.ib(type=str, default=None, metadata={'json': 'ui_status'})
    app_link = attr.ib(type=str, default=None, metadata={'json': 'app_link'})


@to_json_decorator
@attr.s
class Reminder(object):
    minutes = attr.ib(type=int, default=None, metadata={'json': 'minutes'})


@to_json_decorator
@attr.s
class CalendarEvent(object):
    event_id = attr.ib(type=str, default=None, metadata={'json': 'event_id'})
    summary = attr.ib(type=str, default=None, metadata={'json': 'summary'})
    description = attr.ib(type=str, default=None, metadata={'json': 'description'})
    start_time = attr.ib(type=TimeInfo, default=None, metadata={'json': 'start_time'})
    end_time = attr.ib(type=TimeInfo, default=None, metadata={'json': 'end_time'})
    vchat = attr.ib(type=Vchat, default=None, metadata={'json': 'vchat'})
    visibility = attr.ib(type=str, default=None, metadata={'json': 'visibility'})
    attendee_ability = attr.ib(type=str, default=None, metadata={'json': 'attendee_ability'})
    free_busy_status = attr.ib(type=str, default=None, metadata={'json': 'free_busy_status'})
    location = attr.ib(type=EventLocation, default=None, metadata={'json': 'location'})
    color = attr.ib(type=int, default=None, metadata={'json': 'color'})
    reminders = attr.ib(type=List[Reminder], default=None, metadata={'json': 'reminders'})
    recurrence = attr.ib(type=str, default=None, metadata={'json': 'recurrence'})
    status = attr.ib(type=str, default=None, metadata={'json': 'status'})
    is_exception = attr.ib(type=bool, default=None, metadata={'json': 'is_exception'})
    recurring_event_id = attr.ib(type=str, default=None, metadata={'json': 'recurring_event_id'})
    schemas = attr.ib(type=List[Schema], default=None, metadata={'json': 'schemas'})


@to_json_decorator
@attr.s
class AttendeeChatMember(object):
    rsvp_status = attr.ib(type=str, default=None, metadata={'json': 'rsvp_status'})
    is_optional = attr.ib(type=bool, default=None, metadata={'json': 'is_optional'})
    display_name = attr.ib(type=str, default=None, metadata={'json': 'display_name'})
    is_organizer = attr.ib(type=bool, default=None, metadata={'json': 'is_organizer'})
    is_external = attr.ib(type=bool, default=None, metadata={'json': 'is_external'})


@to_json_decorator
@attr.s
class CalendarEventAttendee(object):
    type = attr.ib(type=str, default=None, metadata={'json': 'type'})
    attendee_id = attr.ib(type=str, default=None, metadata={'json': 'attendee_id'})
    rsvp_status = attr.ib(type=str, default=None, metadata={'json': 'rsvp_status'})
    is_optional = attr.ib(type=bool, default=None, metadata={'json': 'is_optional'})
    is_organizer = attr.ib(type=bool, default=None, metadata={'json': 'is_organizer'})
    is_external = attr.ib(type=bool, default=None, metadata={'json': 'is_external'})
    display_name = attr.ib(type=str, default=None, metadata={'json': 'display_name'})
    chat_members = attr.ib(type=List[AttendeeChatMember], default=None, metadata={'json': 'chat_members'})
    user_id = attr.ib(type=str, default=None, metadata={'json': 'user_id'})
    chat_id = attr.ib(type=str, default=None, metadata={'json': 'chat_id'})
    room_id = attr.ib(type=str, default=None, metadata={'json': 'room_id'})
    third_party_email = attr.ib(type=str, default=None, metadata={'json': 'third_party_email'})


@to_json_decorator
@attr.s
class AclScope(object):
    type = attr.ib(type=str, default=None, metadata={'json': 'type'})
    user_id = attr.ib(type=str, default=None, metadata={'json': 'user_id'})


@to_json_decorator
@attr.s
class CalendarAcl(object):
    acl_id = attr.ib(type=str, default=None, metadata={'json': 'acl_id'})
    role = attr.ib(type=str, default=None, metadata={'json': 'role'})
    scope = attr.ib(type=AclScope, default=None, metadata={'json': 'scope'})


@to_json_decorator
@attr.s
class Calendar(object):
    calendar_id = attr.ib(type=str, default=None, metadata={'json': 'calendar_id'})
    summary = attr.ib(type=str, default=None, metadata={'json': 'summary'})
    description = attr.ib(type=str, default=None, metadata={'json': 'description'})
    permissions = attr.ib(type=str, default=None, metadata={'json': 'permissions'})
    color = attr.ib(type=int, default=None, metadata={'json': 'color'})
    type = attr.ib(type=str, default=None, metadata={'json': 'type'})
    summary_alias = attr.ib(type=str, default=None, metadata={'json': 'summary_alias'})
    is_deleted = attr.ib(type=bool, default=None, metadata={'json': 'is_deleted'})
    is_third_party = attr.ib(type=bool, default=None, metadata={'json': 'is_third_party'})
    role = attr.ib(type=str, default=None, metadata={'json': 'role'})


@to_json_decorator
@attr.s
class Freebusy(object):
    start_time = attr.ib(type=str, default=None, metadata={'json': 'start_time'})
    end_time = attr.ib(type=str, default=None, metadata={'json': 'end_time'})


@to_json_decorator
@attr.s
class TimeoffEvent(object):
    timeoff_event_id = attr.ib(type=str, default=None, metadata={'json': 'timeoff_event_id'})
    user_id = attr.ib(type=str, default=None, metadata={'json': 'user_id'})
    timezone = attr.ib(type=str, default=None, metadata={'json': 'timezone'})
    start_time = attr.ib(type=str, default=None, metadata={'json': 'start_time'})
    end_time = attr.ib(type=str, default=None, metadata={'json': 'end_time'})
    title = attr.ib(type=str, default=None, metadata={'json': 'title'})
    description = attr.ib(type=str, default=None, metadata={'json': 'description'})


@to_json_decorator
@attr.s
class Setting(object):
    pass


@to_json_decorator
@attr.s
class CalendarEventAttendeeChatMember(object):
    rsvp_status = attr.ib(type=str, default=None, metadata={'json': 'rsvp_status'})
    is_optional = attr.ib(type=bool, default=None, metadata={'json': 'is_optional'})
    display_name = attr.ib(type=str, default=None, metadata={'json': 'display_name'})
    is_organizer = attr.ib(type=bool, default=None, metadata={'json': 'is_organizer'})
    is_external = attr.ib(type=bool, default=None, metadata={'json': 'is_external'})




@attr.s
class CalendarCreateResult(object):
    calendar = attr.ib(type=Calendar, default=None, metadata={'json': 'calendar'})





@attr.s
class CalendarEventGetResult(object):
    event = attr.ib(type=CalendarEvent, default=None, metadata={'json': 'event'})



@attr.s
class CalendarPatchResult(object):
    calendar = attr.ib(type=Calendar, default=None, metadata={'json': 'calendar'})





@attr.s
class CalendarAclListResult(object):
    acls = attr.ib(type=List[CalendarAcl], default=None, metadata={'json': 'acls'})
    has_more = attr.ib(type=bool, default=None, metadata={'json': 'has_more'})
    page_token = attr.ib(type=str, default=None, metadata={'json': 'page_token'})





@attr.s
class CalendarEventCreateResult(object):
    event = attr.ib(type=CalendarEvent, default=None, metadata={'json': 'event'})





@attr.s
class CalendarEventAttendeeListResult(object):
    items = attr.ib(type=List[CalendarEventAttendee], default=None, metadata={'json': 'items'})
    has_more = attr.ib(type=bool, default=None, metadata={'json': 'has_more'})
    page_token = attr.ib(type=str, default=None, metadata={'json': 'page_token'})



@attr.s
class CalendarListResult(object):
    has_more = attr.ib(type=bool, default=None, metadata={'json': 'has_more'})
    page_token = attr.ib(type=str, default=None, metadata={'json': 'page_token'})
    sync_token = attr.ib(type=str, default=None, metadata={'json': 'sync_token'})
    calendar_list = attr.ib(type=List[Calendar], default=None, metadata={'json': 'calendar_list'})


@to_json_decorator
@attr.s
class CalendarEventAttendeeBatchDeleteReqBody(object):
    attendee_ids = attr.ib(type=List[str], default=None, metadata={'json': 'attendee_ids'})



@to_json_decorator
@attr.s
class CalendarEventAttendeeCreateReqBody(object):
    attendees = attr.ib(type=List[CalendarEventAttendee], default=None, metadata={'json': 'attendees'})


@attr.s
class CalendarEventAttendeeCreateResult(object):
    attendees = attr.ib(type=List[CalendarEventAttendee], default=None, metadata={'json': 'attendees'})





@attr.s
class CalendarEventListResult(object):
    has_more = attr.ib(type=bool, default=None, metadata={'json': 'has_more'})
    page_token = attr.ib(type=str, default=None, metadata={'json': 'page_token'})
    sync_token = attr.ib(type=str, default=None, metadata={'json': 'sync_token'})
    items = attr.ib(type=List[CalendarEvent], default=None, metadata={'json': 'items'})


@to_json_decorator
@attr.s
class CalendarSearchReqBody(object):
    query = attr.ib(type=str, default=None, metadata={'json': 'query'})


@attr.s
class CalendarSearchResult(object):
    items = attr.ib(type=List[Calendar], default=None, metadata={'json': 'items'})
    page_token = attr.ib(type=str, default=None, metadata={'json': 'page_token'})


@to_json_decorator
@attr.s
class FreebusyListReqBody(object):
    time_min = attr.ib(type=str, default=None, metadata={'json': 'time_min'})
    time_max = attr.ib(type=str, default=None, metadata={'json': 'time_max'})
    user_id = attr.ib(type=str, default=None, metadata={'json': 'user_id'})
    room_id = attr.ib(type=str, default=None, metadata={'json': 'room_id'})


@attr.s
class FreebusyListResult(object):
    freebusy_list = attr.ib(type=List[Freebusy], default=None, metadata={'json': 'freebusy_list'})



@attr.s
class CalendarEventPatchResult(object):
    event = attr.ib(type=CalendarEvent, default=None, metadata={'json': 'event'})








@to_json_decorator
@attr.s
class CalendarEventSearchReqBody(object):
    query = attr.ib(type=str, default=None, metadata={'json': 'query'})
    filter = attr.ib(type=EventSearchFilter, default=None, metadata={'json': 'filter'})


@attr.s
class CalendarEventSearchResult(object):
    items = attr.ib(type=List[CalendarEvent], default=None, metadata={'json': 'items'})
    page_token = attr.ib(type=str, default=None, metadata={'json': 'page_token'})



@attr.s
class CalendarSubscribeResult(object):
    calendar = attr.ib(type=Calendar, default=None, metadata={'json': 'calendar'})


@to_json_decorator
@attr.s
class SettingGenerateCaldavConfReqBody(object):
    device_name = attr.ib(type=str, default=None, metadata={'json': 'device_name'})


@attr.s
class SettingGenerateCaldavConfResult(object):
    password = attr.ib(type=str, default=None, metadata={'json': 'password'})
    user_name = attr.ib(type=str, default=None, metadata={'json': 'user_name'})
    server_address = attr.ib(type=str, default=None, metadata={'json': 'server_address'})
    device_name = attr.ib(type=str, default=None, metadata={'json': 'device_name'})









@attr.s
class CalendarEventAttendeeChatMemberListResult(object):
    items = attr.ib(type=List[CalendarEventAttendeeChatMember], default=None, metadata={'json': 'items'})
    has_more = attr.ib(type=bool, default=None, metadata={'json': 'has_more'})
    page_token = attr.ib(type=str, default=None, metadata={'json': 'page_token'})