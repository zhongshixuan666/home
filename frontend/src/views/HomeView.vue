<script setup>
import { media } from '../media'

const IMG = {
  heroMain: media('media/imges/hero-main.jpg'),
  heroBanner: media('media/imges/hero-banner.jpg'),
  axelsen: media('media/imges/axelsen-poster.jpg'),
  leeZijia: media('media/imges/lee-zijia-poster.jpg'),
  gear1: media('media/imges/gear-1.jpg'),
  li1: media('media/imges/li-meimiao-1.jpg'),
  product3: media('media/imges/product-3.png'),
}

const stats = [
  { num: '2026', label: '赛季全程跟踪' },
  { num: '300+', label: '深度报道' },
  { num: '48', label: '球员档案' },
  { num: '12', label: '大赛专栏' },
]

const columns = [
  { num: '01', title: '深度报道', desc: '以数据和现场还原每一场比赛，复盘关键回合与战术变化。' },
  { num: '02', title: '球员档案', desc: '收录世界羽坛顶尖球员的成长路径、荣誉生涯与获奖记录。' },
  { num: '03', title: '装备测评', desc: '球拍、球鞋、羽毛球与配件实测，用真实数据指导选购。' },
  { num: '04', title: '赛事日历', desc: '全年大赛赛程、签表、比分与观赛指南一站式掌握。' },
]

const news = [
  {
    category: '深度',
    title: '2026 赛季过半：男子单打进入群雄逐鹿时代',
    date: '2026.07.28',
    image: IMG.li1,
  },
  {
    category: '赛事',
    title: '全英公开赛前瞻：新老格局的又一次碰撞',
    date: '2026.08.02',
    image: IMG.axelsen,
  },
  {
    category: '人物',
    title: '李梓嘉：暴力进攻背后的体系与坚持',
    date: '2026.07.26',
    image: IMG.leeZijia,
  },
  {
    category: '装备',
    title: '2026 新款高端球拍横评：进攻与控制之争',
    date: '2026.07.20',
    image: IMG.product3,
  },
]

const matches = [
  { date: '08.15', event: '世界羽毛球锦标赛', place: '西班牙 · 马德里', note: '男单 1/4 决赛' },
  { date: '09.02', event: '中国羽毛球公开赛', place: '中国 · 常州', note: '首轮对阵出炉' },
  { date: '09.20', event: '日本羽毛球公开赛', place: '日本 · 大阪', note: '签表公布' },
]
</script>

<template>
  <div>
    <section class="hero">
      <div class="container hero-text">
        <p class="eyebrow">Badminton Journal · Est. 2026</p>
        <h1>羽界</h1>
        <p class="hero-sub">以专业视角，记录羽毛球世界的每一次挥拍与荣耀。</p>
        <div class="hero-actions">
          <RouterLink to="/news" class="btn btn-solid">浏览资讯</RouterLink>
          <RouterLink to="/players" class="btn">球员风采</RouterLink>
        </div>
      </div>
      <div class="container">
        <div class="hero-frame">
          <img :src="IMG.heroMain" alt="羽毛球赛场" />
        </div>
      </div>
    </section>

    <section class="stats">
      <div class="container stats-grid">
        <div v-for="s in stats" :key="s.label" class="stat">
          <p class="stat-num">{{ s.num }}</p>
          <p class="stat-label">{{ s.label }}</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <h2 class="section-title">最新资讯</h2>
          <RouterLink to="/news" class="section-more">全部资讯 →</RouterLink>
        </div>
        <div class="news-grid">
          <RouterLink v-for="n in news" :key="n.title" to="/news" class="news-card card">
            <img :src="n.image" :alt="n.title" />
            <div class="news-body">
              <div class="news-meta">
                <span class="tag">{{ n.category }}</span>
                <span class="news-date">{{ n.date }}</span>
              </div>
              <h3>{{ n.title }}</h3>
            </div>
          </RouterLink>
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="container">
        <div class="section-head">
          <h2 class="section-title">焦点人物</h2>
          <RouterLink to="/players" class="section-more">全部球员 →</RouterLink>
        </div>
        <div class="people-grid">
          <RouterLink to="/players" class="person-card">
            <img :src="IMG.axelsen" alt="安赛龙" />
            <div class="person-info">
              <p class="eyebrow">Denmark · Men's Singles</p>
              <h3>安赛龙</h3>
              <p class="person-note">两届奥运金牌得主，男单统治力标杆。</p>
            </div>
          </RouterLink>
          <RouterLink to="/players" class="person-card">
            <img :src="IMG.leeZijia" alt="李梓嘉" />
            <div class="person-info">
              <p class="eyebrow">Malaysia · Men's Singles</p>
              <h3>李梓嘉</h3>
              <p class="person-note">全英冠军，暴力进攻派的代表人物。</p>
            </div>
          </RouterLink>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <h2 class="section-title">赛事速览</h2>
          <RouterLink to="/matches" class="section-more">全部比赛 →</RouterLink>
        </div>
        <div class="match-grid">
          <div v-for="m in matches" :key="m.event" class="match-card card">
            <p class="match-date">{{ m.date }}</p>
            <h3>{{ m.event }}</h3>
            <p class="match-place">{{ m.place }}</p>
            <p class="match-note">{{ m.note }}</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="container">
        <div class="section-head">
          <h2 class="section-title">栏目纵览</h2>
        </div>
        <div class="columns-grid">
          <div v-for="c in columns" :key="c.num" class="column-card">
            <p class="column-num">{{ c.num }}</p>
            <h3>{{ c.title }}</h3>
            <p>{{ c.desc }}</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <h2 class="section-title">装备精选</h2>
          <RouterLink to="/gear" class="section-more">进入装备区 →</RouterLink>
        </div>
        <div class="gear-feature">
          <img :src="IMG.gear1" alt="装备精选" />
          <div class="gear-text">
            <p class="eyebrow">Gear & Equipment</p>
            <h3>从球拍到拍线，为每一次挥拍负责</h3>
            <p>
              我们实地测评球拍、球鞋、羽毛球与配件，用真实数据帮助你找到适合自己的装备。装备区配有实拍视频，直观展示产品细节。
            </p>
            <RouterLink to="/gear" class="btn">查看装备</RouterLink>
          </div>
        </div>
      </div>
    </section>

    <section class="subscribe">
      <div class="container subscribe-inner">
        <div>
          <p class="eyebrow">Stay Updated</p>
          <h2>不错过任何一场好球</h2>
          <p>关注赛事日历、球员动态与装备测评，订阅我们的每周资讯。</p>
        </div>
        <RouterLink to="/contact" class="btn btn-solid">联系我们</RouterLink>
      </div>
    </section>
  </div>
</template>

<style scoped>
.hero {
  padding: 96px 0 0;
}

.hero-text {
  text-align: center;
}

.hero h1 {
  font-family: var(--serif);
  font-size: 84px;
  font-weight: 600;
  color: var(--paper);
  letter-spacing: 0.34em;
  text-indent: 0.34em;
}

.hero-sub {
  max-width: 560px;
  margin: 22px auto 44px;
  font-size: 17px;
  color: var(--muted);
}

.hero-actions {
  display: flex;
  justify-content: center;
  gap: 20px;
  margin-bottom: 72px;
}

.hero-frame {
  border: 1px solid var(--line);
  border-bottom: none;
  background: var(--bg-soft);
}

.hero-frame img {
  width: 100%;
  height: 520px;
  object-fit: cover;
}

.stats {
  border-bottom: 1px solid var(--line);
  background: var(--bg-soft);
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
}

.stat {
  padding: 44px 24px;
  text-align: center;
  border-right: 1px solid var(--line);
}

.stat:last-child {
  border-right: none;
}

.stat-num {
  font-family: var(--serif);
  font-size: 40px;
  color: var(--gold);
}

.stat-label {
  margin-top: 8px;
  font-size: 13px;
  letter-spacing: 0.24em;
  color: var(--muted);
}

.news-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
}

.news-card img {
  height: 200px;
}

.news-body {
  padding: 22px 24px 26px;
}

.news-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 14px;
}

.news-date {
  font-size: 12px;
  color: var(--muted);
}

.news-body h3 {
  font-family: var(--serif);
  font-size: 17px;
  line-height: 1.55;
  color: var(--paper);
  letter-spacing: 0.04em;
}

.people-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 28px;
}

.person-card {
  background: #ffffff;
  border: 1px solid var(--line);
}

.person-card:hover {
  border-color: var(--gold);
}

.person-card img {
  width: 100%;
  height: 420px;
  object-fit: cover;
}

.person-info {
  padding: 28px 32px 32px;
}

.person-info h3 {
  font-family: var(--serif);
  font-size: 26px;
  color: var(--paper);
  letter-spacing: 0.16em;
}

.person-note {
  margin-top: 10px;
  font-size: 14px;
  color: var(--muted);
}

.match-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.match-card {
  padding: 34px 30px;
  background: #ffffff;
}

.match-date {
  font-family: var(--serif);
  font-size: 30px;
  color: var(--gold);
}

.match-card h3 {
  margin-top: 14px;
  font-family: var(--serif);
  font-size: 20px;
  color: var(--paper);
  letter-spacing: 0.08em;
}

.match-place {
  margin-top: 8px;
  font-size: 13px;
  color: var(--text);
}

.match-note {
  margin-top: 16px;
  padding-top: 14px;
  border-top: 1px solid var(--line);
  font-size: 12px;
  color: var(--muted);
}

.columns-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
}

.column-card {
  padding: 36px 28px;
  border: 1px solid var(--line);
  background: #ffffff;
}

.column-card:hover {
  border-color: var(--gold);
}

.column-num {
  font-family: var(--serif);
  font-size: 26px;
  color: var(--gold);
}

.column-card h3 {
  margin-top: 18px;
  font-family: var(--serif);
  font-size: 19px;
  color: var(--paper);
  letter-spacing: 0.1em;
}

.column-card p:not(.column-num) {
  margin-top: 12px;
  font-size: 13px;
  color: var(--muted);
}

.gear-feature {
  display: grid;
  grid-template-columns: 1.2fr 1fr;
  border: 1px solid var(--line);
  background: #ffffff;
}

.gear-feature img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.gear-text {
  padding: 56px 48px;
}

.gear-text h3 {
  font-family: var(--serif);
  font-size: 26px;
  color: var(--paper);
  line-height: 1.5;
  letter-spacing: 0.06em;
  margin-bottom: 18px;
}

.gear-text p:not(.eyebrow) {
  color: var(--muted);
  font-size: 14px;
  margin-bottom: 32px;
}

.subscribe {
  padding: 96px 0;
  border-top: 1px solid var(--line);
  background: var(--bg-soft);
}

.subscribe-inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 32px;
}

.subscribe h2 {
  font-family: var(--serif);
  font-size: 32px;
  color: var(--paper);
  letter-spacing: 0.14em;
}

.subscribe p:not(.eyebrow) {
  margin-top: 12px;
  color: var(--muted);
  font-size: 15px;
}

@media (max-width: 960px) {
  .news-grid,
  .columns-grid {
    grid-template-columns: 1fr 1fr;
  }
  .people-grid,
  .match-grid,
  .gear-feature {
    grid-template-columns: 1fr;
  }
  .subscribe-inner {
    flex-direction: column;
    text-align: center;
  }
}

@media (max-width: 640px) {
  .stats-grid,
  .news-grid,
  .columns-grid {
    grid-template-columns: 1fr;
  }
}
</style>
