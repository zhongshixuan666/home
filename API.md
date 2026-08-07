# 羽界内容 API

所有接口返回 JSON。开发环境后端地址：`http://127.0.0.1:8000`。

当前接口用于演示数据录入，未做登录鉴权，并使用了 `csrf_exempt`。正式上线时建议增加 Token 鉴权、CSRF 防护和字段级权限控制。

## 通用规则

- 集合接口：`GET /api/news/` 获取列表，`POST /api/news/` 新增。
- 详情接口：`GET /api/news/<id>/`、`PATCH /api/news/<id>/`、`DELETE /api/news/<id>/`。
- 详情接口同时兼容不带结尾斜杠的地址，例如 `/api/news/1`。
- 新增成功返回 `201`，字段校验失败返回 `400`，记录不存在返回 `404`。
- 未发布字段 `is_published` 接受 `true/false/1/0/yes/no/on/off`。

## 登录注册

发送验证码：

`POST /api/auth/send-code/`

```json
{
  "channel": "phone",
  "account": "13800138000",
  "purpose": "register"
}
```

`channel` 可选：`phone`、`email`。开发模式下响应会附带 `dev_code`。

注册：

`POST /api/auth/register/`

```json
{
  "username": "shiyuqi",
  "password": "test123456",
  "phone": "13800138000",
  "email": "shi@yujie.com",
  "channel": "phone",
  "code": "123456"
}
```

登录：

`POST /api/auth/login/`

```json
{
  "account": "13800138000",
  "password": "test123456"
}
```

`account` 支持用户名、手机号或邮箱。其他接口：

```text
GET  /api/auth/me/
POST /api/auth/logout/
```

## 新闻

`POST /api/news/`

```json
{
  "title": "国羽新德里世锦赛前瞻",
  "category": "赛事",
  "date": "2026-08-17",
  "excerpt": "石宇奇领衔国羽出战。",
  "image": "/home/images/hero-main.webp",
  "is_published": true
}
```

必填字段：`title`。

## 球员

`POST /api/players/`

```json
{
  "name": "石宇奇",
  "en_name": "Shi Yu Qi",
  "country": "中国 · China",
  "birth": "1996.02.28",
  "height": "183 cm",
  "status": "男单世界第一",
  "style": "快速连贯的进攻体系",
  "bio": "2025 年世锦赛男单冠军。",
  "image": "/home/images/shi-yu-qi.jpg",
  "video": "/home/videos/shi-yu-qi-web.mp4",
  "is_published": true
}
```

必填字段：`name`。

## 比赛

`POST /api/matches/`

```json
{
  "match_type": "upcoming",
  "date": "08.17-08.23",
  "time": "至 08.23",
  "event": "世界羽毛球锦标赛",
  "stage": "64强至决赛",
  "venue": "印度 · 新德里",
  "watch": "石宇奇冲击卫冕",
  "player_a": "",
  "player_b": "",
  "score": "",
  "result": "",
  "champion": "",
  "is_published": true
}
```

`match_type` 可选值：`upcoming`、`result`、`champion`。

必填字段：`event`。

## 装备

`POST /api/products/`

```json
{
  "name": "旗舰进攻型球拍",
  "desc": "高刚性拍框，重杀出球干脆。",
  "image": "/home/images/product-1.jpeg",
  "tag": "球拍",
  "rank": "1",
  "score": "9.2",
  "is_published": true
}
```

必填字段：`name`。


## 社区投稿

`POST /api/community/`

```json
{
  "title": "聊聊这周的比赛",
  "content": "我觉得国羽男单的防守质量明显提升了。",
  "author": "羽球少年",
  "category": "赛事讨论"
}
```

`category` 可选值：`球迷投稿`、`赛事讨论`、`装备交流`、`训练心得`、`其他`。

必填字段：`title`、`content`、`author`。

热搜榜：

`GET /api/community/hot/`

返回按 `hot_score`、`views`、`likes` 排序的前 10 条内容。

## 后台管理

`/admin/` 登录后可在「内容数据」菜单下管理：

- 新闻资讯：`/admin/core/newsarticle/`
- 球员档案：`/admin/core/playerprofile/`
- 比赛赛程：`/admin/core/matchschedule/`
- 装备产品：`/admin/core/product/`
- 社区投稿：`/admin/core/communitypost/`
