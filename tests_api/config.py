URL_AUTH = {
    'url_login': "http://34.65.101.58:5002/api/Authentication/Login",
    'url_register': "http://34.65.101.58:5002/api/Authentication/Register",
    'url_login_fb': "http://34.65.101.58:5002/api/Authentication/FacebookLogin",
    'url_login_google': "http://34.65.101.58:5002/api/Authentication/google"}
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
    'category_to_edit': {
        "Id": "F535A1D6-EEC4-4697-B4AD-08D7858FCA63",
        "Name": "MountNew"},
    'category_to_create': {
        "Name": "new"}}
HEADER = {
    'header': {
        "accept": "application/json",
        "Content-Type": "application/json-patch+json"}}

URL_USERS = {
    'user_by_id_admin': 'http://34.65.101.58:5002/api/Users/GetUserProfileById?id=F320932E-AAC2-4999-32D3-08D79B47DF59',
    'user_by_id_user': 'http://34.65.101.58:5002/api/Users/GetUserProfileById?id=A1D49D6A-F832-4F2A-32D4-08D79B47DF59',
    'edit_gender': 'http://34.65.101.58:5002/api/Users/EditGender',
    'edit_username': 'http://34.65.101.58:5002/api/Users/EditUsername',
    'edit_user_category': 'http://34.65.101.58:5002/api/Users/EditUserCategory',
    'edit_birthday': 'http://34.65.101.58:5002/api/Users/EditBirthday'}
USER_PAYLOADS = {
    'edit_gender': {
        "id": "f320932e-aac2-4999-32d3-08d79b47df59",
        "gender": "1"},
    'back_gender': {
        "id": "f320932e-aac2-4999-32d3-08d79b47df59",
        "gender": "0"}}
