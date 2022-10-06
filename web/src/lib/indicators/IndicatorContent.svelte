<script type="ts">
	import type { Indicator } from '$lib/domain/Indicator.ts';
	import { access, indicators, proficiency } from '$lib/domain/Indicator.ts';
	import IndicatorCard from '$lib/cards/IndicatorCard.svelte';
	import AccessSnippet from '$lib/indicators/snippets/AccessSnippet.svelte';
	import ProficiencySnippet from '$lib/indicators/snippets/ProficiencySnippet.svelte';
	import ExcellenceSnippet from '$lib/indicators/snippets/ExcellenceSnippet.svelte';

	export let active_indicator: Indicator;
</script>

{#each indicators as indicator}
	{#if active_indicator.name === indicator.name}
		<IndicatorCard>
			<div class="pb-3 border-b-[1px] border-light-gray">
				{#if indicator === access}
					<AccessSnippet />
				{:else if indicator === proficiency}
					<ProficiencySnippet />
				{:else}
					<ExcellenceSnippet />
				{/if}
			</div>

			<div class="divide-solid">
				<slot />
			</div>
		</IndicatorCard>
	{:else}
		<a href={indicator.route} class="md:hidden">
			<IndicatorCard>
				{#if indicator === access}
					<AccessSnippet />
				{:else if indicator === proficiency}
					<ProficiencySnippet />
				{:else}
					<ExcellenceSnippet />
				{/if}
			</IndicatorCard>
		</a>
	{/if}
{/each}
