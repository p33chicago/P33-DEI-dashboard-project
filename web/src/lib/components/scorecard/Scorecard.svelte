<script type="ts">
	import LifestageScore from './lifestage_score/LifestageScore.svelte';
	import type { Scorecard } from '$lib/domain/Scorecard';

	export let scorecard: Scorecard;
</script>

{#each scorecard as lifestage}
	<LifestageScore {lifestage} />
{/each}
