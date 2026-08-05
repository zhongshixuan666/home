<script setup>
const upcoming = [
  { date: '08.15', time: '18:00', event: '世界羽毛球锦标赛', stage: '男单 1/4 决赛', venue: '西班牙 · 马德里', watch: '小组赛签表已出炉' },
  { date: '09.02', time: '10:00', event: '中国羽毛球公开赛', stage: '正赛首轮', venue: '中国 · 常州', watch: '国羽全主力出战' },
  { date: '09.20', time: '11:00', event: '日本羽毛球公开赛', stage: '正赛首轮', venue: '日本 · 大阪', watch: '种子名单公布' },
  { date: '10.05', time: '15:00', event: '丹麦公开赛', stage: '正赛首轮', venue: '丹麦 · 欧登塞', watch: '欧洲赛季收官战' },
  { date: '11.02', time: '13:00', event: '法国公开赛', stage: '正赛首轮', venue: '法国 · 巴黎', watch: '奥运场馆再迎大赛' },
  { date: '12.14', time: '14:00', event: '世界羽联巡回赛总决赛', stage: '小组赛', venue: '中国 · 杭州', watch: '年终巅峰对决' },
]

const results = [
  { date: '2026.07.28', event: '全英公开赛 · 决赛', playerA: '安赛龙', playerB: '李梓嘉', score: '21:18 21:16', result: '安赛龙胜' },
  { date: '2026.07.26', event: '全英公开赛 · 半决赛', playerA: '李梓嘉', playerB: '乔纳坦', score: '21:14 19:21 21:17', result: '李梓嘉胜' },
  { date: '2026.07.20', event: '印尼公开赛 · 决赛', playerA: '安赛龙', playerB: '昆拉武特', score: '21:19 21:15', result: '安赛龙胜' },
  { date: '2026.07.18', event: '印尼公开赛 · 半决赛', playerA: '李美秒', playerB: '山口茜', score: '21:17 18:21 21:19', result: '李美秒胜' },
  { date: '2026.07.12', event: '马来西亚公开赛 · 决赛', playerA: '李梓嘉', playerB: '石宇奇', score: '21:16 22:20', result: '李梓嘉胜' },
  { date: '2026.07.05', event: '新加坡公开赛 · 决赛', playerA: '安赛龙', playerB: '李美秒', score: '21:12 21:14', result: '安赛龙胜' },
]

const champions = [
  { year: '2026', event: '世界羽毛球锦标赛', champion: '待定 · 8 月揭晓' },
  { year: '2026', event: '全英公开赛', champion: '安赛龙' },
  { year: '2026', event: '印尼公开赛', champion: '安赛龙' },
  { year: '2026', event: '马来西亚公开赛', champion: '李梓嘉' },
  { year: '2025', event: '世界羽毛球锦标赛', champion: '安赛龙' },
  { year: '2025', event: '世界羽联巡回赛总决赛', champion: '李梓嘉' },
]

const rules = [
  { title: '赛制', desc: '国际大赛单打采用 21 分制三局两胜，每局先到 21 分且净胜 2 分者获胜，30 分封顶。' },
  { title: '积分体系', desc: '世界羽联巡回赛按超级 100–1000 与总决赛等级累计积分，奥运与世锦赛积分权重最高。' },
  { title: '签表规则', desc: '种子选手按世界排名分配至各半区，同协会选手在早轮次原则上不相遇。' },
  { title: '观赛指南', desc: '欧洲赛事与北京时差 6–7 小时，美洲 12–13 小时，本页赛程均以北京时间标注。' },
]
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
        <div class="schedule">
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
  gap: 28px;
  padding: 26px 30px;
  border-bottom: 1px solid var(--line);
}

.schedule-row:last-child {
  border-bottom: none;
}

.schedule-row:hover {
  background: var(--bg-soft);
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
  gap: 24px;
}

.rule {
  padding: 34px 30px;
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
