<script type="ts">
	import DataSidebar from '$lib/components/DataSidebar.svelte';
	import IndicatorNav from '$lib/components/IndicatorNav.svelte';
	import IndicatorContent from '$lib/components/indicators/IndicatorContent.svelte';
	import BodyContentContainer from '$lib/components/BodyContentContainer.svelte';
	import BannerTitle from '$lib/components/BannerTitle.svelte';
	import { career } from '$lib/domain/Lifestage';

	export let data;

	$: title = `Tech Equity Index: ${indicator.name} in ${
		lifestage === career ? 'Workplace' : lifestage.name
	}`;
	$: lifestage = data.lifestage;
	$: indicator = data.indicator;
</script>

<svelte:head>
	<title>{title}</title>
</svelte:head>

<BannerTitle subtitle="Equity index scorecard" title={lifestage.name} />

<BodyContentContainer>
	<DataSidebar {lifestage} />

	<IndicatorNav {indicator} {lifestage} />

	<div class="grid auto-rows-min row-span-2 col-span-4 md:col-span-3 gap-y-4">
		<IndicatorContent active_indicator={indicator}>
			<slot />
		</IndicatorContent>
	</div>
</BodyContentContainer>
