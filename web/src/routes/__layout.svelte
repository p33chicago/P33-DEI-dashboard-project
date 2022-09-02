<script lang="ts">
	import Header from '$lib/header/Header.svelte';
	// import Footer from '$lib/footer/Footer.svelte';
	import Tota11y from '$lib/Tota11y.svelte';
	import '../app.css';
</script>

<div class="min-h-full flex flex-col">
	<Header />

	<main class="align-top justify-left p-2 max-w-[100vw]">
		<slot />
	</main>

	<!-- <Footer /> -->
	<Tota11y />
</div>

<style>
	main > :global(*) {
		max-width: 80rem; /* 2xl */
	}
</style>