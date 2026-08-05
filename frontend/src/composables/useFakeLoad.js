import { ref } from 'vue'

// 页面内容为静态演示数据，不主动制造额外加载延迟。
// 接入真实接口时再改为根据请求状态控制 loading。
export function useFakeLoad() {
  const loading = ref(false)
  return { loading }
}
