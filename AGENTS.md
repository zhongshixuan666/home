# AGENTS.md

## 项目概述

运动主题网站（Sport Website），前后端分离架构：

- **后端**：Django 6.0.8（Python 3.12），提供管理后台与 JSON API
- **前端**：Vue 3 + Vite 8，单页应用，开发时通过 Vite 代理访问后端
- **后台管理**：Django Admin + SimpleUI，界面语言为简体中文
- **数据库**：SQLite（本地开发）

## 常用命令

### 后端（在项目根目录执行）

```powershell
# 激活虚拟环境
.\.venv\Scripts\Activate.ps1

# 启动 Django 开发服务器（http://127.0.0.1:8000/）
python manage.py runserver

# 检查配置
python manage.py check

# 应用数据库迁移
python manage.py migrate

# 创建超级管理员
python manage.py createsuperuser

# 运行测试
python manage.py test
```

### 前端（在 frontend/ 目录执行）

```powershell
npm install    # 安装依赖
npm run dev    # 启动 Vite 开发服务器（http://127.0.0.1:5173/）
npm run build  # 构建生产产物到 frontend/dist/
```

## 项目结构

```
sport_website/
├── manage.py              # Django 入口
├── sport_website/         # Django 项目配置（settings/urls）
├── core/                  # 核心业务应用（API 视图、模型）
├── frontend/              # Vue 3 前端
│   ├── src/               # 前端源码
│   └── vite.config.js     # 含 /api 代理配置
├── requirements.txt       # Python 依赖
└── .gitignore
```

## 架构约定

- 前端访问后端统一走 `/api/` 前缀；Vite 开发服务器会把 `/api` 请求代理到 `http://127.0.0.1:8000`（见 `frontend/vite.config.js`）
- 桌面素材通过 `/media/video/` 与 `/media/imges/` 映射到 `C:\Users\轩\Desktop\video` 与 `C:\Users\轩\Desktop\imges`（仅 Vite 开发/预览模式可用）
- 管理后台固定在 `/admin/`，使用 SimpleUI 主题
- 联系表单提交到 `POST /api/contact/`，数据存入 SQLite 的 `contract` 表，后台一级菜单「联系表单」下可管理
- 业务接口写在 `core/` 应用中：视图在 `core/views.py`，路由在 `core/urls.py`，并在 `sport_website/urls.py` 中用 `include` 挂载
- 新增数据库模型后必须执行 `python manage.py makemigrations && python manage.py migrate`
- 前端页面使用中文文案；语言/时区已配置为 `zh-hans` / `Asia/Shanghai`

## 开发约定

- 修改后端后如需立即生效，请重启 `runserver`（后台启动时通常带 `--noreload`）
- 新增 Python 依赖后同步更新 `requirements.txt`（可用 `pip freeze`）
- 新增前端依赖后 `package-lock.json` 会自动更新，一并提交
- `.venv/`、`frontend/node_modules/`、`frontend/dist/`、`db.sqlite3` 均不提交到 git
- 超级管理员账号仅存在于本地数据库，凭据不要写入任何提交到仓库的文件

## 当前状态

- 本地已有超级管理员账号（`raining`），可在 `/admin/` 登录，后台使用 SimpleUI 主题并配置了「联系表单」菜单
- 后端接口：`GET /api/home/`（站点信息）、`POST /api/contact/`（联系表单，写入 `contract` 表）
- 前端为「羽界」品牌六页面站（首页/资讯/球员/比赛/联系我们/装备），球员页含照片轮播，装备页引用桌面视频素材
