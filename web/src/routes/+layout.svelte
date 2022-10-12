<script lang="ts">
	import '../app.css';
	import Header from '$lib/components/header/Header.svelte';
	import Tota11y from '$lib/components/Tota11y.svelte';
	import MainContent from '$lib/components/MainContent.svelte';

	export const csr = false;
	export const prerender = true;
</script>

<div class="font-sans min-h-full flex flex-col text-black">
	<Header />
	<MainContent>
		<slot />
	</MainContent>
	<Tota11y />
</div>
