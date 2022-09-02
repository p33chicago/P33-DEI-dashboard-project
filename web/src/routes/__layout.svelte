<script lang="ts">
	import Header from '$lib/header/Header.svelte';
	// import Footer from '$lib/footer/Footer.svelte';
	import Tota11y from '$lib/Tota11y.svelte';
	import '../app.css';
</script>

<div class="min-h-full flex flex-col">
	<Header />

	<main class="m-8 align-top">
		<div class="max-w-7xl m-auto justify-left">
			<slot />
		</div>
	</main>

	<!-- <Footer /> -->
	<Tota11y />
</div>