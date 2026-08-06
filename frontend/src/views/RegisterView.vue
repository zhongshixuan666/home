<script setup>
import { reactive, ref } from 'vue'
import { media } from '../media'

const form = reactive({
  username: '',
  phone: '',
  email: '',
  password: '',
  channel: 'phone',
  code: '',
})

const error = ref('')
const message = ref('')
const codeMessage = ref('')
const sending = ref(false)
const loading = ref(false)

async function sendCode() {
  error.value = ''
  codeMessage.value = ''
  const account = form.channel === 'phone' ? form.phone : form.email
  if (!account) {
    error.value = form.channel === 'phone' ? '请先填写手机号' : '请先填写邮箱'
    return
  }

  sending.value = true
  try {
    const res = await fetch('/api/auth/send-code/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ channel: form.channel, account, purpose: 'register' }),
    })
    const data = await res.json()
    if (res.ok && data.ok) {
      codeMessage.value = data.dev_code ? `演示模式验证码：${data.dev_code}` : data.message
    } else {
      error.value = data.error || '验证码发送失败'
    }
  } catch (e) {
    error.value = '无法连接后端服务，请确认 Django 服务已启动'
  } finally {
    sending.value = false
  }
}

async function submit() {
  error.value = ''
  message.value = ''
  loading.value = true
  try {
    const res = await fetch('/api/auth/register/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form),
    })
    const data = await res.json()
    if (res.ok && data.ok) {
      message.value = data.message
      window.location.href = media('pages/register-success.html')
      return
    }
    error.value = data.error || '注册失败，请稍后重试'
  } catch (e) {
    error.value = '无法连接后端服务，请确认 Django 服务已启动'
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <section class="auth-section">
    <div class="container auth-grid">
      <div class="auth-visual">
        <img :src="media('images/hero-banner.webp')" alt="羽界赛场" />
        <div class="visual-mark">
          <img :src="media('logo.svg')" alt="羽界" />
        </div>
      </div>

      <div class="auth-panel">
        <p class="panel-kicker">Register</p>
        <h2>创建账号</h2>
        <form @submit.prevent="submit">
          <div class="field">
            <label>用户名</label>
            <input v-model="form.username" type="text" autocomplete="username" placeholder="至少 2 个字符" />
          </div>
          <div class="field">
            <label>手机号</label>
            <input v-model="form.phone" type="tel" autocomplete="tel" placeholder="11 位大陆手机号" />
          </div>
          <div class="field">
            <label>邮箱</label>
            <input v-model="form.email" type="email" autocomplete="email" placeholder="example@yujie.com" />
          </div>
          <div class="field">
            <label>密码</label>
            <input v-model="form.password" type="password" autocomplete="new-password" placeholder="至少 6 位" />
          </div>
          <div class="field">
            <label>验证方式</label>
            <select v-model="form.channel">
              <option value="phone">手机验证</option>
              <option value="email">邮箱验证</option>
            </select>
          </div>
          <div class="code-row">
            <div class="field code-field">
              <label>验证码</label>
              <input v-model="form.code" type="text" inputmode="numeric" maxlength="6" placeholder="6 位验证码" />
            </div>
            <button type="button" class="btn code-btn" :disabled="sending" @click="sendCode">
              {{ sending ? '发送中…' : '发送验证码' }}
            </button>
          </div>
          <p v-if="codeMessage" class="code-message">{{ codeMessage }}</p>
          <button type="submit" class="btn btn-solid auth-submit" :disabled="loading">
            {{ loading ? '注册中…' : '注册' }}
          </button>
          <p v-if="error" class="form-error">{{ error }}</p>
          <p v-if="message" class="form-success">{{ message }}</p>
        </form>
        <p class="auth-switch">已有账号？<a :href="media('pages/login.html')">直接登录</a></p>
      </div>
    </div>
  </section>
</template>

<style scoped>
.auth-section {
  padding: 128px 0;
}

.auth-grid {
  display: grid;
  grid-template-columns: 1.1fr 0.9fr;
  gap: 96px;
  align-items: center;
}

.auth-visual {
  position: relative;
  min-height: 600px;
  overflow: hidden;
  border: 1px solid var(--line);
  background: var(--bg-soft);
}

.auth-visual img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.visual-mark {
  position: absolute;
  top: 28px;
  left: 28px;
  padding: 12px 16px;
  background: rgba(255, 255, 255, 0.92);
  border: 1px solid var(--line);
}

.visual-mark img {
  position: static;
  width: auto;
  height: 34px;
}

.auth-panel {
  padding: 56px 52px;
  border: 1px solid var(--line);
  background: #ffffff;
}

.panel-kicker {
  font-size: 12px;
  letter-spacing: 0.32em;
  color: var(--gold);
}

.auth-panel h2 {
  margin-top: 12px;
  font-family: var(--serif);
  font-size: 28px;
  color: var(--paper);
  letter-spacing: 0.12em;
}

.field {
  margin-top: 22px;
}

.field label {
  display: block;
  font-size: 12px;
  letter-spacing: 0.24em;
  color: var(--gold);
  margin-bottom: 10px;
}

.field input,
.field select {
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
.field select:focus {
  border-color: var(--gold);
}

.code-row {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 16px;
  align-items: end;
}

.code-btn {
  margin-bottom: 4px;
  padding: 12px 20px;
  white-space: nowrap;
}

.code-message,
.form-error,
.form-success {
  margin-top: 14px;
  font-size: 13px;
}

.code-message,
.form-success {
  color: #3d6b48;
}

.form-error {
  color: #a34a3a;
}

.auth-submit {
  width: 100%;
  margin-top: 32px;
}

.auth-switch {
  margin-top: 26px;
  font-size: 13px;
  color: var(--muted);
}

.auth-switch a {
  color: var(--gold);
}

@media (max-width: 960px) {
  .auth-grid {
    grid-template-columns: 1fr;
    gap: 48px;
  }
  .auth-visual {
    min-height: 340px;
  }
  .code-row {
    grid-template-columns: 1fr;
  }
}
</style>
