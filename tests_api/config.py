URL_AUTH = {
    'url_login': "http://34.65.101.58:5002/api/Authentication/Login",
    'url_register': "http://34.65.101.58:5002/api/Authentication/Register",
    'url_login_fb': "http://34.65.101.58:5002/api/Authentication/FacebookLogin",
    'url_login_google': "http://34.65.101.58:5002/api/Authentication/google",
    'url_change_password': "http://34.65.101.58:5002/api/Authentication/ChangePassword"
}
URL_CATEGORY = {
    'url_category_edit': "http://34.65.101.58:5002/api/Category/Edit",
    'url_category_all': "http://34.65.101.58:5002/api/Category/All",
    'url_category_delete': "http://34.65.101.58:5002/api/Category/Delete/"
}

AUTH_PAYLOADS = {
    'payload_admin': {"Email": "admin@gmail.com", "Password": "1qaz1qaz"},
    'payload_user': {"Email": "user@gmail.com", "Password": "1qaz1qaz"},
    'payload_vasya': {"Email": "vasya@gmail.com", "Password": "1qaz1qaz"},
    'payload_unauth': {"Email": "katya@gmail.com", "Password": "123456"},
    'payload_change_password': {"oldPassword": "1qaz1qaz", "newPassword": "1qaz1qaz1", "repeatPassword": "1qaz1qaz1"}}

CATEGORY_PAYLOADS = {
    'category_to_edit': {
        "Id": "62b95ad8-7276-4411-f45e-08d79b47df60",
        "Name": "MountNew"},
    'category_to_create': {
        "Name": "new"}}
HEADER = {
    'header': {
        "accept": "application/json",
        "Content-Type": "application/json-patch+json"}
}

URL_USERS = {
    'user_by_id': "http://34.65.101.58:5002/api/Users/GetUserProfileById?id=",
    'edit_gender': 'http://34.65.101.58:5002/api/Users/EditGender',
    'edit_username': 'http://34.65.101.58:5002/api/Users/EditUsername',
    'edit_user_category': 'http://34.65.101.58:5002/api/Users/EditUserCategory',
    'edit_birthday': 'http://34.65.101.58:5002/api/Users/EditBirthday',
    'set_attitude': 'http://34.65.101.58:5002/api/Users/SetAttitude',
    'url_search_users': "http://34.65.101.58:5002/api/Users/SearchUsers?page=1",
    'url_users': "http://34.65.101.58:5002/api/Users/Get?page=1",
    'url_unblock_user': "http://34.65.101.58:5002/api/Users/Unblock?page=1",
    'url_block_user': "http://34.65.101.58:5002/api/Users/Block?page=1",
}

USER_PAYLOADS = {
    'edit_gender': {
        "id": "e02dfd94-a8a9-4b1a-6cfc-08d7a28d1878",
        "gender": "1"},
    'back_gender': {
        "id": "e02dfd94-a8a9-4b1a-6cfc-08d7a28d1878",
        "gender": "0"}}

URL_CHAT = {
    'id': "f723480e-ad42-4ecb-fa3e-08d7a318593f",
    'id_user': "a1d49d6a-f832-4f2a-32d4-08d79b47df55",
    'id_admin': "038f157b-c102-4578-6cfb-08d7a28d1878",
    'all_chats': "http://34.65.101.58:5002/api/Chat/GetAllChats",
    'get_chat': "http://34.65.101.58:5002/api/chat/GetChat?chatId=f723480e-ad42-4ecb-fa3e-08d7a318593f",
    'unread_messages_user':
        "http://34.65.101.58:5002/api/chat/GetUnreadMessages?userId=a1d49d6a-f832-4f2a-32d4-08d79b47df55"
}
URL_EVENT = {
    'event_edit': "http://34.65.101.58:5002/api/Event/Edit/",
    'block_event': "http://34.65.101.58:5002/api/Event/Block",
    'unblock_event': "http://34.65.101.58:5002/api/Event/Unblock",
    'add_user_to_event': "http://34.65.101.58:5002/api/Event/AddUserToEvent",
    'delete_user_from_event': "http://34.65.101.58:5002/api/Event/DeleteUserFromEvent",
    'set_rating': "http://34.65.101.58:5002/api/Event/SetRate",
    'get_event': "http://34.65.101.58:5002/api/Event/Get",
    'get_all_event': "http://34.65.101.58:5002/api/Event/All",
    'get_rating_event': "http://34.65.101.58:5002/api/Event/GetAverageRate"
}

EVENT_PAYLOAD = {
    'eventId': "?eventId=",
    'blocked': "?Blocked=True&",
    'page': "Page=1"
}
