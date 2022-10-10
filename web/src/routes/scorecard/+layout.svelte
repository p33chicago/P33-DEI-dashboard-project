<script type="ts">
	import DataSidebar from '$lib/DataSidebar.svelte';
	import BodyContentContainer from '$lib/BodyContentContainer.svelte';
	import BannerTitle from '$lib/BannerTitle.svelte';
</script>

<svelte:head>
	<title>Scorecard</title>
</svelte:head>

<BannerTitle
	subtitle="Equity index scorecard"
	title="Kindergarten-8th, High School, College, Career"
/>

<BodyContentContainer>
	<DataSidebar />

	<div class="grid auto-rows-min row-span-2 col-span-1 sm:col-span-4 md:col-span-3 gap-y-4">
		<slot />
	</div>
</BodyContentContainer>
