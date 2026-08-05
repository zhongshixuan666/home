<script setup>
defineProps({
  variant: { type: String, default: 'grid' },
  count: { type: Number, default: 4 },
  cols: { type: Number, default: 4 },
  imgHeight: { type: Number, default: 210 },
})
</script>

<template>
  <div class="skeleton" role="status" aria-live="polite">
    <span class="skeleton-sr">内容加载中…</span>

    <!-- 卡片网格骨架：资讯 / 推荐 / 产品 / 球员等 -->
    <div v-if="variant === 'grid'" class="sk-grid" :style="{ '--sk-cols': cols }">
      <div v-for="i in count" :key="i" class="sk-card">
        <div v-if="imgHeight > 0" class="sk sk-img" :style="{ height: imgHeight + 'px' }"></div>
        <div class="sk-body">
          <div v-if="imgHeight > 0" class="sk-meta">
            <div class="sk sk-tag"></div>
            <div class="sk sk-date"></div>
          </div>
          <div class="sk sk-line long"></div>
          <div class="sk sk-line mid"></div>
        </div>
      </div>
    </div>

    <!-- 头条 + 列表骨架：资讯页 -->
    <div v-else-if="variant === 'page'" class="sk-page">
      <div class="sk-page-featured">
        <div class="sk sk-img"></div>
        <div class="sk-page-body">
          <div class="sk sk-tag"></div>
          <div class="sk sk-line long"></div>
          <div class="sk sk-line mid"></div>
          <div class="sk sk-line short"></div>
        </div>
      </div>
      <div class="sk-grid" :style="{ '--sk-cols': cols }">
        <div v-for="i in count" :key="i" class="sk-card">
          <div v-if="imgHeight > 0" class="sk sk-img" :style="{ height: imgHeight + 'px' }"></div>
          <div class="sk-body">
            <div class="sk sk-line long"></div>
            <div class="sk sk-line mid"></div>
          </div>
        </div>
      </div>
    </div>

    <!-- 轮播 + 档案骨架：球员页 -->
    <div v-else-if="variant === 'carousel'" class="sk-carousel-layout">
      <div class="sk sk-carousel"></div>
      <div class="sk-carousel-body">
        <div class="sk sk-line long"></div>
        <div class="sk sk-line mid"></div>
        <div v-for="i in 4" :key="i" class="sk sk-line short"></div>
      </div>
    </div>

    <!-- 列表行骨架：赛程 / 长列表 -->
    <div v-else-if="variant === 'list'" class="sk-list">
      <div v-for="i in count" :key="i" class="sk sk-row"></div>
    </div>

    <!-- 大图 / Hero 骨架 -->
    <div v-else class="sk" :style="{ height: imgHeight + 'px' }"></div>
  </div>
</template>
