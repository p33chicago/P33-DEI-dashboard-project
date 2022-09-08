<script>
	import Figure from '$lib/figure/Figure.svelte';
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="P33" />
</svelte:head>

<div class="container flex space-x-4 overflow-scroll snap-x snap-mandatory">
	<div class="space-y-4 text-center">
		<div class="drop-shadow-card">
			<h1 class="capitalize"><a href="/k8/access">K-8</a></h1>
			<p>City of Chicago</p>
		</div>
		<div class="drop-shadow-card">
			<Figure id="figure" />
		</div>
	</div>
	<div class="space-y-4 text-center">
		<div class="drop-shadow-card">
			<h1 class="capitalize"><a href="/hs/access">High school</a></h1>
			<p>City of Chicago</p>
		</div>
		<div class="drop-shadow-card">
			<Figure id="figure" />
		</div>
	</div>
	<div class="space-y-4 text-center">
		<div class="drop-shadow-card">
			<h1 class="capitalize"><a href="/college/access">College</a></h1>
			<p>City of Chicago</p>
		</div>
		<div class="drop-shadow-card">
			<Figure id="figure" />
		</div>
	</div>
	<div class="space-y-4 text-center">
		<div class="drop-shadow-card">
			<h1 class="capitalize"><a href="/career/access">Career</a></h1>
			<p>City of Chicago</p>
		</div>
		<div class="drop-shadow-card">
			<Figure id="figure" />
		</div>
	</div>
</div>

<style>
	.container > * {
		min-width: calc(320px - 1rem);
		width: calc(320px - 1rem);
		scroll-snap-align: center;
	}
	.container > * > * {
		background-color: white;
		box-sizing: border-box;
		padding: 1rem;
	}
	.container > * > * > :global(*) {
		/* margin: 1rem; */
	}
</style>
