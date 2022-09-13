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

	<main class="grid grid-cols-4 align-top justify-left px-4 md:px-8 py-1.5 md:py-3.5 gap-x-8 gap-y-2 md:gap-y-3.5 mx-auto">
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