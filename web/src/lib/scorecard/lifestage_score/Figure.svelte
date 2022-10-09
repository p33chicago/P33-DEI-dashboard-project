<script type="ts">
	import type { Scorecard } from '$lib/domain/Scorecard';
	import BaseFigure from '$lib/figure/Figure.svelte';
	import { domain_to_p33py } from '$lib/p33py_adapter/lifestage_map.ts';

	export let lifestage: Scorecard[number];
	let { route } = lifestage;
	let file = route && `ei_${domain_to_p33py[route]}`; // TODO: avoid having to translate here, by storing the figure filename in scorecard
</script>

<div class="py-4 w-full min-h-[113px] aspect-[268/113]" data-test-id="scorecard.figure-{route}">
	{#if file}
		<BaseFigure {file} />
	{/if}
</div>
