class Login():
    def user_login(self,b,username,pwd):
        b.find_element_by_class_name("globalLoginBtn").click()
        b.find_element_by_id(uid).clear()
        b.find_element_by_id(uid).send_keys(username)
        b.find_element_by_id(pid).clear()
        b.find_element_by_id(pid).send_keys(pwd)

    def user_logout(self,b):
        b.quit()

uid = "id_account_l"
pid = "id_password_l"

