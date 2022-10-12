<script type="ts">
	import Scorecard from '$lib/components/scorecard/Scorecard.svelte';
	import Definitions from '$lib/components/scorecard/definitions/Definitions.svelte';
	import type { Scorecard as ScorecardType } from '$lib/domain/Scorecard';

	export let data: { scorecard: ScorecardType };
	let { scorecard } = data;
</script>

<svelte:head>
	<title>Scorecard</title>
	<meta
		content="Combining numerous data sources to assess how well schools, colleges and companies support underrepresented populations on tech career pathways in Chicago."
		name="description"
	/>
</svelte:head>

<Scorecard {scorecard} />
<div class="text-white sm:col-span-4 bg-black/60 px-8 py-4 bg-blend-multiply my-6 pb-4">
	<Definitions />
</div>
