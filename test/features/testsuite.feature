Feature:andriod_apk
Scenario:login

Given login成功启动页面
When 点击单选框,点击同意,点击下一步,点击下一步,点击下一步,点击完成,点击权限框,输入账号18621263786,输入密码1qaz2wsx,点击登陆
Then 判断是否是订单页面


Feature:andriod_apk1
Scenario:login2

Given 进入订单页面
When 点击数字1,点击数字2,点击数字3,点击数字4,点击数字1,点击数字2,点击数字3,点击数字4
Then 判断是否登陆成功