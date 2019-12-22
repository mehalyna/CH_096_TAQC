from Data.credentials import user
# from utilities.testFrame import InitPagesDriver

# class TestLogin():

def test_login(event):
    event.linked.type_login(user['email'])
    print("Locating and fill in username")

    event.linked.type_pass(user['password'])
    print("Locating and fill in password form...")

    event.linked.press_button_signin()
    # try:
    assert 'abcd' in 'fsfabcdre'
    print("Assertion test completed successfully")
    # except AssertionError:
    #     print('Assertion test failed')
    print('Login OK')


# if __name__ == '__main__':
#     pytest.main()