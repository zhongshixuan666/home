<script setup>
import PlayerCarousel from '../components/PlayerCarousel.vue'
import SkeletonLoader from '../components/SkeletonLoader.vue'
import { useFakeLoad } from '../composables/useFakeLoad'
import { media } from '../media'

const IMG = {
  axelsen: media('images/an-sai-long.jpg'),
  leeZijia: media('images/li-zi-jia.jpg'),
  anXiYin: media('images/an-xi-yin.jpg'),
  linDan: media('images/lin-dan.jpg'),
  liuGuoLun: media('images/liu-guo-lun.jpg'),
  shiYuQi: media('images/shi-yu-qi.jpg'),
  li1: media('images/li-meimiao-1.jpg'),
  li2: media('images/li-meimiao-2.jpg'),
}

const VIDEOS = {
  axelsen: media('videos/an-sai-long-web.mp4'),
  leeZijia: media('videos/li-zi-jia-web.mp4'),
  anXiYin: media('videos/an-xi-yin-web.mp4'),
  linDan: media('videos/lin-dan-web.mp4'),
  liuGuoLun: media('videos/liu-guo-lun-web.mp4'),
  shiYuQi: media('videos/shi-yu-qi-web.mp4'),
}

const players = [
  {
    id: 'axelsen',
    name: '安赛龙',
    en: 'Viktor Axelsen',
    country: '丹麦 · Denmark',
    birth: '1994.01.02',
    height: '194 cm',
    status: '已退役（2026.04）',
    style: '打法全面，攻守均衡，身高臂长的绝对控制流',
    gallery: [IMG.axelsen, media('images/4.jfif'), media('images/5.jfif')],
    video: VIDEOS.axelsen,
    bio: '丹麦传奇男单，两届奥运会金牌得主。2026年4月，他因反复腰伤宣布从职业赛场退役。职业生涯中，他以严谨的训练体系、极致的多拍稳定性和出色的身高臂展，成为这一代男单的重要标杆。',
    career: [
      { year: '2016', text: '作为丹麦队核心，夺得汤姆斯杯冠军，历史首次登顶' },
      { year: '2017', text: '格拉斯哥世锦赛男单夺冠，正式跻身顶尖行列' },
      { year: '2021', text: '东京奥运会男单决赛夺冠，收获首枚奥运金牌' },
      { year: '2022', text: '东京世锦赛成功卫冕，同年登顶男单世界第一' },
      { year: '2024', text: '巴黎奥运会成功卫冕，实现男单奥运两连冠' },
      { year: '2026', text: '因反复腰伤宣布从职业赛场退役，结束两届奥运冠军的职业生涯' },
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
    id: 'shi-yuqi',
    name: '石宇奇',
    en: 'Shi Yu Qi',
    country: '中国 · China',
    birth: '1996.02.28',
    height: '183 cm',
    status: '男单世界第一',
    style: '快速连贯的进攻体系，劈杀犀利，网前变化丰富，擅长节奏控制',
    gallery: [IMG.shiYuQi],
    video: VIDEOS.shiYuQi,
    bio: '中国男单领军人物，2025年巴黎世锦赛男单冠军、2026年亚锦赛男单冠军。近期重返世界第一并累计达成百周世界第一，以稳定的多拍质量和关键分能力成为国羽男单的新旗帜。',
    career: [
      { year: '2018', text: '全英公开赛男单夺冠，同年加冕世界羽联巡回赛总决赛冠军' },
      { year: '2025', text: '巴黎世锦赛男单夺冠，为中国男单时隔10年再夺世锦赛男单冠军' },
      { year: '2026', text: '宁波亚锦赛男单决赛击败印度新秀谢蒂，生涯首夺亚锦赛冠军' },
      { year: '2026', text: '重返男单世界第一，并达成累计百周世界第一的里程碑' },
    ],
    awards: [
      { year: '2026', event: '亚洲羽毛球锦标赛', result: '男单冠军' },
      { year: '2025', event: '世界羽毛球锦标赛', result: '男单冠军' },
      { year: '2018', event: '全英公开赛', result: '男单冠军' },
      { year: '2018', event: '世界羽联世界巡回赛总决赛', result: '男单冠军' },
    ],
  },
  {
    id: 'an-se-young',
    name: '安洗莹',
    en: 'An Se Young',
    country: '韩国 · Korea',
    birth: '2002.02.05',
    height: '170 cm',
    status: '女单世界第一',
    style: '防守稳固、步伐覆盖大、多拍耐心，网前手感细腻，关键分极其稳定',
    gallery: [IMG.anXiYin],
    video: VIDEOS.anXiYin,
    bio: '韩国女单领军人物，2023年世锦赛冠军、2024年巴黎奥运会金牌得主。2026赛季胜率高达97.4%，持续稳居世界第一，被视为深圳大师赛女单冠军最大热门。',
    career: [
      { year: '2018', text: '以初中生身份入选韩国国家队，创下韩国羽毛球选拔历史' },
      { year: '2023', text: '夺得世界羽毛球锦标赛女单冠军，正式开启女单统治期' },
      { year: '2024', text: '巴黎奥运会女单决赛夺冠，收获个人首枚奥运金牌' },
      { year: '2026', text: '保持世界第一与高胜率，领衔参加新德里世锦赛与深圳大师赛' },
    ],
    awards: [
      { year: '2024', event: '巴黎奥运会', result: '女单金牌' },
      { year: '2023', event: '世界羽毛球锦标赛', result: '女单冠军' },
      { year: '2025', event: '世界羽联年度评选', result: '年度最佳女运动员' },
    ],
  },
  {
    id: 'lee-zijia',
    name: '李梓嘉',
    en: 'Lee Zii Jia',
    country: '马来西亚 · Malaysia',
    birth: '1998.03.29',
    height: '186 cm',
    status: '巴黎奥运铜牌',
    style: '强力进攻型打法，杀球爆发力出众，观赏性极强',
    gallery: [IMG.leeZijia, media('images/product-1.jpeg'), media('images/product-2.jpeg')],
    video: VIDEOS.leeZijia,
    bio: '马来西亚男单代表，以极具冲击力的重杀和快速连贯闻名。2024年巴黎奥运会夺得男单铜牌，成为马来西亚新一代表现最稳定的男单旗帜之一。',
    career: [
      { year: '2021', text: '全英公开赛男单夺冠，成为马来西亚新一任全英冠军' },
      { year: '2022', text: '亚洲羽毛球锦标赛男单夺金，首获洲际大赛冠军' },
      { year: '2022', text: '泰国公开赛男单登顶，赛季状态持续火热' },
      { year: '2023', text: '再次夺得泰国公开赛冠军，巩固顶级男单地位' },
      { year: '2024', text: '巴黎奥运会男单铜牌赛三局逆转拉克什亚，收获生涯首枚奥运奖牌' },
    ],
    awards: [
      { year: '2024', event: '巴黎奥运会', result: '男单铜牌' },
      { year: '2023', event: '泰国公开赛', result: '男单冠军' },
      { year: '2022', event: '亚洲羽毛球锦标赛', result: '男单金牌' },
      { year: '2022', event: '泰国公开赛', result: '男单冠军' },
      { year: '2021', event: '全英公开赛', result: '男单冠军' },
      { year: '2021', event: '苏迪曼杯', result: '团体季军' },
    ],
  },
  {
    id: 'lin-dan',
    name: '林丹',
    en: 'Lin Dan',
    country: '中国 · China',
    birth: '1983.10.14',
    height: '178 cm',
    status: '2020年退役',
    style: '左手持拍，拉吊突击，鱼跃救球与关键分大心脏闻名',
    gallery: [IMG.linDan],
    video: VIDEOS.linDan,
    bio: '“超级丹”，中国羽毛球男单传奇。他集奥运冠军、世锦赛冠军、世界杯冠军、亚运会冠军、亚锦赛冠军与全英赛冠军于一身，以2008、2012两枚奥运金牌和五届世锦赛冠军成为羽毛球历史上的标志性人物。',
    career: [
      { year: '2008', text: '北京奥运会男单决赛夺冠，首次站上奥运最高领奖台' },
      { year: '2012', text: '伦敦奥运会男单决赛击败李宗伟，实现奥运两连冠' },
      { year: '2013', text: '广州世锦赛第五次夺得男单冠军，延续世锦赛统治' },
      { year: '2020', text: '正式宣布退役，结束国家队生涯与职业赛场征程' },
    ],
    awards: [
      { year: '2013', event: '世界羽毛球锦标赛', result: '男单冠军' },
      { year: '2012', event: '伦敦奥运会', result: '男单金牌' },
      { year: '2011', event: '世界羽毛球锦标赛', result: '男单冠军' },
      { year: '2009', event: '世界羽毛球锦标赛', result: '男单冠军' },
      { year: '2008', event: '北京奥运会', result: '男单金牌' },
      { year: '2007', event: '世界羽毛球锦标赛', result: '男单冠军' },
    ],
  },
  {
    id: 'li-meimiao',
    name: '李美妙',
    en: 'Pornpawee Chochuwong',
    country: '泰国 · Thailand',
    birth: '1998.01.22',
    height: '170 cm',
    status: '世界排名第8',
    style: '攻守兼备，脚步移动快，反手线路变化丰富，网前抢网积极',
    gallery: [IMG.li2, IMG.li1],
    bio: '泰国女单名将，本名蓬帕威·磋楚翁。她在学校学习中文后为自己取名“李美妙”，以扎实的移动和线路变化常年稳定在世界女单前列，2026年澳大利亚公开赛闯入女单决赛。',
    career: [
      { year: '2015', text: '亚洲青年羽毛球锦标赛女单亚军，进入国际视野' },
      { year: '2016', text: '世界青年羽毛球锦标赛女单亚军' },
      { year: '2020', text: '西班牙大师赛女单决赛爆冷击败马林，夺得冠军' },
      { year: '2026', text: '澳大利亚公开赛闯入女单决赛，世界排名升至第8位' },
    ],
    awards: [
      { year: '2026', event: '澳大利亚公开赛', result: '女单亚军' },
      { year: '2020', event: '西班牙大师赛', result: '女单冠军' },
      { year: '2016', event: '世界青年羽毛球锦标赛', result: '女单亚军' },
      { year: '2015', event: '亚洲青年羽毛球锦标赛', result: '女单亚军' },
    ],
  },
  {
    id: 'liu-guo-lun',
    name: '刘国伦',
    en: 'Daren Liew',
    country: '马来西亚 · Malaysia',
    birth: '1987.08.06',
    height: '178 cm',
    status: '自由人 · 世锦赛铜牌',
    style: '扎实的控制型打法，防守韧性出色，擅长以耐心拖入多拍',
    gallery: [IMG.liuGuoLun],
    video: VIDEOS.liuGuoLun,
    bio: '马来西亚男单老将，以自由人身份长期坚持征战国际赛场。2018年南京世锦赛带伤闯入四强，最终与谌龙并列获得男单铜牌，成为那届世锦赛最励志的球员之一。',
    career: [
      { year: '2018', text: '南京世锦赛1/4决赛带伤三局险胜常山干太，闯入男单四强' },
      { year: '2018', text: '半决赛不敌桃田贤斗，获得男单铜牌，创个人世锦赛最佳战绩' },
      { year: '2018', text: '以亚运会参赛名额回报大马羽总，继续以自由人身份参赛' },
    ],
    awards: [
      { year: '2018', event: '世界羽毛球锦标赛', result: '男单铜牌' },
    ],
  },
]

const rankings = [
  { rank: '1', name: '石宇奇', country: '中国', points: '94,655' },
  { rank: '2', name: '昆拉武特', country: '泰国', points: '91,215' },
  { rank: '3', name: '乔纳坦', country: '印尼', points: '89,231' },
  { rank: '4', name: '安东森', country: '丹麦', points: '87,705' },
  { rank: '5', name: '小波波夫', country: '法国', points: '87,002' },
]

const quotes = [
  { text: '每一分都是独立的，忘记上一分，专注下一分。', author: '安赛龙' },
  { text: '进攻不是莽撞，而是把机会压缩到对手无法反应。', author: '李梓嘉' },
  { text: '多拍不会说谎，稳定才是女单最深的护城河。', author: '李美妙' },
]
const { loading } = useFakeLoad(700)
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
            <SkeletonLoader v-if="loading" variant="carousel" />
            <template v-else>
              <PlayerCarousel :images="p.gallery" :alt="p.name" />
              <div class="player-profile">
              <h2>{{ p.name }}<span class="player-en">{{ p.en }}</span></h2>
              <ul class="player-facts">
                <li><span>协会</span>{{ p.country }}</li>
                <li><span>出生日期</span>{{ p.birth }}</li>
                <li><span>身高</span>{{ p.height }}</li>
                <li><span>当前</span>{{ p.status }}</li>
                <li><span>技术特点</span>{{ p.style }}</li>
              </ul>
              <p class="player-bio">{{ p.bio }}</p>
              </div>
            </template>
          </div>

          <div v-if="!loading" class="player-detail">
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

          <div v-if="!loading && p.video" class="player-video">
            <div class="video-head">
              <h3>高光视频</h3>
              <span>{{ p.name }} · 赛场片段</span>
            </div>
            <video :src="p.video" :poster="p.gallery[0]" controls preload="none" playsinline></video>
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
          <div v-for="q in quotes" :key="q.author" class="quote-card micro-card">
            <p class="quote-text">“{{ q.text }}”</p>
            <p class="quote-author">{{ q.author }}</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <h2 class="section-title">更多球员</h2>
        </div>
        <SkeletonLoader v-if="loading" variant="grid" :count="6" :cols="3" :img-height="280" />
        <div v-else class="more-grid">
          <div v-for="p in players" :key="p.id" class="more-card card micro-card">
            <img :src="p.gallery[0]" :alt="p.name" loading="lazy" />
            <p>{{ p.name }} · {{ p.country.split(' · ')[0] }}</p>
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
  gap: 64px;
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
  gap: 64px;
  margin-top: 72px;
  padding-top: 64px;
  border-top: 1px solid var(--line);
}

.player-video {
  margin-top: 64px;
  padding-top: 64px;
  border-top: 1px solid var(--line);
}

.video-head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 24px;
  margin-bottom: 24px;
}

.video-head h3 {
  font-family: var(--serif);
  font-size: 22px;
  color: var(--paper);
  letter-spacing: 0.14em;
}

.video-head span {
  font-size: 12px;
  letter-spacing: 0.22em;
  color: var(--gold);
}

.player-video video {
  width: 100%;
  aspect-ratio: 16 / 9;
  background: #111111;
  object-fit: cover;
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
  gap: 32px;
}

.quote-card {
  padding: 48px 40px;
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
  gap: 32px;
}

.more-card img {
  height: 280px;
}

.more-card p {
  padding: 22px 26px;
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
  .video-head {
    flex-direction: column;
    align-items: flex-start;
    gap: 8px;
  }
  .quotes-grid,
  .more-grid {
    grid-template-columns: 1fr;
  }
}
</style>
