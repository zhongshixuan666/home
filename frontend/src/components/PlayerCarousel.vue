<script setup>
import { onBeforeUnmount, onMounted, ref } from 'vue'

const props = defineProps({
  images: { type: Array, required: true },
  alt: { type: String, default: '' },
})

const index = ref(0)
let timer = null

function next() {
  index.value = (index.value + 1) % props.images.length
}

function prev() {
  index.value = (index.value - 1 + props.images.length) % props.images.length
}

function start() {
  stop()
  timer = setInterval(next, 4500)
}

function stop() {
  if (timer) {
    clearInterval(timer)
    timer = null
  }
}

onMounted(start)
onBeforeUnmount(stop)
</script>

<template>
  <div class="carousel" @mouseenter="stop" @mouseleave="start">
    <div class="stage">
      <img
        v-for="(img, i) in images"
        :key="img"
        :src="img"
        :alt="alt"
        class="slide"
        :class="{ show: i === index }"
      />
    </div>
    <button class="arrow prev" aria-label="上一张" @click="prev">‹</button>
    <button class="arrow next" aria-label="下一张" @click="next">›</button>
    <div class="dots">
      <span
        v-for="(img, i) in images"
        :key="img"
        class="dot"
        :class="{ on: i === index }"
        @click="index = i"
      ></span>
    </div>
  </div>
</template>

<style scoped>
.carousel {
  position: relative;
  border: 1px solid var(--line);
  background: var(--ink-2);
  overflow: hidden;
}

.stage {
  position: relative;
  height: 520px;
}

.slide {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0;
  transition: opacity 1s ease;
}

.slide.show {
  opacity: 1;
}

.arrow {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 44px;
  height: 44px;
  border: 1px solid rgba(242, 237, 226, 0.4);
  background: rgba(15, 16, 19, 0.45);
  color: var(--paper);
  font-size: 24px;
  line-height: 1;
  cursor: pointer;
}

.arrow:hover {
  border-color: var(--gold);
  color: var(--gold);
}

.arrow.prev {
  left: 18px;
}

.arrow.next {
  right: 18px;
}

.dots {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 18px;
  display: flex;
  justify-content: center;
  gap: 10px;
}

.dot {
  width: 9px;
  height: 9px;
  border: 1px solid var(--muted);
  background: transparent;
  cursor: pointer;
}

.dot.on {
  background: var(--gold);
  border-color: var(--gold);
}
</style>
