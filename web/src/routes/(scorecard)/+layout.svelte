<script type="ts">
	import DataSidebar from '$lib/components/DataSidebar.svelte';
	import IndicatorNav from '$lib/components/IndicatorNav.svelte';
	import IndicatorContent from '$lib/components/IndicatorContent.svelte';
	import BannerTitle from '$lib/components/BannerTitle.svelte';

	export let data;
	$: lifestage = data.lifestage;
	$: indicator = data.indicator;
</script>

<svelte:head>
	<title>{lifestage.name}: {indicator.name}</title>
</svelte:head>

<BannerTitle subtitle="Equity index scorecard" title={lifestage?.name || 'Methodology'} />

<div class="w-full h-full grow bg-brand-primary-really-light-green">
	<div class="grow h-full flex flex-row max-w-7xl sm:pl-7 lg:pl-8 md:mx-auto">
		<div class="hidden md:block h-full text-xl py-8 pr-8">
			<DataSidebar {lifestage} />
		</div>
		<div class="grow bg-white px-8 w-full h-full">
			<div class="hidden md:block space-x-5 py-8">
				<IndicatorNav {indicator} {lifestage} />
			</div>

			<div class="">
				<IndicatorContent active_indicator={indicator}>
					<slot />
				</IndicatorContent>
			</div>
		</div>
	</div>
</div>
