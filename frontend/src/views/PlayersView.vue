<script setup>
import PlayerCarousel from '../components/PlayerCarousel.vue'
import { media } from '../media'

const IMG = {
  axelsen: media('media/imges/axelsen-poster.jpg'),
  leeZijia: media('media/imges/lee-zijia-poster.jpg'),
  li1: media('media/imges/li-meimiao-1.jpg'),
  li2: media('media/imges/li-meimiao-2.jpg'),
  li3: media('media/imges/li-meimiao-3.jpg'),
}

const players = [
  {
    id: 'axelsen',
    name: '安赛龙',
    en: 'Viktor Axelsen',
    country: '丹麦 · Denmark',
    birth: '1994.01.02',
    height: '194 cm',
    style: '打法全面，攻守均衡，身高臂长的绝对控制流',
    gallery: [media('media/imges/4.jfif'), media('media/imges/5.jfif'), media('media/imges/6.jfif')],
    bio: '丹麦男单领军人物，两届奥运会金牌得主。他以严谨的训练体系与极致的多拍稳定性，长期占据男单世界第一的位置，被视为这一代男单的标杆。',
    career: [
      { year: '2016', text: '作为丹麦队核心，夺得汤姆斯杯冠军，历史首次登顶' },
      { year: '2017', text: '格拉斯哥世锦赛男单夺冠，正式跻身顶尖行列' },
      { year: '2021', text: '东京奥运会男单决赛夺冠，收获首枚奥运金牌' },
      { year: '2022', text: '东京世锦赛成功卫冕，同年登顶男单世界第一' },
      { year: '2024', text: '巴黎奥运会成功卫冕，实现男单奥运两连冠' },
    ],
    awards: [
      { year: '2024', event: '巴黎奥运会', result: '男单金牌' },
      { year: '2022', event: '世界羽毛球锦标赛', result: '男单冠军' },
      { year: '2022', event: '全英公开赛', result: '男单冠军' },
      { year: '2021', event: '东京奥运会', result: '男单金牌' },
      { year: '2017', event: '世界羽毛球锦标赛', result: '男单冠军' },
      { year: '2016', event: '汤姆斯杯', result: '团体冠军' },
    ],
  },
  {
    id: 'lee-zijia',
    name: '李梓嘉',
    en: 'Lee Zii Jia',
    country: '马来西亚 · Malaysia',
    birth: '1998.03.29',
    height: '186 cm',
    style: '强力进攻型打法，杀球爆发力出众，观赏性极强',
    gallery: [media('media/imges/product-1.jpeg'), media('media/imges/product-2.jpeg')],
    bio: '马来西亚男单一哥，凭借极具冲击力的进攻风格在国际赛场屡创佳绩。他继承了东南亚男单的传统特色，以重杀和快速连贯闻名。',
    career: [
      { year: '2021', text: '全英公开赛男单夺冠，成为马来西亚新一任全英冠军' },
      { year: '2022', text: '亚洲羽毛球锦标赛男单夺金，首获洲际大赛冠军' },
      { year: '2022', text: '泰国公开赛男单登顶，赛季状态持续火热' },
      { year: '2023', text: '再次夺得泰国公开赛冠军，巩固顶级男单地位' },
      { year: '2024', text: '巴黎奥运会闯入男单四强，刷新个人奥运最佳战绩' },
    ],
    awards: [
      { year: '2024', event: '巴黎奥运会', result: '男单第四名' },
      { year: '2023', event: '泰国公开赛', result: '男单冠军' },
      { year: '2022', event: '亚洲羽毛球锦标赛', result: '男单金牌' },
      { year: '2022', event: '泰国公开赛', result: '男单冠军' },
      { year: '2021', event: '全英公开赛', result: '男单冠军' },
      { year: '2021', event: '苏迪曼杯', result: '团体季军' },
    ],
  },
  {
    id: 'li-meimiao',
    name: '李美秒',
    en: 'Li Meimiao',
    country: '中国 · China',
    birth: '2005.08.14',
    height: '172 cm',
    style: '技术细腻，网前手感出色，以节奏变化制胜',
    gallery: [IMG.li1, IMG.li2, media('media/imges/8.jpg')],
    bio: '中国女单新生代代表人物。她从青年赛一路走来，以冷静的头脑和出色的网前技术受到关注，被视为中国女单未来的希望之一。',
    career: [
      { year: '2023', text: '全国青年羽毛球锦标赛女单夺冠，崭露头角' },
      { year: '2024', text: '亚洲青年羽毛球锦标赛女单金牌' },
      { year: '2025', text: '首次入选国家一队，开启成年组征战' },
      { year: '2025', text: '全国羽毛球锦标赛女单亚军' },
      { year: '2026', text: '世界羽联超级 500 赛闯入四强，创造个人最佳' },
    ],
    awards: [
      { year: '2026', event: '世界羽联超级 500 赛', result: '女单四强' },
      { year: '2025', event: '全国羽毛球锦标赛', result: '女单亚军' },
      { year: '2024', event: '亚洲青年羽毛球锦标赛', result: '女单金牌' },
      { year: '2023', event: '全国青年羽毛球锦标赛', result: '女单冠军' },
    ],
  },
]

const rankings = [
  { rank: '1', name: '安赛龙', country: '丹麦', points: '102,540' },
  { rank: '2', name: '李梓嘉', country: '马来西亚', points: '96,280' },
  { rank: '3', name: '石宇奇', country: '中国', points: '91,730' },
  { rank: '4', name: '昆拉武特', country: '泰国', points: '87,460' },
  { rank: '5', name: '乔纳坦', country: '印尼', points: '83,910' },
]

const quotes = [
  { text: '每一分都是独立的，忘记上一分，专注下一分。', author: '安赛龙' },
  { text: '进攻不是莽撞，而是把机会压缩到对手无法反应。', author: '李梓嘉' },
  { text: '我还年轻，我的名字值得被记住。', author: '李美秒' },
]
</script>

<template>
  <div>
    <div class="page-head">
      <div class="container">
        <p class="eyebrow">Players & Legends</p>
        <h1>球员</h1>
        <p>球员档案、荣誉生涯与获奖记录，读懂每一位顶尖选手。</p>
      </div>
    </div>

    <div v-for="(p, i) in players" :key="p.id">
      <section class="section" :class="{ 'section-alt': i % 2 === 1 }">
        <div class="container">
          <div class="player-head">
            <PlayerCarousel :images="p.gallery" :alt="p.name" />
            <div class="player-profile">
              <p class="eyebrow">{{ p.country }}</p>
              <h2>{{ p.name }}<span class="player-en">{{ p.en }}</span></h2>
              <ul class="player-facts">
                <li><span>出生日期</span>{{ p.birth }}</li>
                <li><span>身高</span>{{ p.height }}</li>
                <li><span>技术特点</span>{{ p.style }}</li>
              </ul>
              <p class="player-bio">{{ p.bio }}</p>
            </div>
          </div>

          <div class="player-detail">
            <div class="detail-col">
              <h3>荣誉生涯</h3>
              <div class="hairline"></div>
              <ol class="timeline">
                <li v-for="c in p.career" :key="c.year" class="timeline-item">
                  <span class="tl-year">{{ c.year }}</span>
                  <p>{{ c.text }}</p>
                </li>
              </ol>
            </div>
            <div class="detail-col">
              <h3>获奖情况</h3>
              <div class="hairline"></div>
              <div class="table-wrap">
                <table>
                  <thead>
                    <tr>
                      <th>年份</th>
                      <th>赛事</th>
                      <th>成绩</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="a in p.awards" :key="a.event + a.year">
                      <td>{{ a.year }}</td>
                      <td>{{ a.event }}</td>
                      <td>{{ a.result }}</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <h2 class="section-title">男单世界排名 · 前五</h2>
        </div>
        <div class="table-wrap">
          <table>
            <thead>
              <tr>
                <th>排名</th>
                <th>球员</th>
                <th>协会</th>
                <th>积分</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="r in rankings" :key="r.rank">
                <td>{{ r.rank }}</td>
                <td>{{ r.name }}</td>
                <td>{{ r.country }}</td>
                <td>{{ r.points }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="container">
        <div class="section-head">
          <h2 class="section-title">球员语录</h2>
        </div>
        <div class="quotes-grid">
          <div v-for="q in quotes" :key="q.author" class="quote-card">
            <p class="quote-text">“{{ q.text }}”</p>
            <p class="quote-author">—— {{ q.author }}</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <h2 class="section-title">更多球员</h2>
        </div>
        <div class="more-grid">
          <div class="more-card card">
            <img :src="IMG.li1" alt="李美秒" />
            <p>李美秒 · 中国</p>
          </div>
          <div class="more-card card">
            <img :src="IMG.axelsen" alt="安赛龙" />
            <p>安赛龙 · 丹麦</p>
          </div>
          <div class="more-card card">
            <img :src="IMG.leeZijia" alt="李梓嘉" />
            <p>李梓嘉 · 马来西亚</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.section-alt {
  background: var(--bg-soft);
  border-top: 1px solid var(--line);
  border-bottom: 1px solid var(--line);
}

.player-head {
  display: grid;
  grid-template-columns: 420px 1fr;
  gap: 56px;
  align-items: center;
}

.player-profile h2 {
  font-family: var(--serif);
  font-size: 40px;
  color: var(--paper);
  letter-spacing: 0.12em;
}

.player-en {
  display: block;
  margin-top: 6px;
  font-family: var(--sans);
  font-size: 14px;
  letter-spacing: 0.3em;
  color: var(--muted);
  font-weight: 400;
}

.player-facts {
  list-style: none;
  margin-top: 30px;
  border-top: 1px solid var(--line);
}

.player-facts li {
  display: flex;
  gap: 24px;
  padding: 14px 0;
  border-bottom: 1px solid var(--line);
  font-size: 14px;
  color: var(--text);
}

.player-facts span {
  width: 90px;
  color: var(--gold);
  letter-spacing: 0.18em;
  font-size: 12px;
}

.player-bio {
  margin-top: 26px;
  font-size: 14px;
  color: var(--muted);
}

.player-detail {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 56px;
  margin-top: 64px;
  padding-top: 56px;
  border-top: 1px solid var(--line);
}

.detail-col h3 {
  font-family: var(--serif);
  font-size: 22px;
  color: var(--paper);
  letter-spacing: 0.14em;
}

.timeline {
  list-style: none;
  position: relative;
  padding-left: 30px;
}

.timeline::before {
  content: '';
  position: absolute;
  left: 7px;
  top: 6px;
  bottom: 6px;
  width: 1px;
  background: var(--line);
}

.timeline-item {
  position: relative;
  padding: 0 0 30px;
}

.timeline-item::before {
  content: '';
  position: absolute;
  left: -30px;
  top: 7px;
  width: 7px;
  height: 7px;
  background: var(--gold);
}

.timeline-item:last-child {
  padding-bottom: 0;
}

.tl-year {
  font-family: var(--serif);
  font-size: 18px;
  color: var(--gold);
  letter-spacing: 0.1em;
}

.timeline-item p {
  margin-top: 6px;
  font-size: 14px;
  color: var(--text);
}

.quotes-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 26px;
}

.quote-card {
  padding: 40px 34px;
  border: 1px solid var(--line);
  background: #ffffff;
}

.quote-text {
  font-family: var(--serif);
  font-size: 19px;
  line-height: 1.9;
  color: var(--paper);
  letter-spacing: 0.04em;
}

.quote-author {
  margin-top: 22px;
  font-size: 13px;
  letter-spacing: 0.24em;
  color: var(--gold);
}

.more-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 26px;
}

.more-card img {
  height: 280px;
}

.more-card p {
  padding: 18px 22px;
  font-family: var(--serif);
  font-size: 17px;
  color: var(--paper);
  letter-spacing: 0.1em;
}

@media (max-width: 960px) {
  .player-head {
    grid-template-columns: 1fr;
  }
  .player-detail {
    grid-template-columns: 1fr;
  }
  .quotes-grid,
  .more-grid {
    grid-template-columns: 1fr;
  }
}
</style>
