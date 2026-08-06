# 线上部署说明

## 架构

- Django（gunicorn + WhiteNoise）在 8000 端口提供：管理后台、`/api/` 接口、`/media/` 素材、Vue 构建产物
- Vue 前端由 Dockerfile 分阶段构建，产物由 Django 兜底路由托管
- 生产配置使用 `sport_website/settings_prod.py`，关键值通过环境变量注入

## 准备工作

1. 生成随机密钥并创建环境文件：

   ```powershell
   python -c "import secrets; print(secrets.token_urlsafe(50))"
   Copy-Item .env.production.example .env.production
   # 编辑 .env.production 填入密钥、域名
   ```

2. 媒体素材已包含在仓库的 `frontend/public/media/` 中，Docker 构建时会自动复制到容器 `media/` 目录，不需要在服务器上重新上传桌面素材：

   ```powershell
   # 本地如需调试桌面原始素材，可运行：
   .\scripts\prepare_media.ps1
   ```

3. 在服务器上执行（需安装 Docker）：

   ```bash
   docker compose up -d --build
   docker compose exec web python manage.py migrate
   docker compose exec web python manage.py createsuperuser
   ```

4. 首次部署前若宿主机不存在 db.sqlite3，请先创建空文件：

   ```bash
   touch db.sqlite3
   ```

## 域名与 HTTPS

- 建议在服务器上用 Nginx/Caddy 反向代理到 127.0.0.1:8000，并配置 HTTPS
- `DJANGO_HTTPS=1` 会开启 Cookie 安全标记；有代理时请设置 `SECURE_PROXY_SSL_HEADER`（settings_prod.py 已内置）
- 更新域名后同步修改 `.env.production` 中的 `DJANGO_ALLOWED_HOSTS` 与 `DJANGO_CSRF_TRUSTED_ORIGINS`

## 更新发布

```bash
git pull
docker compose up -d --build
docker compose exec web python manage.py migrate
```

## 注意

- `media/`、`staticfiles/`、`db.sqlite3`、`.env.production` 均不提交到 git
- 生产环境必须更换 `DJANGO_SECRET_KEY`，并避免使用默认弱密码
- 演示部署直接由 Django 提供媒体文件；流量较大时建议改用对象存储或 Nginx 托管

## GitHub Pages 部署（前端静态版）

GitHub Pages 只能托管静态文件，无法运行 Django。前端已支持子路径部署：

- 站点资源（图片/视频）已复制到 `frontend/public/media/`，随构建发布
- 前端构建为多页面 HTML：`index.html`、`news.html`、`players.html`、`matches.html`、`contact.html`、`gear.html`
- 媒体路径自动适配部署前缀（开发环境 `/`，Pages 为 `/home/`）

推送 `main` 分支后，[`.github/workflows/deploy.yml`](.github/workflows/deploy.yml) 会自动构建前端并发布到 GitHub Pages。

注意：此模式下「联系表单」提交与后台管理不可用（需要后端），需要完整功能请使用 Docker 方案部署到服务器。
