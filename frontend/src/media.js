// 统一资源路径：开发环境为 /，GitHub Pages 部署为 /home/
export const media = (p) => import.meta.env.BASE_URL + p
