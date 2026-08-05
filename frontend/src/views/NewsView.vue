<script setup>
import { ref } from 'vue'
import { media } from '../media'
import SkeletonLoader from '../components/SkeletonLoader.vue'
import { useFakeLoad } from '../composables/useFakeLoad'

const IMG = {
  li1: media('media/imges/li-meimiao-1.jpg'),
  li2: media('media/imges/li-meimiao-2.jpg'),
  axelsen: media('media/imges/an-sai-long.jpg'),
  leeZijia: media('media/imges/li-zi-jia.jpg'),
  gear1: media('media/imges/gear-1.jpg'),
  gear2: media('media/imges/gear-2.jpg'),
  product3: media('media/imges/product-3.png'),
  banner: media('media/imges/hero-banner.jpg'),
}

const categories = ['全部', '赛事', '人物', '装备', '深度']
const active = ref('全部')

const topics = ['全英公开赛', '巴黎奥运', '世界排名', '安赛龙', '李梓嘉', '球拍横评', '训练方法论', '青年球员']

const articles = [
  {
    category: '深度',
    title: '2026 赛季过半：男子单打进入群雄逐鹿时代',
    date: '2026.07.28',
    excerpt: '从安赛龙到李梓嘉，从老将坚守到新人冲击，男单格局正在被重新书写。',
    image: IMG.li1,
  },
  {
    category: '赛事',
    title: '全英公开赛前瞻：新老格局的又一次碰撞',
    date: '2026.08.02',
    excerpt: '百年全英即将开赛，签表关键对决与种子选手状态一网打尽。',
    image: IMG.axelsen,
  },
  {
    category: '人物',
    title: '安赛龙：把训练场搬回家，依旧统治男单',
    date: '2026.07.26',
    excerpt: '深入他的日常训练体系，看两届奥运冠军如何保持竞争力。',
    image: IMG.leeZijia,
  },
  {
    category: '装备',
    title: '2026 新款高端球拍横评：进攻与控制之争',
    date: '2026.07.20',
    excerpt: '三款旗舰球拍同场实测，挥重、弹性与出球质量的真实数据。',
    image: IMG.gear1,
  },
  {
    category: '装备',
    title: '羽毛球选购指南：从球速到耐打性的完整解析',
    date: '2026.07.12',
    excerpt: '76、77、78 速怎么选？鹅毛与鸭毛的差距到底在哪？',
    image: IMG.product3,
  },
  {
    category: '人物',
    title: '李美妙：泰国女单的移动与线路艺术',
    date: '2026.07.05',
    excerpt: '从青年赛到世界女单前列，她用稳定与变化证明自己的名字值得被记住。',
    image: IMG.li2,
  },
  {
    category: '深度',
    title: '数据看羽坛：2026 上半年的十个关键数字',
    date: '2026.06.30',
    excerpt: '胜率、场均耗时、多拍回合……用数据还原上半年的真实走势。',
    image: IMG.banner,
  },
]

const recommends = [
  { title: '球鞋选购的五个关键参数，大部分人都忽略了', date: '2026.07.18', image: IMG.gear2, category: '装备' },
  { title: '汤姆斯杯回顾：团体赛里的排兵布阵艺术', date: '2026.06.22', image: IMG.banner, category: '赛事' },
  { title: '训练笔记：多拍相持中的重心控制方法', date: '2026.06.15', image: IMG.axelsen, category: '深度' },
  { title: '青年军崛起：近三年闯入前二十的新面孔', date: '2026.06.08', image: IMG.li2, category: '人物' },
]

const filtered = () =>
  active.value === '全部' ? articles : articles.filter((a) => a.category === active.value)
const { loading } = useFakeLoad(650)
</script>

<template>
  <div>
    <div class="page-head">
      <div class="container">
        <p class="eyebrow">News & Reports</p>
        <h1>资讯</h1>
        <p>赛事报道、人物专访与装备测评，来自现场的深度内容。</p>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <SkeletonLoader v-if="loading" variant="page" :count="3" :cols="3" />
        <template v-else>
        <div class="featured card micro-card">
          <img :src="articles[0].image" alt="头条" />
          <div class="featured-body">
            <p class="tag">{{ articles[0].category }}</p>
            <h2>{{ articles[0].title }}</h2>
            <p class="featured-excerpt">{{ articles[0].excerpt }}</p>
            <p class="featured-date">{{ articles[0].date }}</p>
          </div>
        </div>

        <div class="filters">
          <button
            v-for="c in categories"
            :key="c"
            class="filter-btn"
            :class="{ active: active === c }"
            @click="active = c"
          >
            {{ c }}
          </button>
        </div>

        <div class="news-grid">
          <article v-for="a in filtered()" :key="a.title" class="news-card card micro-card">
            <img :src="a.image" :alt="a.title" loading="lazy" />
            <div class="news-body">
              <div class="news-meta">
                <span class="tag">{{ a.category }}</span>
                <span class="news-date">{{ a.date }}</span>
              </div>
              <h3>{{ a.title }}</h3>
              <p>{{ a.excerpt }}</p>
            </div>
          </article>
        </div>
        </template>
      </div>
    </section>

    <section class="section section-alt">
      <div class="container">
        <div class="section-head">
          <h2 class="section-title">热门话题</h2>
        </div>
        <div class="topics">
          <span v-for="t in topics" :key="t" class="topic"># {{ t }}</span>
        </div>
        <div class="topic-stats">
          <div class="topic-stat micro-card">
            <p class="ts-num">1.8w</p>
            <p>全英公开赛相关讨论</p>
          </div>
          <div class="topic-stat micro-card">
            <p class="ts-num">9.6k</p>
            <p>安赛龙专栏阅读量</p>
          </div>
          <div class="topic-stat micro-card">
            <p class="ts-num">3.2k</p>
            <p>球拍横评收藏数</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <h2 class="section-title">推荐阅读</h2>
        </div>
        <SkeletonLoader v-if="loading" variant="grid" :count="4" :cols="4" />
        <div v-else class="reco-grid">
          <article v-for="r in recommends" :key="r.title" class="reco-card micro-card">
            <img :src="r.image" :alt="r.title" loading="lazy" />
            <div class="reco-body">
              <div class="reco-meta">
                <span class="tag">{{ r.category }}</span>
                <span>{{ r.date }}</span>
              </div>
              <h3>{{ r.title }}</h3>
            </div>
          </article>
        </div>
      </div>
    </section>

    <section class="quote-band">
      <div class="container">
        <p class="quote-text">“资讯的价值，不在于追逐热点，而在于让每一篇报道都经得起时间的检验。”</p>
        <p class="quote-author">羽界编辑部</p>
      </div>
    </section>
  </div>
</template>

<style scoped>
.featured {
  display: grid;
  grid-template-columns: 1.25fr 1fr;
  margin-bottom: 64px;
  background: #ffffff;
}

.featured img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.featured-body {
  padding: 60px 56px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.featured-body h2 {
  margin-top: 18px;
  font-family: var(--serif);
  font-size: 30px;
  line-height: 1.55;
  color: var(--paper);
  letter-spacing: 0.05em;
}

.featured-excerpt {
  margin-top: 16px;
  color: var(--muted);
  font-size: 14px;
}

.featured-date {
  margin-top: 22px;
  font-size: 12px;
  letter-spacing: 0.2em;
  color: var(--gold);
}

.filters {
  display: flex;
  gap: 12px;
  margin-bottom: 44px;
}

.filter-btn {
  padding: 9px 24px;
  border: 1px solid var(--line);
  background: #ffffff;
  color: var(--muted);
  font-size: 13px;
  letter-spacing: 0.18em;
  cursor: pointer;
}

.filter-btn:hover {
  color: var(--paper);
  border-color: var(--gold);
}

.filter-btn.active {
  color: var(--paper);
  background: var(--gold);
  border-color: var(--gold);
}

.news-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 32px;
}

.news-card img {
  height: 210px;
}

.news-body {
  padding: 28px 30px 32px;
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
  font-size: 19px;
  line-height: 1.5;
  color: var(--paper);
  letter-spacing: 0.04em;
}

.news-body p:not(.news-date) {
  margin-top: 12px;
  font-size: 13px;
  color: var(--muted);
}

.topics {
  display: flex;
  flex-wrap: wrap;
  gap: 14px;
  margin-bottom: 48px;
}

.topic {
  padding: 10px 24px;
  border: 1px solid var(--line);
  background: #ffffff;
  font-size: 14px;
  letter-spacing: 0.08em;
  color: var(--text);
}

.topic:hover {
  border-color: var(--gold);
  color: var(--gold);
}

.topic-stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 28px;
}

.topic-stat {
  padding: 44px 32px;
  text-align: center;
  border: 1px solid var(--line);
  background: #ffffff;
}

.ts-num {
  font-family: var(--serif);
  font-size: 34px;
  color: var(--gold);
}

.topic-stat p:not(.ts-num) {
  margin-top: 8px;
  font-size: 13px;
  color: var(--muted);
}

.reco-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 32px;
}

.reco-card {
  border: 1px solid var(--line);
  background: #ffffff;
}

.reco-card:hover {
  border-color: var(--gold);
}

.reco-card img {
  width: 100%;
  height: 190px;
  object-fit: cover;
}

.reco-body {
  padding: 26px 28px 30px;
}

.reco-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 12px;
  color: var(--muted);
  margin-bottom: 12px;
}

.reco-body h3 {
  font-family: var(--serif);
  font-size: 16px;
  line-height: 1.55;
  color: var(--paper);
  letter-spacing: 0.04em;
}

.quote-band {
  padding: 120px 0;
  background: var(--bg-soft);
  border-top: 1px solid var(--line);
  text-align: center;
}

.quote-text {
  max-width: 760px;
  margin: 0 auto;
  font-family: var(--serif);
  font-size: 26px;
  line-height: 1.9;
  color: var(--paper);
  letter-spacing: 0.06em;
}

.quote-author {
  margin-top: 28px;
  font-size: 13px;
  letter-spacing: 0.3em;
  color: var(--gold);
}

@media (max-width: 960px) {
  .featured {
    grid-template-columns: 1fr;
  }
  .news-grid {
    grid-template-columns: 1fr 1fr;
  }
  .reco-grid {
    grid-template-columns: 1fr 1fr;
  }
}

@media (max-width: 640px) {
  .news-grid,
  .reco-grid,
  .topic-stats {
    grid-template-columns: 1fr;
  }
}
</style>
