<script setup>
import PageShell from './components/PageShell.vue'
</script>

<template>
  <PageShell>
    <RouterView v-slot="{ Component }">
      <Transition name="page" mode="out-in">
        <component :is="Component" />
      </Transition>
    </RouterView>
  </PageShell>
</template>
