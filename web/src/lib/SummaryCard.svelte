<script lang="ts">
	import MainInfo from './cards/MainInfo.svelte';
	export let title: string;
</script>

<MainInfo>
	<h1>{title}</h1>
</MainInfo>
