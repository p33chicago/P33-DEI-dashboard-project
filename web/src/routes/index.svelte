<script>
	import Figure from '$lib/figure/Figure.svelte';
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="P33" />
</svelte:head>

<div class="container flex space-x-4 overflow-scroll snap-x snap-mandatory">
	<div>
		<p>Some stuff</p>
		<Figure id="figure" />
	</div>
	<div>
		<p>Other stuff</p>
		<Figure id="figure" />
	</div>
	<div>
		<p>More stupid stuff</p>
		<Figure id="figure" />
	</div>
	<div>
		<p>More stupid stuff</p>
		<Figure id="figure" />
	</div>
</div>

<style>
	.container > * {
		background-color: white;
		min-width: calc(320px - 1rem);
		width: calc(320px - 1rem);
		scroll-snap-align: center;
	}
	.container > * > :global(*) {
		margin: 1rem;
	}
</style>
