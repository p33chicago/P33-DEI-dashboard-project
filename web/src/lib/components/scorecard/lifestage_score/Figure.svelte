<script type="ts">
	import type { Scorecard } from '$lib/domain/Scorecard';
	import BaseFigure from '$lib/components/figure/Figure.svelte';

	export let lifestage: Scorecard[number];
	let { route } = lifestage;
	let file = route && `scorecard/figure_${route}`; // TODO avoid having to translate here, by storing the figure filename in scorecard
</script>

<div
	class="py-4 w-full min-h-[100px] aspect-ratio-[268/100]"
	data-test-id="scorecard.figure-{route}"
>
	{#if file}
		<BaseFigure {file} svg_only />
	{/if}
</div>
