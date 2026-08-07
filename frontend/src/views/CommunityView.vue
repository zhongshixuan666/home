<script setup>
import { onMounted, reactive, ref } from 'vue'

const fallbackPosts = [
  {
    id: 1,
    title: '安赛龙之后，男单的下一个统治级选手会是谁？',
    content: '石宇奇的状态越来越稳定，李诗沣也在快速成长。男单现在更像是一个群雄逐鹿的时代，谁能先拿下大赛冠军，谁就能占据心理优势。',
    author: '羽球观察员',
    category: '赛事讨论',
    views: 286,
    likes: 46,
    hot_score: 860,
    created_at: '2026-08-07T09:30:00+08:00',
  },
  {
    id: 2,
    title: '分享一套适合业余球友的防守训练计划',
    content: '这套训练从接杀站位开始，再到多球反应，最后加入半场对抗。核心不是动作多漂亮，而是每次都能稳定把球回到底线。',
    author: '业余训练笔记',
    category: '训练心得',
    views: 174,
    likes: 31,
    hot_score: 640,
    created_at: '2026-08-06T21:12:00+08:00',
  },
  {
    id: 3,
    title: '大家现在主力球拍是什么？预算 800 左右有推荐吗',
    content: '最近想换一支进攻型球拍，之前一直打均衡拍，想知道同价位里哪些型号更适合我这种发力一般但喜欢杀球的球友。',
    author: '球拍小白',
    category: '装备交流',
    views: 132,
    likes: 18,
    hot_score: 520,
    created_at: '2026-08-06T15:40:00+08:00',
  },
]

const fallbackHot = [
  { id: 1, title: '全英公开赛签表分析', hot_score: 982 },
  { id: 2, title: '石宇奇最新状态', hot_score: 874 },
  { id: 3, title: '业余球拍选购指南', hot_score: 761 },
  { id: 4, title: '安赛龙退役回顾', hot_score: 688 },
  { id: 5, title: '李诗沣冠军', hot_score: 596 },
  { id: 6, title: '防守训练方法', hot_score: 511 },
]

const posts = ref([...fallbackPosts])
const hotTopics = ref([...fallbackHot])
const loading = ref(true)
const usingFallback = ref(false)

const categories = ['球迷投稿', '赛事讨论', '装备交流', '训练心得', '其他']
const form = reactive({
  title: '',
  content: '',
  author: '',
  category: '球迷投稿',
})

const submitting = ref(false)
const submitState = ref(null)
const serverError = ref('')
const isStaticPreview = import.meta.env.BASE_URL !== '/'

function formatDate(value) {
  if (!value) return '刚刚'
  const text = String(value)
  return text.slice(0, 10).replaceAll('-', '.')
}

function excerpt(value) {
  return String(value || '').slice(0, 160)
}

async function loadCommunity() {
  try {
    const [listRes, hotRes] = await Promise.all([
      fetch('/api/community/'),
      fetch('/api/community/hot/'),
    ])
    if (listRes.ok) {
      const data = await listRes.json()
      if (data.results && data.results.length) {
        posts.value = data.results
      }
    }
    if (hotRes.ok) {
      const data = await hotRes.json()
      if (data.results && data.results.length) {
        hotTopics.value = data.results
      }
    }
  } catch (e) {
    usingFallback.value = true
  } finally {
    loading.value = false
  }
}

async function submit() {
  serverError.value = ''
  if (!form.title.trim() || !form.content.trim() || !form.author.trim()) {
    serverError.value = '请填写标题、内容和作者昵称'
    return
  }

  submitting.value = true
  submitState.value = null
  try {
    const res = await fetch('/api/community/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        title: form.title.trim(),
        content: form.content.trim(),
        author: form.author.trim(),
        category: form.category,
      }),
    })
    const data = await res.json()
    if (res.ok && data.ok) {
      posts.value.unshift({
        id: data.id,
        title: form.title.trim(),
        content: form.content.trim(),
        author: form.author.trim(),
        category: form.category,
        views: 0,
        likes: 0,
        hot_score: 0,
        created_at: new Date().toISOString(),
      })
      form.title = ''
      form.content = ''
      form.author = ''
      form.category = '球迷投稿'
      submitState.value = 'ok'
    } else {
      submitState.value = 'error'
      serverError.value = data.error || '投稿失败，请稍后重试'
    }
  } catch (e) {
    submitState.value = 'error'
    serverError.value = isStaticPreview
      ? '当前为静态预览，无法连接 Django 后端；请使用本地完整版或部署 Django 后端。'
      : '无法连接后端服务，请确认 Django 服务已启动'
  }
  submitting.value = false
}

onMounted(loadCommunity)
</script>

<template>
  <div>
    <div class="page-head">
      <div class="container">
        <p class="eyebrow">Fan Community</p>
        <h1>球迷社区</h1>
        <p>分享比赛观点、训练经验与装备心得，让每一位羽球爱好者的声音被看见。</p>
      </div>
    </div>

    <section class="section section-alt">
      <div class="container">
        <div class="community-grid">
          <div class="submit-panel micro-card">
            <div class="panel-head">
              <p class="eyebrow">Submit</p>
              <h2>发布你的投稿</h2>
              <p>提交后内容会出现在最新投稿中，优秀内容有机会进入热搜榜。</p>
            </div>

            <form @submit.prevent="submit">
              <div class="field">
                <label>标题</label>
                <input v-model="form.title" type="text" maxlength="120" placeholder="用一句话说清你想聊的话题" />
              </div>
              <div class="field-row">
                <div class="field">
                  <label>分类</label>
                  <select v-model="form.category">
                    <option v-for="c in categories" :key="c" :value="c">{{ c }}</option>
                  </select>
                </div>
                <div class="field">
                  <label>作者昵称</label>
                  <input v-model="form.author" type="text" maxlength="50" placeholder="你的昵称" />
                </div>
              </div>
              <div class="field">
                <label>内容</label>
                <textarea v-model="form.content" rows="7" maxlength="2000" placeholder="写下你的观点、经验或问题"></textarea>
              </div>
              <button type="submit" class="btn btn-solid" :disabled="submitting">
                {{ submitting ? '发布中…' : '发布投稿' }}
              </button>
              <p v-if="submitState === 'ok'" class="form-tip success">投稿已发布，感谢你的分享。</p>
              <p v-if="submitState === 'error'" class="form-tip error">{{ serverError }}</p>
            </form>
          </div>

          <aside class="hot-panel micro-card">
            <div class="panel-head">
              <p class="eyebrow">Trending</p>
              <h2>热搜榜</h2>
              <p>根据浏览、点赞与热度值实时排序。</p>
            </div>
            <ol class="hot-list">
              <li v-for="(topic, index) in hotTopics" :key="topic.id || topic.title">
                <span class="hot-index" :class="{ top: index < 3 }">{{ index + 1 }}</span>
                <div class="hot-body">
                  <h3>{{ topic.title }}</h3>
                  <p>热度 {{ topic.hot_score || topic.views || topic.likes || 0 }}</p>
                </div>
              </li>
            </ol>
          </aside>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <h2 class="section-title">最新投稿</h2>
          <p class="section-more">来自球迷社区的实时内容</p>
        </div>

        <p v-if="loading" class="loading-note">正在加载投稿内容...</p>
        <div v-else class="post-grid">
          <article v-for="post in posts" :key="post.id || post.title" class="post-card micro-card">
            <div class="post-meta">
              <span class="tag">{{ post.category }}</span>
              <span class="post-date">{{ formatDate(post.created_at) }}</span>
            </div>
            <h3>{{ post.title }}</h3>
            <p>{{ excerpt(post.content) }}</p>
            <div class="post-foot">
              <span>{{ post.author }}</span>
              <span>{{ post.views || 0 }} 浏览 · {{ post.likes || 0 }} 点赞</span>
            </div>
          </article>
        </div>
        <p v-if="usingFallback" class="fallback-note">当前展示示例内容，连接 Django 后端后可查看真实用户投稿。</p>
      </div>
    </section>

    <section class="quote-band">
      <div class="container">
        <p class="quote-text">“好的社区不是只有热闹，而是每一次认真讨论都能被看见。”</p>
        <p class="quote-author">羽界球迷社区</p>
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

.community-grid {
  display: grid;
  grid-template-columns: 1.18fr 0.82fr;
  gap: 32px;
  align-items: start;
}

.submit-panel,
.hot-panel {
  padding: 48px 44px 52px;
  border: 1px solid var(--line);
  background: #ffffff;
}

.panel-head h2 {
  font-family: var(--serif);
  font-size: 26px;
  color: var(--paper);
  letter-spacing: 0.1em;
  margin-top: 12px;
}

.panel-head p:not(.eyebrow) {
  margin-top: 12px;
  font-size: 13px;
  color: var(--muted);
}

.field {
  margin-bottom: 24px;
}

.field-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}

.field label {
  display: block;
  font-size: 12px;
  letter-spacing: 0.24em;
  color: var(--gold);
  margin-bottom: 10px;
}

.field input,
.field select,
.field textarea {
  width: 100%;
  padding: 13px 16px;
  background: #ffffff;
  border: 1px solid var(--line);
  color: var(--paper);
  font-family: var(--sans);
  font-size: 14px;
  outline: none;
}

.field input:focus,
.field select:focus,
.field textarea:focus {
  border-color: var(--gold);
}

.field textarea {
  resize: vertical;
}

.form-tip {
  margin-top: 18px;
  font-size: 13px;
}

.form-tip.success {
  color: #2f6b43;
}

.form-tip.error {
  color: #a34a3a;
}

.hot-list {
  list-style: none;
  margin-top: 26px;
}

.hot-list li {
  display: grid;
  grid-template-columns: 42px 1fr;
  gap: 16px;
  align-items: center;
  padding: 15px 0;
  border-bottom: 1px solid var(--line);
}

.hot-list li:last-child {
  border-bottom: 0;
}

.hot-index {
  width: 34px;
  height: 34px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid var(--line);
  color: var(--muted);
  font-size: 13px;
}

.hot-index.top {
  border-color: var(--gold);
  color: var(--paper);
  background: var(--gold);
}

.hot-body h3 {
  font-family: var(--serif);
  font-size: 16px;
  color: var(--paper);
  letter-spacing: 0.04em;
}

.hot-body p {
  margin-top: 4px;
  font-size: 12px;
  color: var(--muted);
}

.loading-note,
.fallback-note {
  padding: 36px 0;
  color: var(--muted);
  font-size: 14px;
}

.post-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 32px;
}

.post-card {
  padding: 34px 32px 30px;
  border: 1px solid var(--line);
  background: #ffffff;
}

.post-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 18px;
}

.post-date {
  font-size: 12px;
  color: var(--muted);
}

.post-card h3 {
  font-family: var(--serif);
  font-size: 20px;
  line-height: 1.5;
  color: var(--paper);
  letter-spacing: 0.04em;
}

.post-card p:not(.post-date) {
  margin-top: 14px;
  font-size: 13px;
  color: var(--muted);
}

.post-foot {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 26px;
  padding-top: 18px;
  border-top: 1px solid var(--line);
  font-size: 12px;
  color: var(--muted);
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
  .community-grid,
  .post-grid {
    grid-template-columns: 1fr 1fr;
  }
}

@media (max-width: 640px) {
  .community-grid,
  .field-row,
  .post-grid {
    grid-template-columns: 1fr;
  }
  .submit-panel,
  .hot-panel {
    padding: 36px 26px 40px;
  }
}
</style>