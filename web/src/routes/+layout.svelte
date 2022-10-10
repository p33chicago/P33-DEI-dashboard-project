<script lang="ts">
	import '../app.css';
	import Header from '$lib/header/Header.svelte';
	import Tota11y from '$lib/Tota11y.svelte';
	import MainContent from '$lib/MainContent.svelte';

	export const csr = false;
	export const prerender = true;
</script>

<div class="font-sans min-h-full flex flex-col">
	<Header />
	<MainContent>
		<slot />
	</MainContent>
	<Tota11y />
</div>
