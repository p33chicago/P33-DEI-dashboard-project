<script>
	import Figure from '$lib/figure/Figure.svelte';
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="P33" />
</svelte:head>

<section class="sm:grid-col-1 lg:grid-col-4">
	<Figure id="figure" />
	<Figure id="figure" />
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
