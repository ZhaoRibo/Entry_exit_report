from selenium import webdriver

# 个人信息
userName = input('学号：')
password = input('密码：')
email = input('邮箱：')
phone = input('电话：')

# 打开门户并进入认证界面
driver = webdriver.Chrome("chromedriver.exe")   # 填写自己电脑浏览器驱动程序位置
driver.get(
    r"https://portal.pku.edu.cn/portal2017/#/index?rand=0.9019998387126195")
driver.find_element_by_xpath(
    '//*[@id="ng-app"]/div[1]/header/section/section[1]/section[2]/ul[1]/li/a'
).click()

# 统一登陆认证
driver.find_element_by_name('userName').send_keys(userName)
driver.find_element_by_name('password').send_keys(password)
driver.find_element_by_xpath('//*[@id="logon_button"]').click()

# 进入出入校备案页面
if driver.find_element_by_xpath(
        '//*[@id="bizTip"]/div/div/div[1]/div/div/table/tbody/tr[11]/td/a'
).is_displayed():
    driver.find_element_by_xpath(
        '//*[@id="bizTip"]/div/div/div[1]/div/div/table/tbody/tr[11]/td/a'
    ).click()
driver.find_element_by_xpath('//*[@id="all"]').click()
driver.find_element_by_xpath('//*[@id="tag_s_stuCampusExEnReq"]').click()
n = driver.window_handles
driver.switch_to.window(n[1])
driver.find_element_by_xpath(
    '/html/body/div/section/div/div/div[2]/main/div[3]/a/div').click()

##########################
# 出校备案
##########################

# 出校/入校：出校
driver.find_element_by_xpath(
    '/html/body/div/section/div/div/div[2]/main/div/div[2]/form/div/div[3]/div/div/div/div[1]/input'
).click()
driver.find_element_by_xpath(
    '/html/body/div[2]/div[1]/div[1]/ul/li[1]').click()
# 所在校区
driver.find_element_by_xpath(
    '/html/body/div[1]/section/div/div/div[2]/main/div/div[2]/form/div/div[4]/div/div/div/div/input'
).click()
driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click(
)  # xpath末尾’/ui/li[_i]',_i可取1,2,3,4,分别对应 燕园 万柳 畅春 圆明园
# 邮箱填写
elm_emial = driver.find_element_by_xpath(
    '/html/body/div[1]/section/div/div/div[2]/main/div/div[2]/form/div/div[5]/div/div/div/input'
)
if elm_emial.get_attribute('value') == email:
    pass
else:
    elm_emial.clear()
    elm_emial.send_keys(email)
# 手机号填写
elm_phone = driver.find_element_by_xpath(
    '/html/body/div[1]/section/div/div/div[2]/main/div/div[2]/form/div/div[6]/div/div/div/input'
)
if elm_phone.get_attribute('value') == phone:
    pass
else:
    elm_phone.clear()
    elm_phone.send_keys(phone)
# 出入校事由
driver.find_element_by_xpath(
    '/html/body/div[1]/section/div/div/div[2]/main/div/div[2]/form/div/div[7]/div/div/div[1]/textarea'
).send_keys('做实验')
# 出校目的地：默认北京（改动需要自行调整后续代码）
driver.find_element_by_xpath(
    '/html/body/div[1]/section/div/div/div[2]/main/div/div[2]/form/div/div[8]/div[2]/div/div/div/div/input'
).click()
driver.find_element_by_xpath(
    '/html/body/div[4]/div[1]/div[1]/ul/li[1]').click()
# 出校行动轨迹
driver.find_element_by_xpath(
    '/html/body/div[1]/section/div/div/div[2]/main/div/div[2]/form/div/div[8]/div[3]/div/div/div[1]/textarea'
).send_keys('北大东门-物理学院-北大东门')
# 勾选本人遵守疫情防控要求。。。
if driver.find_element_by_xpath(
        '/html/body/div[1]/section/div/div/div[2]/main/div/div[2]/form/div/div[9]/div/div/label/span[1]/span'
).is_selected():
    pass
else:
    driver.find_element_by_xpath(
        '/html/body/div[1]/section/div/div/div[2]/main/div/div[2]/form/div/div[9]/div/div/label/span[1]/span'
    ).click()
# 保存
driver.find_element_by_xpath(
    '/html/body/div[1]/section/div/div/div[2]/main/div/div[2]/form/div/div[10]/div/div/div/div[1]/button'
).click()
driver.find_element_by_xpath('/html/body/div[5]/div/div[3]/button[2]').click()
driver.find_element_by_xpath('/html/body/div[6]/div/div[3]/button[2]').click()
driver.find_element_by_xpath(
    '/html/body/div[1]/section/div/div/div[2]/main/div/div[1]/div/div/div[1]'
).click()

##########################
# 入校备案
##########################

driver.find_element_by_xpath(
    '/html/body/div/section/div/div/div[2]/main/div[3]/a/div').click()

# 出校/入校：入校
driver.find_element_by_xpath(
    '/html/body/div/section/div/div/div[2]/main/div/div[2]/form/div/div[3]/div/div/div/div[1]/input'
).click()
driver.find_element_by_xpath(
    '/html/body/div[3]/div[1]/div[1]/ul/li[2]').click()
# 所在校区
driver.find_element_by_xpath(
    '/html/body/div[1]/section/div/div/div[2]/main/div/div[2]/form/div/div[4]/div/div/div/div/input'
).click()
driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[1]').click(
)  # xpath末尾’/ui/li[_i]',_i可取1,2,3,4,分别对应 燕园 万柳 畅春 圆明园
# 邮箱填写
elm_emial = driver.find_element_by_xpath(
    '/html/body/div[1]/section/div/div/div[2]/main/div/div[2]/form/div/div[5]/div/div/div/input'
)
if elm_emial.get_attribute('value') == email:
    pass
else:
    elm_emial.clear()
    elm_emial.send_keys(email)
# 手机号填写
elm_phone = driver.find_element_by_xpath(
    '/html/body/div[1]/section/div/div/div[2]/main/div/div[2]/form/div/div[6]/div/div/div/input'
)
if elm_phone.get_attribute('value') == phone:
    pass
else:
    elm_phone.clear()
    elm_phone.send_keys(phone)
# 出入校事由
driver.find_element_by_xpath(
    '/html/body/div[1]/section/div/div/div[2]/main/div/div[2]/form/div/div[7]/div/div/div[1]/textarea'
).send_keys('做实验')
# 入校前居住地：默认北京（改动需要自行调整后续代码）
driver.find_element_by_xpath(
    '/html/body/div[1]/section/div/div/div[2]/main/div/div[2]/form/div/div[8]/div[2]/div[1]/div/div/div/div/input'
).click()
driver.find_element_by_xpath(
    '/html/body/div[5]/div[1]/div[1]/ul/li[1]').click()
# 居住地所在区：默认海淀
driver.find_element_by_xpath(
    '/html/body/div[1]/section/div/div/div[2]/main/div/div[2]/form/div/div[8]/div[2]/div[2]/div/div/div/div/input'
).click()
driver.find_element_by_xpath(
    '/html/body/div[6]/div[1]/div[1]/ul/li[7]').click()
# 居住地所在区：默认燕园街道
driver.find_element_by_xpath(
    '/html/body/div[1]/section/div/div/div[2]/main/div/div[2]/form/div/div[8]/div[2]/div[3]/div/div/div[1]/textarea'
).send_keys('燕园街道')
# 14日内是否一直在京与抵京日期
'''
driver.find_element_by_xpath(
    '/html/body/div[1]/section/div/div/div[2]/main/div/div[2]/form/div/div[8]/div[2]/div[4]/div/div/div/label[1]'
).click()   # 14日是否抵京若选择为‘是’，请启用此段代码，并注释或者删除下段代码
'''
driver.find_element_by_xpath(
    '/html/body/div[1]/section/div/div/div[2]/main/div/div[2]/form/div/div[8]/div[2]/div[4]/div/div/div/label[2]'
).click()
driver.find_element_by_xpath(
    '/html/body/div[1]/section/div/div/div[2]/main/div/div[2]/form/div/div[8]/div[2]/div[5]/div/div/div/input'
).click()
driver.find_element_by_xpath(
    '/html/body/div[7]/div[1]/div/div[1]/button[2]').click()
driver.find_element_by_xpath(
    '/html/body/div[7]/div[1]/div/div[2]/table[1]/tbody/tr[6]/td[6]/div'
).click()  # 选择抵京日期，默认为8月28日，若为29日返京请讲xpath最后的数字改为'7',其他日期请自行更改此两行代码或联系作者

# 勾选本人遵守疫情防控要求。。。
if driver.find_element_by_xpath(
        '/html/body/div[1]/section/div/div/div[2]/main/div/div[2]/form/div/div[9]/div/div/label/span[1]/span'
).is_selected():
    pass
else:
    driver.find_element_by_xpath(
        '/html/body/div[1]/section/div/div/div[2]/main/div/div[2]/form/div/div[9]/div/div/label/span[1]/span'
    ).click()
# 保存
driver.find_element_by_xpath(
    '/html/body/div[1]/section/div/div/div[2]/main/div/div[2]/form/div/div[10]/div/div/div/div[1]/button'
).click()
driver.find_element_by_xpath('/html/body/div[7]/div/div[3]/button[2]').click()
driver.find_element_by_xpath('/html/body/div[8]/div/div[3]/button[2]').click()
driver.find_element_by_xpath(
    '/html/body/div[1]/section/div/div/div[2]/main/div/div[1]/div/div/div[1]'
).click()

# 打开备案历史
driver.find_element_by_xpath(
    '/html/body/div[1]/section/div/div/div[2]/main/div[5]/a/div').click()
