<script setup>
import { media } from '../media'
import SkeletonLoader from '../components/SkeletonLoader.vue'
import { useFakeLoad } from '../composables/useFakeLoad'

const VID = {
  promo1: media('media/video/promo-1-web.mp4'),
  promo2: media('media/video/promo-2-web.mp4'),
  axelsen: media('media/video/an-sai-long-web.mp4'),
  leeZijia: media('media/video/li-zi-jia-web.mp4'),
}

const IMG = {
  banner: media('media/imges/hero-banner.jpg'),
  gear1: media('media/imges/gear-1.jpg'),
  gear2: media('media/imges/gear-2.jpg'),
  product1: media('media/imges/product-1.jpeg'),
  product2: media('media/imges/product-2.jpeg'),
  product3: media('media/imges/product-3.png'),
}

const products = [
  { name: '旗舰进攻型球拍', desc: '高刚性拍框，重杀出球干脆', image: IMG.product1, tag: '球拍' },
  { name: '专业竞技球鞋', desc: '轻量支撑，急停启动更稳', image: IMG.product2, tag: '球鞋' },
  { name: '比赛级羽毛球', desc: '精选鹅毛，飞行轨迹稳定', image: IMG.product3, tag: '羽球' },
  { name: '高弹拍线', desc: '控制与弹性兼顾的经典搭配', image: IMG.gear1, tag: '配件' },
  { name: '多功能球包', desc: '大容量分区收纳，通勤比赛两用', image: IMG.gear2, tag: '配件' },
]

const videos = [
  { src: VID.promo1, title: '2026 春季系列宣传片', poster: IMG.banner },
  { src: VID.promo2, title: '实战测试：高弹拍线专项', poster: IMG.gear2 },
  { src: VID.axelsen, title: '安赛龙高光：身高臂展与控制流', poster: media('media/imges/an-sai-long.jpg') },
  { src: VID.leeZijia, title: '李梓嘉高光：暴力进攻美学', poster: media('media/imges/li-zi-jia.jpg') },
]

const rankings = [
  { rank: '1', item: '旗舰进攻型球拍 A 款', score: '9.2', note: '出球干脆，容错率高' },
  { rank: '2', item: '均衡控制型球拍 B 款', score: '8.8', note: '多拍相持手感细腻' },
  { rank: '3', item: '轻量速度型球拍 C 款', score: '8.5', note: '挥速快，连贯性强' },
]

const care = [
  { title: '球拍保养', desc: '避免高温暴晒与潮湿存放，拍线松弛或起毛时及时更换，穿线磅数按打法调整。' },
  { title: '球鞋保养', desc: '每次使用后通风干燥，避免机洗；鞋底磨损到防滑纹路变浅时应及时更换。' },
  { title: '羽毛球存放', desc: '保持球桶密封并置于阴凉处，比赛用球提前一晚加湿回潮，飞行会更稳定。' },
  { title: '拍线张力', desc: '建议每 3–6 个月或断线后重穿，磅数变化以 1–2 磅为梯度，避免突然大幅调整。' },
]
const { loading } = useFakeLoad(700)
</script>

<template>
  <div>
    <section class="gear-hero">
      <img :src="IMG.banner" alt="装备" class="bg-image" loading="eager" fetchpriority="high" />
      <div class="gear-mask"></div>
      <div class="container gear-hero-content">
        <p class="eyebrow">Gear & Equipment</p>
        <h1>装备</h1>
        <p>从球场实测到产品解析，用真实视频与数据为你的选择提供参考。</p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <h2 class="section-title">视频实测</h2>
        </div>
        <SkeletonLoader v-if="loading" variant="grid" :count="2" :cols="2" :img-height="340" />
        <div v-else class="video-grid">
          <figure v-for="v in videos" :key="v.title" class="video-card micro-card">
            <video :src="v.src" :poster="v.poster" controls preload="metadata"></video>
            <figcaption>
              <h3>{{ v.title }}</h3>
              <p>实拍素材 · 来自羽界装备实验室</p>
            </figcaption>
          </figure>
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="container">
        <div class="section-head">
          <h2 class="section-title">产品系列</h2>
        </div>
        <SkeletonLoader v-if="loading" variant="grid" :count="5" :cols="3" :img-height="300" />
        <div v-else class="product-grid">
          <div v-for="p in products" :key="p.name" class="product-card card">
            <img :src="p.image" :alt="p.name" loading="lazy" />
            <div class="product-body">
              <p class="tag">{{ p.tag }}</p>
              <h3>{{ p.name }}</h3>
              <p>{{ p.desc }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <h2 class="section-title">本月评测榜单</h2>
        </div>
        <div class="table-wrap">
          <table>
            <thead>
              <tr>
                <th>排名</th>
                <th>产品</th>
                <th>综合评分</th>
                <th>评测要点</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="r in rankings" :key="r.rank">
                <td>{{ r.rank }}</td>
                <td>{{ r.item }}</td>
                <td>{{ r.score }}</td>
                <td>{{ r.note }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="container">
        <div class="section-head">
          <h2 class="section-title">保养指南</h2>
        </div>
        <div class="care-grid">
          <div v-for="c in care" :key="c.title" class="care card">
            <h3>{{ c.title }}</h3>
            <p>{{ c.desc }}</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <h2 class="section-title">选购指南</h2>
        </div>
        <div class="guide-grid">
          <div class="guide card">
            <h3>按打法选拍</h3>
            <p>进攻型选手优先考虑拍头重、挥速快的型号；控制型选手可关注拍框刚性中等、弹性更细腻的产品。</p>
          </div>
          <div class="guide card">
            <h3>按场地选鞋</h3>
            <p>木地板场地需要更强的缓震，塑胶场地更看重抓地与侧向支撑，试穿时注意前掌宽度。</p>
          </div>
          <div class="guide card">
            <h3>按季节选球</h3>
            <p>冬季低温建议选用 77 速，夏季高温选用 76 速；比赛优先选鹅毛球，训练可搭配鸭毛球降低成本。</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.gear-hero {
  position: relative;
  min-height: 540px;
  display: flex;
  align-items: center;
  overflow: hidden;
  border-bottom: 1px solid var(--line);
}

.bg-image {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.gear-mask {
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg, rgba(255, 255, 255, 0.92) 0%, rgba(255, 255, 255, 0.62) 100%);
}

.gear-hero-content {
  position: relative;
}

.gear-hero-content h1 {
  font-family: var(--serif);
  font-size: 72px;
  font-weight: 600;
  color: var(--paper);
  letter-spacing: 0.3em;
}

.gear-hero-content p:not(.eyebrow) {
  max-width: 520px;
  color: var(--text);
  font-size: 16px;
}

.section-alt {
  background: var(--bg-soft);
  border-top: 1px solid var(--line);
  border-bottom: 1px solid var(--line);
}

.video-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 32px;
}

.video-card {
  border: 1px solid var(--line);
  background: #ffffff;
}

.video-card:hover {
  border-color: var(--gold);
}

.video-card video {
  width: 100%;
  height: 340px;
  object-fit: cover;
  background: #000;
}

.video-card figcaption {
  padding: 24px 28px 28px;
}

.video-card h3 {
  font-family: var(--serif);
  font-size: 19px;
  color: var(--paper);
  letter-spacing: 0.06em;
}

.video-card figcaption p {
  margin-top: 6px;
  font-size: 12px;
  color: var(--muted);
}

.product-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 32px;
}

.product-card img {
  height: 300px;
}

.product-body {
  padding: 28px 30px 32px;
}

.product-body h3 {
  margin-top: 14px;
  font-family: var(--serif);
  font-size: 19px;
  color: var(--paper);
  letter-spacing: 0.06em;
}

.product-body p:not(.tag) {
  margin-top: 10px;
  font-size: 13px;
  color: var(--muted);
}

.care-grid,
.guide-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 28px;
}

.care,
.guide {
  padding: 40px 34px;
  background: #ffffff;
}

.care h3,
.guide h3 {
  font-family: var(--serif);
  font-size: 19px;
  color: var(--paper);
  letter-spacing: 0.1em;
  margin-bottom: 14px;
}

.care p,
.guide p {
  font-size: 13px;
  color: var(--muted);
}

@media (max-width: 960px) {
  .video-grid {
    grid-template-columns: 1fr;
  }
  .product-grid,
  .care-grid,
  .guide-grid {
    grid-template-columns: 1fr 1fr;
  }
}

@media (max-width: 640px) {
  .product-grid,
  .care-grid,
  .guide-grid {
    grid-template-columns: 1fr;
  }
}
</style>
