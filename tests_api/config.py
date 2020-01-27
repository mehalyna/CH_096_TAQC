URL_AUTH = {
    'url_login': "http://34.65.101.58:5002/api/Authentication/Login",
    'url_register': "http://34.65.101.58:5002/api/Authentication/Register",
    'url_login_fb': "http://34.65.101.58:5002/api/Authentication/FacebookLogin",
    'url_login_google': "http://34.65.101.58:5002/api/Authentication/google"
}
URL_CATEGORY = {
    'url_category_edit': "http://34.65.101.58:5002/api/Category/Edit",
    'url_category_all': "http://34.65.101.58:5002/api/Category/All",
    'url_category_delete': "http://34.65.101.58:5002/api/Category/Delete/"
}

AUTH_PAYLOADS = {
    'payload_admin': {"Email": "admin@gmail.com", "Password": "1qaz1qaz"},
    'payload_user': {"Email": "user@gmail.com", "Password": "1qaz1qaz"},
    'payload_unauth': {"Email": "katya@gmail.com", "Password": "123"}
}

CATEGORY_PAYLOADS = {
    'category_to_edit': {"Id": "62b95ad8-7276-4411-f45e-08d79b47df60", "Name": "MountNew"},
    'category_to_create': {"Name": "new"}
}
HEADER = {
    'header': {"accept": "application/json", "Content-Type": "application/json-patch+json"}
}

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