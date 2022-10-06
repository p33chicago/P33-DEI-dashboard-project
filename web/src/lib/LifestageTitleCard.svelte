<script lang="ts">
	import Card from './cards/Card.svelte';
	export let title: string;
	let subtitle = 'Chicago Public Schools';
</script>

<Card>
	<h1 class="capitalize text-6xl text-center">{title}</h1>
	<p class="text-center">{subtitle}</p>
</Card>
