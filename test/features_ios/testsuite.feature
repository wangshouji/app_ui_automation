Feature:_andriod_apk
Scenario:login

Given login成功启动页面
When 点击跳过,点击单选框,点击同意,输入手机号码18621263786,输入密码1qaz2wsx,点击登陆
Then 判断是否是订单页面


Feature:_andriod_apk1
Scenario:login2

Given 进入订单页面
When 点击数字1,点击数字2,点击数字3,点击数字4,点击数字1,点击数字2,点击数字3,点击数字4
Then 判断是否登陆成功