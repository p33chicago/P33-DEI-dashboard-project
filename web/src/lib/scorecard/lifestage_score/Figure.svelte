<script type="ts">
	import type { Scorecard } from '$lib/domain/Scorecard';
	import BaseFigure from '$lib/figure/Figure.svelte';

	export let lifestage: Scorecard[number];
	let { route } = lifestage;
	let file = route && `scorecard/figure_${route}`; // TODO avoid having to translate here, by storing the figure filename in scorecard
</script>

<div class="py-4 w-full min-h-[100px] aspect-[2.371]" data-test-id="scorecard.figure-{route}">
	{#if file}
		<BaseFigure {file} />
	{/if}
</div>
