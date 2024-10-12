# 使用 Flask-mangger 管理数据库

```sh
# 设置启动的App
set FLASK_APP=app
# 配置环境
set FLASK_ENV=development 

# 初始化仓库
flask db init
# 创建迁移脚本
flask db migrate -m "initial migration"
# 更新数据库1
flask db upgrade
```
