<script setup>
import { media } from '../media'
import SkeletonLoader from '../components/SkeletonLoader.vue'
import { useFakeLoad } from '../composables/useFakeLoad'

const IMG = {
  heroMain: media('images/hero-main.webp'),
  heroBanner: media('images/hero-banner.webp'),
  axelsen: media('images/an-sai-long.jpg'),
  leeZijia: media('images/li-zi-jia.jpg'),
  gear1: media('images/gear-1.jpg'),
  li1: media('images/li-meimiao-2.jpg'),
  product3: media('images/product-3.webp'),
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
  { date: '08.17', event: '世界羽毛球锦标赛', place: '印度 · 新德里', note: '8月17-23日' },
  { date: '09.01', event: '李宁·中国羽毛球大师赛', place: '中国 · 深圳', note: '超级750' },
  { date: '09.06', event: '全国羽毛球单项锦标赛', place: '中国 · 合肥', note: '9月6-13日' },
]
const { loading } = useFakeLoad(650)
</script>

<template>
  <div>
    <section class="hero">
      <div class="container hero-text">
        <p class="eyebrow">Badminton Journal · Est. 2026</p>
        <h1>羽界</h1>
        <p class="hero-sub">以专业视角，记录羽毛球世界的每一次挥拍与荣耀。</p>
        <div class="hero-actions">
          <a :href="media('pages/news.html')" class="btn btn-solid">浏览资讯</a>
          <a :href="media('pages/players.html')" class="btn">球员风采</a>
        </div>
      </div>
      <div class="container">
        <div class="hero-frame">
          <SkeletonLoader v-if="loading" variant="hero" :img-height="520" />
          <img v-else :src="IMG.heroMain" alt="羽毛球赛场" />
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
          <a :href="media('pages/news.html')" class="section-more">全部资讯 →</a>
        </div>
        <SkeletonLoader v-if="loading" variant="grid" :count="4" :cols="4" />
        <div v-else class="news-grid">
          <a v-for="n in news" :key="n.title" :href="media('pages/news.html')" class="news-card card micro-card">
            <img :src="n.image" :alt="n.title" loading="lazy" />
            <div class="news-body">
              <div class="news-meta">
                <span class="tag">{{ n.category }}</span>
                <span class="news-date">{{ n.date }}</span>
              </div>
              <h3>{{ n.title }}</h3>
            </div>
          </a>
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="container">
        <div class="section-head">
          <h2 class="section-title">焦点人物</h2>
          <a :href="media('pages/players.html')" class="section-more">全部球员 →</a>
        </div>
        <SkeletonLoader v-if="loading" variant="grid" :count="2" :cols="2" :img-height="420" />
        <div v-else class="people-grid">
          <a :href="media('pages/players.html')" class="person-card micro-card">
            <img :src="IMG.axelsen" alt="安赛龙" loading="lazy" />
            <div class="person-info">
              <p class="person-meta">丹麦 · 男单</p>
              <h3>安赛龙</h3>
              <p class="person-note">两届奥运金牌得主，2026年4月因反复腰伤退役。</p>
            </div>
          </a>
          <a :href="media('pages/players.html')" class="person-card micro-card">
            <img :src="IMG.leeZijia" alt="李梓嘉" loading="lazy" />
            <div class="person-info">
              <p class="person-meta">马来西亚 · 男单</p>
              <h3>李梓嘉</h3>
              <p class="person-note">全英冠军，暴力进攻派的代表人物。</p>
            </div>
          </a>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <h2 class="section-title">赛事速览</h2>
          <a :href="media('pages/matches.html')" class="section-more">全部比赛 →</a>
        </div>
        <SkeletonLoader v-if="loading" variant="grid" :count="3" :cols="3" :img-height="0" />
        <div v-else class="match-grid">
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
          <div v-for="c in columns" :key="c.num" class="column-row">
            <span class="column-num">{{ c.num }}</span>
            <div class="column-body">
              <h3>{{ c.title }}</h3>
              <p>{{ c.desc }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <h2 class="section-title">装备精选</h2>
          <a :href="media('pages/gear.html')" class="section-more">进入装备区 →</a>
        </div>
        <div class="gear-feature micro-card">
          <img :src="IMG.gear1" alt="装备精选" loading="lazy" />
          <div class="gear-text">
            <p class="eyebrow">Gear & Equipment</p>
            <h3>从球拍到拍线，为每一次挥拍负责</h3>
            <p>
              我们实地测评球拍、球鞋、羽毛球与配件，用真实数据帮助你找到适合自己的装备。装备区配有实拍视频，直观展示产品细节。
            </p>
            <a :href="media('pages/gear.html')" class="btn">查看装备</a>
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
        <a :href="media('pages/contact.html')" class="btn btn-solid">联系我们</a>
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
  margin-bottom: 84px;
}

.hero-frame {
  border: 1px solid var(--line);
  border-bottom: none;
  background: var(--bg-soft);
}

.hero-frame img {
  width: 100%;
  height: 540px;
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
  padding: 52px 24px;
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
  gap: 32px;
}

.news-card img {
  height: 200px;
}

.news-body {
  padding: 26px 28px 30px;
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
  gap: 36px;
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
  padding: 32px 36px 36px;
}

.person-info h3 {
  font-family: var(--serif);
  font-size: 26px;
  color: var(--paper);
  letter-spacing: 0.16em;
}

.person-meta {
  font-size: 12px;
  letter-spacing: 0.16em;
  color: var(--muted);
  margin-bottom: 8px;
}

.person-note {
  margin-top: 10px;
  font-size: 14px;
  color: var(--muted);
}

.match-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 32px;
}

.match-card {
  padding: 40px 34px;
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
  border-top: 1px solid var(--line);
}

.column-row {
  display: grid;
  grid-template-columns: 120px 1fr;
  gap: 32px;
  padding: 40px 8px;
  border-bottom: 1px solid var(--line);
}

.column-row:hover {
  background: var(--bg-soft);
}

.column-num {
  font-family: var(--serif);
  font-size: 22px;
  color: var(--gold);
  letter-spacing: 0.12em;
}

.column-body h3 {
  font-family: var(--serif);
  font-size: 22px;
  color: var(--paper);
  letter-spacing: 0.1em;
}

.column-body p {
  margin-top: 8px;
  font-size: 14px;
  color: var(--muted);
  max-width: 72ch;
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
  padding: 64px 56px;
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
  padding: 112px 0;
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
