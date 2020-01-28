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
    'payload_change_password': {"oldPassword": "1qaz1qaz", "newPassword": "1qaz1qaz1", "repeatPassword": "1qaz1qaz1"}
}

CATEGORY_PAYLOADS = {
    'category_to_edit': {"Id": "62b95ad8-7276-4411-f45e-08d79b47df60", "Name": "MountNew"},
    'category_to_create': {"Name": "new"}
}
HEADER = {
    'header': {
        "accept": "application/json",
        "Content-Type": "application/json-patch+json"}
}

URL_USERS = {
    'user_by_id_admin': 'http://34.65.101.58:5002/api/Users/GetUserProfileById?id=F320932E-AAC2-4999-32D3-08D79B47DF59',
    'user_by_id_user': 'http://34.65.101.58:5002/api/Users/GetUserProfileById?id=A1D49D6A-F832-4F2A-32D4-08D79B47DF59',
    'user_by_id_vasya': 'http://34.65.101.58:5002/api/Users/GetUserProfileById?id=05a469fe-8f90-479e-ed9a-08d7a0ce42ac',
    'edit_gender': 'http://34.65.101.58:5002/api/Users/EditGender',
    'edit_username': 'http://34.65.101.58:5002/api/Users/EditUsername',
    'edit_user_category': 'http://34.65.101.58:5002/api/Users/EditUserCategory',
    'edit_birthday': 'http://34.65.101.58:5002/api/Users/EditBirthday',
    'url_search_users': "http://34.65.101.58:5002/api/Users/SearchUsers?page=1",
    'url_users': "http://34.65.101.58:5002/api/Users/Get?page=1",
    'url_unblock_user': "http://34.65.101.58:5002/api/Users/Unblock?page=1",
    'url_block_user': "http://34.65.101.58:5002/api/Users/Block?page=1",
}

USER_PAYLOADS = {
    'edit_gender': {
        "id": "f320932e-aac2-4999-32d3-08d79b47df59",
        "gender": "1"},
    'back_gender': {
        "id": "f320932e-aac2-4999-32d3-08d79b47df59",
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
    'url_event_edit': "http://34.65.101.58:5002/api/Event/Edit/"
}
