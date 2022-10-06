<script type="ts">
	import LifestageScore from '$lib/scorecard/lifestage_score/LifestageScore.svelte';
	import type { Scorecard } from '../domain/Scorecard';

	export let scorecard: Scorecard;
</script>

{#each scorecard as lifestage}
	<LifestageScore {lifestage} />
{/each}
