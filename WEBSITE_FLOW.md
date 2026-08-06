# 网站制作到部署完整流程

## 当前状态

- 本地项目路径：`B:\Users\轩\Documents\sport_website`
- 线上静态预览：`https://zhongshixuan666.github.io/home/`
- 前端：Vue 3 + Vite 多页面 HTML，已完成
- 后端：Django + SQLite + 内容 API，已完成
- 线上：GitHub Pages 静态版已上线
- 未完成：Django 后端尚未部署到服务器
- 未完成：前端页面尚未真正从 API 读取数据库数据

## 制作流程

### 1. 需求与设计

- 明确网站定位、页面、用户操作和线上访问方式
- 区分静态展示、表单提交、后台管理是否需要后端
- 当前需求：资讯、球员、比赛、装备展示，联系表单，后台数据管理

### 2. 数据设计

- 联系留言：`Contract`
- 新闻资讯：`NewsArticle`
- 球员档案：`PlayerProfile`
- 比赛赛程：`MatchSchedule`
- 装备产品：`Product`

新增模型后必须执行：

```bash
.venv/Scripts/python.exe manage.py makemigrations core
.venv/Scripts/python.exe manage.py migrate core
```

### 3. 后端 API

接口统一放在 `/api/` 下：

```text
POST /api/contact/
GET/POST /api/news/
GET/POST /api/players/
GET/POST /api/matches/
GET/POST /api/products/
```

详情接口支持 `GET / PATCH / DELETE`，文档见 `API.md`。

### 4. 前端开发

- 页面入口：`frontend/*.html`
- 页面组件：`frontend/src/views/`
- 公共布局：`frontend/src/components/PageShell.vue`
- 页面入口脚本：`frontend/src/entries/`
- 前端访问 API 时统一走 `/api/`，由 Vite 代理到 Django

### 5. 测试

```bash
.venv/Scripts/python.exe manage.py check
.venv/Scripts/python.exe manage.py test core
cd frontend
npm run build
```

### 6. 本地运行

```bash
.venv/Scripts/python.exe manage.py runserver 127.0.0.1:8000
cd frontend
npm run dev
```

本地访问：

- 前端：`http://127.0.0.1:5173/`
- 后端：`http://127.0.0.1:8000/`
- 后台：`http://127.0.0.1:8000/admin/`

## 部署流程

### 方式一：GitHub Pages 静态预览

- 推送 `main` 后自动构建
- 在线地址：`https://zhongshixuan666.github.io/home/`
- 适用：静态页面预览、图片视频展示
- 不适用：联系表单、后台管理、数据库 API

### 方式三：客户静态版

- 目录：`C:\Users\轩\Desktop\36钟世轩\网站静态版`
- 直接双击 `index.html` 即可查看完整页面，不需要运行服务
- 联系表单、后台管理和 API 仍需要在线服务或本地 Django

### 方式二：完整线上部署

需要一台服务器，并安装 Docker 与 Docker Compose。

```bash
git clone https://github.com/zhongshixuan666/home.git
cd home
cp .env.production.example .env.production
```

修改 `.env.production`：

```dotenv
DJANGO_SECRET_KEY=随机密钥
DJANGO_ALLOWED_HOSTS=域名或服务器IP
DJANGO_CSRF_TRUSTED_ORIGINS=https://域名
DJANGO_HTTPS=1
```

启动：

```bash
touch db.sqlite3
docker compose up -d --build
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```

部署后访问：

- 网站：`http://服务器IP:8000/`
- 后台：`http://服务器IP:8000/admin/`

正式域名建议用 Nginx 或 Caddy 反代到 `8000` 端口并配置 HTTPS。

## 反思与待改进

1. 前端页面仍使用硬编码数据，尚未读取数据库 API，下一步应逐页接入真实数据。
2. Django 后端尚未上线，联系表单在线暂不可用，需要完成服务器部署。
3. API 目前未做登录鉴权和访问控制，仅适合开发演示，正式上线前需要 Token 鉴权、CSRF 与权限管理。
4. GitHub Actions 只构建前端，尚未自动跑 Django 测试和 Docker 构建，CI 覆盖不完整。
5. 当前使用 SQLite，适合演示和低并发；正式运营建议迁移到 PostgreSQL，并配置备份。
6. 媒体已优化但仍由单台服务器提供，后续可按需迁移到对象存储或 CDN。
7. 联系表单已展示真实后端错误，但仍缺少成功后的邮件通知、防刷验证码和限流。
8. 部署流程缺少一键脚本和回滚方案，后续可补充部署脚本与版本发布记录。
