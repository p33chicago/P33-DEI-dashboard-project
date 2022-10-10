<script type="ts">
	import Header from './Header.svelte';
	import Indicators from '$lib/scorecard/lifestage_score/Indicators.svelte';
	import type { Scorecard } from '$lib/domain/Scorecard';
	import Figure from './Figure.svelte';

	export let lifestage: Scorecard[number];
	let { area, score, indicators } = lifestage;
</script>

<div class="flex flex-col flex-initial bg-white text-black p-5">
	<div class="grow">
		<Header {area} {lifestage} {score} />
	</div>
	<Figure {lifestage} />
	<div class="flex flex-col gap-y-5">
		<Indicators {indicators} />
	</div>
</div>
