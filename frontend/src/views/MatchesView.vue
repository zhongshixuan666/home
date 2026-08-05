<script setup>
import SkeletonLoader from '../components/SkeletonLoader.vue'
import { useFakeLoad } from '../composables/useFakeLoad'
const upcoming = [
  { date: '08.04', time: '至 08.09', event: '韩国羽毛球大师赛', stage: '超级300 · 正赛', venue: '韩国 · 牙山', watch: '正在进行' },
  { date: '08.17', time: '至 08.23', event: '世界羽毛球锦标赛', stage: '64强至决赛', venue: '印度 · 新德里', watch: '签表已出炉' },
  { date: '08.29', time: '至 08.30', event: '全国羽毛球运动水平等级赛', stage: '浙江分站赛', venue: '中国 · 浙江', watch: '总决赛10月举行' },
  { date: '09.01', time: '至 09.06', event: '李宁·中国羽毛球大师赛', stage: '超级750 · 正赛', venue: '中国 · 深圳', watch: '石宇奇、安洗莹领衔' },
  { date: '09.06', time: '至 09.13', event: '全国羽毛球单项锦标赛', stage: '单项赛', venue: '中国 · 合肥', watch: '全国单项争冠' },
  { date: '10.05', time: '至 10.06', event: '全国羽毛球运动水平等级赛', stage: '总决赛', venue: '中国', watch: '年度收官' },
]

const results = [
  { date: '2026.07.26', event: '中国公开赛 · 男单决赛', playerA: '周天成', playerB: '大波波夫', score: '21:15 7:21 21:13', result: '周天成胜' },
  { date: '2026.07.26', event: '中国公开赛 · 女单决赛', playerA: '山口茜', playerB: '陈雨菲', score: '21:18 21:16', result: '山口茜胜' },
  { date: '2026.07.26', event: '中国公开赛 · 男双决赛', playerA: '阿尔菲安/菲克里', playerB: '金元昊/徐承宰', score: '16:21 21:19 21:19', result: '阿尔菲安/菲克里胜' },
  { date: '2026.07.26', event: '中国公开赛 · 女双决赛', playerA: '刘圣书/谭宁', playerB: '福岛由纪/松本麻佑', score: '21:14 21:19', result: '刘圣书/谭宁胜' },
  { date: '2026.07.26', event: '中国公开赛 · 混双决赛', playerA: '郭新娃/陈芳卉', playerB: '冯彦哲/黄东萍', score: '25:23 20:22 21:15', result: '郭新娃/陈芳卉胜' },
  { date: '2026.06.14', event: '澳大利亚公开赛 · 女单决赛', playerA: '山口茜', playerB: '李美妙', score: '22:20 21:18', result: '山口茜胜' },
]

const champions = [
  { year: '2026', event: '中国羽毛球公开赛', champion: '周天成' },
  { year: '2026', event: '亚洲羽毛球锦标赛', champion: '石宇奇' },
  { year: '2026', event: '澳大利亚羽毛球公开赛', champion: '山口茜' },
  { year: '2025', event: '世界羽毛球锦标赛', champion: '石宇奇' },
  { year: '2024', event: '巴黎奥运会', champion: '安赛龙 / 安洗莹' },
  { year: '2023', event: '世界羽毛球锦标赛', champion: '安洗莹' },
]

const rules = [
  { title: '赛制', desc: '国际大赛单打采用 21 分制三局两胜，每局先到 21 分且净胜 2 分者获胜，30 分封顶。' },
  { title: '积分体系', desc: '世界羽联巡回赛按超级 100–1000 与总决赛等级累计积分，奥运与世锦赛积分权重最高。' },
  { title: '签表规则', desc: '种子选手按世界排名分配至各半区，同协会选手在早轮次原则上不相遇。' },
  { title: '观赛指南', desc: '欧洲赛事与北京时差 6–7 小时，美洲 12–13 小时，本页赛程均以北京时间标注。' },
]
const { loading } = useFakeLoad(600)
</script>

<template>
  <div>
    <div class="page-head">
      <div class="container">
        <p class="eyebrow">Matches & Results</p>
        <h1>比赛</h1>
        <p>赛程预告、即时比分与赛后复盘，一站式掌握羽坛动态。</p>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <h2 class="section-title">赛程预告</h2>
        </div>
        <SkeletonLoader v-if="loading" variant="list" :count="6" />
        <div v-else class="schedule">
          <div v-for="m in upcoming" :key="m.event" class="schedule-row">
            <div class="sch-date">
              <p>{{ m.date }}</p>
              <span>{{ m.time }}</span>
            </div>
            <div class="sch-main">
              <h3>{{ m.event }}</h3>
              <p>{{ m.stage }} · {{ m.venue }}</p>
            </div>
            <p class="sch-note">{{ m.watch }}</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="container">
        <div class="section-head">
          <h2 class="section-title">近期赛果</h2>
        </div>
        <div class="table-wrap">
          <table>
            <thead>
              <tr>
                <th>日期</th>
                <th>赛事</th>
                <th>对阵</th>
                <th>比分</th>
                <th>结果</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="r in results" :key="r.event + r.date">
                <td>{{ r.date }}</td>
                <td>{{ r.event }}</td>
                <td>{{ r.playerA }} vs {{ r.playerB }}</td>
                <td>{{ r.score }}</td>
                <td>{{ r.result }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <h2 class="section-title">年度冠军榜</h2>
        </div>
        <div class="table-wrap">
          <table>
            <thead>
              <tr>
                <th>年份</th>
                <th>赛事</th>
                <th>冠军</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="c in champions" :key="c.event + c.year">
                <td>{{ c.year }}</td>
                <td>{{ c.event }}</td>
                <td>{{ c.champion }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="container">
        <div class="section-head">
          <h2 class="section-title">赛制与观赛</h2>
        </div>
        <div class="rules-grid">
          <div v-for="r in rules" :key="r.title" class="rule card">
            <h3>{{ r.title }}</h3>
            <p>{{ r.desc }}</p>
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

.schedule {
  border: 1px solid var(--line);
  background: #ffffff;
}

.schedule-row {
  display: grid;
  grid-template-columns: 130px 1fr 200px;
  align-items: center;
  gap: 32px;
  padding: 30px 34px;
  border-bottom: 1px solid var(--line);
  transition: background 0.3s ease, padding-left 0.4s var(--ease-out);
}

.schedule-row:last-child {
  border-bottom: none;
}

.schedule-row:hover {
  background: var(--bg-soft);
  padding-left: 42px;
}

.sch-date p {
  font-family: var(--serif);
  font-size: 28px;
  color: var(--gold);
}

.sch-date span {
  font-size: 12px;
  letter-spacing: 0.2em;
  color: var(--muted);
}

.sch-main h3 {
  font-family: var(--serif);
  font-size: 20px;
  color: var(--paper);
  letter-spacing: 0.06em;
}

.sch-main p {
  margin-top: 6px;
  font-size: 13px;
  color: var(--muted);
}

.sch-note {
  font-size: 13px;
  color: var(--text);
  text-align: right;
}

.rules-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 28px;
}

.rule {
  padding: 40px 34px;
  background: #ffffff;
}

.rule h3 {
  font-family: var(--serif);
  font-size: 19px;
  color: var(--paper);
  letter-spacing: 0.1em;
  margin-bottom: 14px;
}

.rule p {
  font-size: 13px;
  color: var(--muted);
}

@media (max-width: 960px) {
  .schedule-row {
    grid-template-columns: 1fr;
    gap: 12px;
  }
  .sch-note {
    text-align: left;
  }
  .rules-grid {
    grid-template-columns: 1fr 1fr;
  }
}

@media (max-width: 640px) {
  .rules-grid {
    grid-template-columns: 1fr;
  }
}
</style>
