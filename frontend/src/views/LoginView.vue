<script setup>
import { reactive, ref } from 'vue'
import { media } from '../media'

const form = reactive({
  account: '',
  password: '',
})

const error = ref('')
const message = ref('')
const loading = ref(false)

async function submit() {
  error.value = ''
  message.value = ''
  if (!form.account || !form.password) {
    error.value = '请输入账号和密码'
    return
  }

  loading.value = true
  try {
    const res = await fetch('/api/auth/login/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form),
    })
    const data = await res.json()
    if (res.ok && data.ok) {
      message.value = data.message
      window.location.href = media('pages/index.html')
      return
    }
    error.value = data.error || '登录失败，请稍后重试'
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
      <div class="auth-copy">
        <p class="eyebrow">Member Access</p>
        <h1>登录羽界</h1>
        <p>使用用户名、手机号或邮箱登录，继续查看球员档案、赛事动态和装备内容。</p>
        <a :href="media('pages/register.html')" class="btn">注册新账号</a>
      </div>

      <div class="auth-panel">
        <p class="panel-kicker">Account Login</p>
        <h2>账号登录</h2>
        <form @submit.prevent="submit">
          <div class="field">
            <label>账号</label>
            <input v-model="form.account" type="text" autocomplete="username" placeholder="用户名 / 手机号 / 邮箱" />
          </div>
          <div class="field">
            <label>密码</label>
            <input v-model="form.password" type="password" autocomplete="current-password" placeholder="请输入密码" />
          </div>
          <button type="submit" class="btn btn-solid auth-submit" :disabled="loading">
            {{ loading ? '登录中…' : '登录' }}
          </button>
          <p v-if="error" class="form-error">{{ error }}</p>
          <p v-if="message" class="form-success">{{ message }}</p>
        </form>
        <p class="auth-switch">还没有账号？<a :href="media('pages/register.html')">立即注册</a></p>
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
  grid-template-columns: 1fr 1fr;
  gap: 96px;
  align-items: center;
}

.auth-copy h1 {
  font-family: var(--serif);
  font-size: 56px;
  color: var(--paper);
  letter-spacing: 0.12em;
}

.auth-copy p:not(.eyebrow) {
  max-width: 480px;
  margin: 24px 0 36px;
  color: var(--muted);
  font-size: 15px;
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
  margin-top: 26px;
}

.field label {
  display: block;
  font-size: 12px;
  letter-spacing: 0.24em;
  color: var(--gold);
  margin-bottom: 10px;
}

.field input {
  width: 100%;
  padding: 13px 16px;
  background: #ffffff;
  border: 1px solid var(--line);
  color: var(--paper);
  font-family: var(--sans);
  font-size: 14px;
  outline: none;
}

.field input:focus {
  border-color: var(--gold);
}

.auth-submit {
  width: 100%;
  margin-top: 32px;
}

.form-error,
.form-success {
  margin-top: 18px;
  font-size: 13px;
}

.form-error {
  color: #a34a3a;
}

.form-success {
  color: #3d6b48;
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
}
</style>
