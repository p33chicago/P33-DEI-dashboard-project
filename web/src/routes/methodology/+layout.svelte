<script type="ts">
	import DataSidebar from '../../lib/components/DataSidebar.svelte';
	import BannerTitle from '../../lib/components/BannerTitle.svelte';
</script>

<svelte:head>
	<title>Scorecard</title>
</svelte:head>

<BannerTitle title="Methodology" />

<div class="w-full h-full grow bg-brand-primary-really-light-green">
	<div class="grow h-full flex flex-row max-w-7xl sm:pl-7 lg:pl-8 md:mx-auto">
		<div class="hidden md:block h-full text-xl py-8 pr-8">
			<DataSidebar />
		</div>
		<div class="grow bg-white px-8 w-full h-full">
			<div class="">
				<slot />
			</div>
		</div>
	</div>
</div>
