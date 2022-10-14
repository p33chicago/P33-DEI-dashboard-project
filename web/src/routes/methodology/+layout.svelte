<script type="ts">
	import DataSidebar from '$lib/components/DataSidebar.svelte';
	import BodyContentContainer from '$lib/components/BodyContentContainer.svelte';
	import BannerTitle from '$lib/components/BannerTitle.svelte';
</script>

<svelte:head>
	<title>Scorecard</title>
</svelte:head>

<BannerTitle title="Methodology" />

<BodyContentContainer>
	<DataSidebar />

	<div class="grid auto-rows-min row-span-2 col-span-1 sm:col-span-4 md:col-span-3 gap-y-4">
		<slot />
	</div>
</BodyContentContainer>
