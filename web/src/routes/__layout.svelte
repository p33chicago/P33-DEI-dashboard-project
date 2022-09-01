<script lang="ts">
	import Footer from '$lib/footer/Footer.svelte';
	import Header from '$lib/header/Header.svelte';
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
</div>

<style>
	/* main {
		flex: 1;
		display: flex;
		flex-direction: column;
		padding: 1rem 0;
		width: 100%;
		box-sizing: border-box;
		min-height: 100vh;
	} */
</style>
