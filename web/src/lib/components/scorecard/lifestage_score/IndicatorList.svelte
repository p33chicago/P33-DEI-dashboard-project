<script type="ts">
	import type { Scorecard } from '$lib/domain/Scorecard';
	import { indicators as domain_indicators } from '$lib/domain/Indicator';
	import Indicator from '$lib/components/scorecard/lifestage_score/Indicator.svelte';

	export let indicators: Scorecard[number]['indicators'];

	indicators = domain_indicators.map((domain_indicator) => {
		const scorecard_indicator = indicators.find(
			(scorecard_indicator) => scorecard_indicator.route === domain_indicator.route
		);
		return scorecard_indicator || domain_indicator;
	});
</script>

{#each indicators as indicator}
	<Indicator {indicator} />
{/each}
