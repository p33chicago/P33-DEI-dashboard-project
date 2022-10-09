<script type="ts">
	import Header from './Header.svelte';
	import Indicators from '$lib/scorecard/lifestage_score/Indicators.svelte';
	import type { Scorecard } from '$lib/domain/Scorecard';
	import Figure from './Figure.svelte';

	export let lifestage: Scorecard[number];
	let { area, score, indicators } = lifestage;
</script>

<div class="flex flex-col flex-initial bg-white text-black py-3.5 px-2">
	<div class="grow">
		<Header {lifestage} {area} {score} />
	</div>
	<Figure {lifestage} />
	<Indicators {indicators} />
</div>
