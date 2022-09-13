<script lang="ts">
	import Header from '$lib/header/Header.svelte';
	// import Footer from '$lib/footer/Footer.svelte';
	import Tota11y from '$lib/Tota11y.svelte';
	import '../app.css';

	export const csr = false;
	export const prerender = true;
</script>

<div class="min-h-full flex flex-col">
	<Header />

	<main class="flex flex-wrap align-top justify-left gap-x-8 p-4 md:p-8 max-w-7xl mx-auto">
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