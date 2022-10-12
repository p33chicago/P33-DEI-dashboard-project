<script lang="ts">
	import '../app.css';
	import Header from '$lib/components/header/Header.svelte';
	import Tota11y from '$lib/components/Tota11y.svelte';
	import MainContent from '$lib/components/MainContent.svelte';
	import Footer from '$lib/components/footer/Footer.svelte';

	export const csr = false;
	export const prerender = true;
</script>

<Header />
<MainContent>
	<slot />
</MainContent>
<Footer />
<Tota11y />
