<script setup>
import { reactive, ref } from 'vue'

const form = reactive({
  name: '',
  phone: '',
  project_type: '投稿合作',
  message: '',
})

const projectTypes = ['投稿合作', '媒体采访', '商务合作', '品牌赞助', '网站咨询', '其他']

const submitting = ref(false)
const submitState = ref(null) // 'ok' | 'error'
const phoneError = ref('')
const serverError = ref('')

const PHONE_RE = /^1[3-9]\d{9}$/

async function submit() {
  phoneError.value = ''
  if (!PHONE_RE.test(form.phone)) {
    phoneError.value = '请输入 11 位大陆手机号（1 开头，第二位 3-9）'
    return
  }
  submitting.value = true
  submitState.value = null
  serverError.value = ''
  try {
    const res = await fetch('/api/contact/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        name: form.name,
        phone: form.phone,
        project_type: form.project_type,
        message: form.message,
      }),
    })
    const data = await res.json()
    if (res.ok && data.ok) {
      submitState.value = 'ok'
    } else {
      submitState.value = 'error'
      serverError.value = data.error || '提交失败，请稍后重试'
    }
  } catch (e) {
    submitState.value = 'error'
    serverError.value = '无法连接后端服务，请确认 Django 服务已启动'
  }
  submitting.value = false
}

function resetForm() {
  form.name = ''
  form.phone = ''
  form.project_type = '投稿合作'
  form.message = ''
  submitState.value = null
  phoneError.value = ''
  serverError.value = ''
}

const steps = [
  { num: '01', title: '提交需求', desc: '填写联系人、联系电话、项目类型与需求说明，我们会在一个工作日内确认收悉。' },
  { num: '02', title: '初步沟通', desc: '编辑与商务同事与你电话或邮件沟通，明确合作范围与时间安排。' },
  { num: '03', title: '方案确认', desc: '根据需求输出合作方案与排期，双方确认后进入执行阶段。' },
  { num: '04', title: '落地交付', desc: '稿件、专题或合作内容按约定发布，并提供数据反馈与结项报告。' },
]

const faqs = [
  { q: '如何投稿？', a: '将稿件以 Word 或 Markdown 格式随表单提交，或发送至 editorial@yujie.com，注明作者与联系方式即可。' },
  { q: '可以转载你们的内容吗？', a: '欢迎非商业性转载，请注明出处并保留原文链接；商业使用需提前取得书面授权。' },
  { q: '如何获取比赛门票信息？', a: '大型赛事开票信息会在「比赛」页提前发布，同时可关注合作票务平台公告。' },
  { q: '品牌合作一般提前多久联系？', a: '建议至少提前三周沟通，涉及大赛节点的合作请提前一个月以上确认排期。' },
]
</script>

<template>
  <div>
    <div class="page-head">
      <div class="container">
        <p class="eyebrow">Contact Us</p>
        <h1>联系我们</h1>
        <p>投稿、合作、媒体采访或意见反馈，欢迎随时与我们联系。</p>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <h2 class="section-title">合作流程</h2>
        </div>
        <div class="steps-grid">
          <div v-for="s in steps" :key="s.num" class="step micro-card">
            <p class="step-num">{{ s.num }}</p>
            <h3>{{ s.title }}</h3>
            <p>{{ s.desc }}</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="container">
        <div class="contact-grid">
          <div class="contact-info">
            <h2>编辑部</h2>
            <div class="hairline"></div>
            <ul class="info-list">
              <li>
                <span>地址</span>
                <p>北京市朝阳区体育中心路 88 号 羽界编辑部</p>
              </li>
              <li>
                <span>电话</span>
                <p>+86 10-8888 6688</p>
              </li>
              <li>
                <span>邮箱</span>
                <p>editorial@yujie.com</p>
              </li>
              <li>
                <span>商务</span>
                <p>business@yujie.com</p>
              </li>
            </ul>

            <h2 class="mt">工作时间</h2>
            <div class="hairline"></div>
            <ul class="info-list">
              <li>
                <span>周一至周五</span>
                <p>09:00 – 18:00</p>
              </li>
              <li>
                <span>周六至周日</span>
                <p>10:00 – 17:00（仅赛事直播值班）</p>
              </li>
            </ul>
          </div>

          <div class="contact-form">
            <template v-if="submitState !== 'ok'">
              <h2>提交需求</h2>
              <div class="hairline"></div>
              <form @submit.prevent="submit">
                <div class="field">
                  <label>联系人</label>
                  <input v-model="form.name" type="text" required placeholder="你的称呼" />
                </div>
                <div class="field">
                  <label>联系电话</label>
                  <input v-model="form.phone" type="tel" required placeholder="11 位大陆手机号" />
                  <p v-if="phoneError" class="form-error">{{ phoneError }}</p>
                </div>
                <div class="field">
                  <label>项目类型</label>
                  <select v-model="form.project_type">
                    <option v-for="t in projectTypes" :key="t" :value="t">{{ t }}</option>
                  </select>
                </div>
                <div class="field">
                  <label>需求说明</label>
                  <textarea v-model="form.message" rows="6" required placeholder="请简要描述你的需求"></textarea>
                </div>
                <button type="submit" class="btn btn-solid" :disabled="submitting">
                  {{ submitting ? '提交中…' : '提交表单' }}
                </button>
                <p v-if="submitState === 'error'" class="form-error">
                  {{ serverError || '提交失败，请检查网络或稍后重试；也可直接发送邮件至 editorial@yujie.com。' }}
                </p>
              </form>
            </template>

            <div v-else class="submit-ok">
              <p class="eyebrow">Message Received</p>
              <h2>已收到你的需求</h2>
              <p>
                感谢 {{ form.name }} 的来信，我们会在 1–2 个工作日内通过 {{ form.phone }} 与你联系。
              </p>
              <button class="btn" @click="resetForm">再提交一封</button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
          <h2 class="section-title">常见问题</h2>
        </div>
        <div class="faq">
          <div v-for="f in faqs" :key="f.q" class="faq-item micro-card">
            <h3>{{ f.q }}</h3>
            <p>{{ f.a }}</p>
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

.steps-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 28px;
}

.step {
  padding: 44px 34px;
  border: 1px solid var(--line);
  background: #ffffff;
}

.step-num {
  font-family: var(--serif);
  font-size: 26px;
  color: var(--gold);
}

.step h3 {
  margin-top: 16px;
  font-family: var(--serif);
  font-size: 19px;
  color: var(--paper);
  letter-spacing: 0.1em;
}

.step p:not(.step-num) {
  margin-top: 12px;
  font-size: 13px;
  color: var(--muted);
}

.contact-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 80px;
}

.contact-info h2,
.contact-form h2 {
  font-family: var(--serif);
  font-size: 24px;
  color: var(--paper);
  letter-spacing: 0.12em;
}

.contact-info h2.mt {
  margin-top: 52px;
}

.info-list {
  list-style: none;
}

.info-list li {
  display: flex;
  gap: 26px;
  padding: 16px 0;
  border-bottom: 1px solid var(--line);
}

.info-list span {
  width: 96px;
  font-size: 12px;
  letter-spacing: 0.18em;
  color: var(--gold);
}

.info-list p {
  font-size: 14px;
  color: var(--text);
}

.contact-form {
  padding: 52px 48px 56px;
  border: 1px solid var(--line);
  background: #ffffff;
}

.field {
  margin-bottom: 26px;
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

.form-error {
  margin-top: 18px;
  font-size: 13px;
  color: #a34a3a;
}

.submit-ok {
  padding: 48px 0;
  text-align: center;
}

.submit-ok h2 {
  font-size: 28px;
}

.submit-ok p:not(.eyebrow) {
  margin: 18px 0 36px;
  color: var(--muted);
  font-size: 14px;
}

.faq {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 32px;
}

.faq-item {
  padding: 40px 34px;
  border: 1px solid var(--line);
  background: #ffffff;
}

.faq-item h3 {
  font-family: var(--serif);
  font-size: 18px;
  color: var(--paper);
  letter-spacing: 0.08em;
  margin-bottom: 14px;
}

.faq-item p {
  font-size: 13px;
  color: var(--muted);
}

@media (max-width: 960px) {
  .steps-grid {
    grid-template-columns: 1fr 1fr;
  }
  .contact-grid {
    grid-template-columns: 1fr;
    gap: 44px;
  }
}

@media (max-width: 640px) {
  .steps-grid,
  .faq {
    grid-template-columns: 1fr;
  }
}
</style>
