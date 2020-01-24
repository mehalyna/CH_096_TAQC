URL_AUTH = {
    'url_login': "http://localhost:50621/api/Authentication/Login",
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
    'id': "b410fa81-d64a-4572-2721-08d766a5bece",
    'all_chats': "http://34.65.101.58:5002/api/Chat/GetAllChats",
    'get_chat': "http://localhost:50621/api/Chat/GetChat?chatId=b410fa81-d64a-4572-2721-08d766a5bece",
    'unread_messages_user':
        "http://localhost:50621/api/Chat/GetUnreadMessages?userId=e948eb47-ef5b-4142-ab44-08d76385302a"
}
URL_EVENT = {
    'url_event_edit': "http://34.65.101.58:5002/api/Event/Edit/"
}