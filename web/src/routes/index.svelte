<script context="module" lang="ts">
	export const prerender = true;
</script>

<script lang="ts">
	import { browser } from '$app/env';
	
	// let Figure;

	const load = async () => {
		window.global = window;
		window.Plotly = await import('plotly.js/dist/plotly-basic.min.js');
		const {data, layout} = (await import('../../../data/figure.json')).default;
		const node = document.querySelector('#figure');
		const plot = await Plotly.newPlot(node, data, layout);
		console.log(Plotly.validate(data, layout));
	}

	if (browser) {
		load();
	}
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="P33" />
</svelte:head>

<section class="sm:grid-col-1 lg:grid-col-4">
	<div class="fig" id="figure" />
	<h1>some fig</h1>
	<h1>some fig</h1>
	<h1>some fig</h1>
</section>

<style>
	section {
		display: flex;
		flex-direction: row;
		justify-content: space-around;
		/* align-items: center; */
		flex: 1;
	}
</style>
