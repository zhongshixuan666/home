<script setup>
import { onMounted } from 'vue'
import { media } from '../media'

onMounted(() => {
  setTimeout(() => {
    window.location.href = media('pages/index.html')
  }, 2000)
})
</script>

<template>
  <section class="success-section">
    <div class="container">
      <p class="eyebrow">Register Success</p>
      <h1>注册成功</h1>
      <p>正在跳转首页，请稍候。</p>
      <a :href="media('pages/index.html')" class="btn btn-solid">立即进入首页</a>
    </div>
  </section>
</template>

<style scoped>
.success-section {
  padding: 160px 0;
  text-align: center;
}

.success-section h1 {
  font-family: var(--serif);
  font-size: 48px;
  color: var(--paper);
  letter-spacing: 0.12em;
}

.success-section p:not(.eyebrow) {
  margin: 20px 0 36px;
  color: var(--muted);
  font-size: 15px;
}
</style>
