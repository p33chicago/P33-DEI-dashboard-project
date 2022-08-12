<script context="module" lang="ts">
	export const prerender = true;
</script>

<script lang="ts">
	import Counter from '$lib/Counter.svelte';
	import { browser } from '$app/env';
	
	// let Figure;

	const load = async () => {
		window.global = window;
		window.Plotly = await import('plotly.js/lib/core.js');

		// via JSON
		const {data, layout} = (await import('../../../data/figure.json')).default;
		const node = document.querySelector('#figure');
		// console.log(data);
		// console.log(Plotly.validate(data));
		// console.log(layout);
		// console.log(Plotly.validate(json));
		const plot = Plotly.newPlot(node, data, layout);

		// via HTML
		// Figure = (await import('../../../data/figure.svelte')).default;
	}

	if (browser) {
		load();
	}
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section>
	Figure:
	<!-- {#if browser && typeof Figure !== 'undefined'}
	<svelte:component this={Figure}/>
	{/if} -->
	<div id="figure" />
</section>

<style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 1;
	}

	h1 {
		width: 100%;
	}

	.welcome {
		display: block;
		position: relative;
		width: 100%;
		height: 0;
		padding: 0 0 calc(100% * 495 / 2048) 0;
	}

	.welcome img {
		position: absolute;
		width: 100%;
		height: 100%;
		top: 0;
		display: block;
	}
</style>
