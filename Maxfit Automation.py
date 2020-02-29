from selenium import webdriver
from time import sleep


class maxfitAutomation:
    def __init__(self):
        self.url = "https://maxfit-client.herokuapp.com"
        self.driver = webdriver.Chrome("D:\AutomationDrivers\chromedriver")
        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(1)

    # Show Password
    def ShowPassword(self):
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/main/div/div/div/div[2]/form/input').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/main/div/div/div/div[2]/form/input').click()

    # Register
    def Register(self, Email, Fullname, Password, rePassword, Phone, ID):
        # Register Button From Welcome page
        RegisterButton = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[4]/div[1]/a/button')
        RegisterButton.click()

        # Email
        insertEmail = self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/main/div/div/div/div[2]/form/div[1]/div[1]/div/input')
        insertEmail.send_keys(Email)
        sleep(1)

        # Fullname
        insertFullname = self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/main/div/div/div/div[2]/form/div[1]/div[2]/div/input')
        insertFullname.send_keys(Fullname)
        sleep(1)

        # Password
        insertPassword = self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/main/div/div/div/div[2]/form/div[2]/div[1]/div/input')
        insertPassword.send_keys(Password)
        sleep(1)

        # rePassword
        insertRePassword = self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/main/div/div/div/div[2]/form/div[2]/div[2]/div/input')
        insertRePassword.send_keys(rePassword)
        sleep(1)

        # Phone
        insertPhone = self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/main/div/div/div/div[2]/form/div[2]/div[3]/div/input')
        insertPhone.send_keys(Phone)
        sleep(1)

        # ID
        insertID = self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/main/div/div/div/div[2]/form/div[2]/div[4]/div/input')
        insertID.send_keys(ID)
        sleep(1)

        # Register .Click
        RegisterClick = self.driver.find_element_by_xpath('//*[@id="buttonPosition"]')
        RegisterClick.click()
        sleep(2)

    # Login
    def Login(self, Email, Password):
        # Login Button from Welcome page
        LoginButton = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[4]/div[2]/a/button')
        LoginButton.click()

        # Email
        insertEmail = self.driver.find_element_by_xpath('//*[@id="formBasicEmail"]')
        insertEmail.send_keys(Email)
        sleep(1)

        # Password
        insertPassword = self.driver.find_element_by_xpath('//*[@id="formBasicPassword"]')
        insertPassword.send_keys(Password)
        sleep(1)

        # Login .Click
        LoginClick = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/main/div/div/div/div[2]/form/button')
        LoginClick.click()
        sleep(2)

    # MyProfile
    def MyProfile(self):
        MyProfile = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/nav/div/div[2]/a[2]')
        MyProfile.click()
        sleep(1)

    # Processing
    def Processing(self, Weight, Bust, HandScope, Waist):
        Processing = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/a[1]')
        Processing.click()
        sleep(1)

        # Weight
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/div[3]/div/div/div/div/div/p[1]/form/div/div[1]/input').send_keys(Weight)
        sleep(1)
        # Bust
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/div[3]/div/div/div/div/div/p[1]/form/div/div[2]/input').send_keys(Bust)
        sleep(1)
        # HandScope
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/div[3]/div/div/div/div/div/p[2]/form/div/div[1]/input').send_keys(HandScope)
        sleep(1)
        # Waist
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/div[3]/div/div/div/div/div/p[2]/form/div/div[2]/input').send_keys(Waist)
        sleep(1)

        # Processing .Click
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div/div/div/button').click()
        sleep(2)

    # Subscription
    def Subscription(self):
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/a[2]').click()
        sleep(1)

        # Subscription type - Regular
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/div[3]/div/div/div/div/div/div[1]/div[1]/div/span[1]/div/label').click()
        sleep(1)

        # Subscription period - 3 Month
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/div[3]/div/div/div/div/div/div[1]/div[2]/div/span[2]/div/label').click()
        sleep(1)

        # Payment - Cash
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/div[3]/div/div/div/div/div/div[1]/div[3]/div/span[1]/div/label').click()
        sleep(1)

        # Subscription .Click
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/div[3]/div/div/div/div/div/div[2]/div/div[3]/form/button').click()
        sleep(2)

    # TrainingPlan
    def TrainingPlan(self):
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/a[3]').click()
        sleep(1)

        # מסת שריר
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div[3]/div[1]/div[1]/div').click()
        sleep(1)

        # עיצוב וחיטוב
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div[3]/div[2]/div[1]/div').click()
        sleep(1)

        # אירובי
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div[3]/div[3]/div[1]/div').click()
        sleep(1)

        # אימון פונקציונאלי
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div[3]/div[4]/div[1]/div').click()
        sleep(1)

        # Amount of training per week
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div[5]/div/button[3]').click()
        sleep(1)

        # Send Training Plan .Click
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div[6]/div/form/button').click()
        sleep(2)

    # Health
    def Health(self, Firstname, Lastname):
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/a[4]').click()
        sleep(1)

        # Firstname
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/div[3]/div/div[2]/form/div[1]/div/div[1]/input').send_keys(Firstname)
        sleep(1)

        # Lastname
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/div[3]/div/div[2]/form/div[1]/div/div[2]/input').send_keys(Lastname)
        sleep(1)

        # Health .Click
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div[2]/form/div[1]/button').click()
        sleep(2)

    # userSettings
    def userSettings(self):
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/a[5]').click()
        sleep(2)

    # Changing Password
    def ChangePassword(self, Password, NewPassword, ReNewPassword):
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/div[3]/div/div/div/div[2]/div/div[2]/p/form/div[1]/div/input').send_keys(Password)
        sleep(1)

        self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/div[3]/div/div/div/div[2]/div/div[2]/p/form/div[2]/div/input').send_keys(
            NewPassword)
        sleep(1)

        self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/div[3]/div/div/div/div[2]/div/div[2]/p/form/div[3]/div/input').send_keys(
            ReNewPassword)
        sleep(1)

        # Change Password .CLick
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/div[3]/div/div/div/div[2]/div/div[2]/p/form/button').click()
        sleep(2)

    # Changing Mail
    def ChangingMail(self, Email, reMail):
        self.driver.find_element_by_xpath(
            '//*[@id="formPlaintextEmail"]').send_keys(Email)
        sleep(1)

        self.driver.find_element_by_name('reEmail').send_keys(reMail)
        sleep(1)

        self.driver.find_element_by_xpath('//*[@id="buttonEmail"]').click()
        sleep(2)

    # Live
    def Live(self):
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/nav/div/div[2]/a[3]').click()
        sleep(3)

    # Store
    def Store(self):
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/nav/div/div[2]/a[4]').click()
        sleep(2)

        # Shift Right()
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div/div[1]/a[2]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div/div[1]/a[2]').click()
        sleep(1)

        # Shift Left()
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div/div[2]/a[1]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div/div[2]/a[2]').click()
        sleep(2)

    def Notifications(self):
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[1]/nav/div/div[2]/a[5]').click()
        sleep(3)

    # LogOut
    def LogOut(self):
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/nav/div/a/button').click()
        sleep(1)


# Main:

Email = "Automation@gmail.com"
Fullname = "Test Automation"
splitFullname = Fullname.split(' ')
Password = "123456"
rePassword = "123456"
Phone = "0502241114"
ID = "123456789"
NewPass = "12345678"

# testCases:

# testAutomation = maxfitAutomation()
# testAutomation.ShowPassword()
# testAutomation.Register(Email, Fullname, Password, rePassword, Phone, ID)
# testAutomation.Login(Mail, Password)
# testAutomation.MyProfile()
# testAutomation.Processing("1.70", "50", "20", "40")
# testAutomation.Subscription()
# testAutomation.TrainingPlan()
# testAutomation.Health(splitFullname[0], splitFullname[1])
# testAutomation.userSettings()
# testAutomation.ChangePassword(Password, "12345678", "12345678")
# testAutomation.ChangingMail("Automation1@gmail.com", "Automation1@gmail1.com")
# testAutomation.Live()
# testAutomation.Store()
# testAutomation.Notifications()
# testAutomation.LogOut()

# Active Cases:
testAutomation = maxfitAutomation()
testAutomation.Login(Email, Password)

