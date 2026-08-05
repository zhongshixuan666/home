import { onBeforeUnmount, onMounted, ref } from 'vue'

// 模拟异步数据加载，用于演示骨架屏。
// 接入真实接口时，把 setTimeout 替换为实际请求即可（loading 语义不变）。
export function useFakeLoad(delay = 650) {
  const loading = ref(true)
  let timer = null

  onMounted(() => {
    timer = setTimeout(() => {
      loading.value = false
    }, delay)
  })

  onBeforeUnmount(() => {
    if (timer) clearTimeout(timer)
  })

  return { loading }
}
