<script type="ts">
	import Header from './Header.svelte';
	import Indicators from '$lib/scorecard/lifestage_score/Indicators.svelte';
	import type { Scorecard } from '$lib/domain/Scorecard';

	export let lifestage: Scorecard[number];
	let { area, score, indicators } = lifestage;
</script>

<div class="bg-white text-black py-3.5 px-2">
	<Header {lifestage} {area} {score} />
	<div class="bg-light-gray w-[268px] h-[113px]">
		<em class="text-white w-full h-full block leading-[113px] text-center">placeholder</em>
	</div>
	<Indicators {indicators} />
</div>
