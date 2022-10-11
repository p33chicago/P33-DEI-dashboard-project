<script type="ts">
	import type { Indicator } from '$lib/domain/Indicator';
	import { access, indicators, proficiency } from '$lib/domain/Indicator';
	import IndicatorCard from '$lib/components/cards/IndicatorCard.svelte';
	import AccessSnippet from './snippets/AccessSnippet.svelte';
	import ProficiencySnippet from './snippets/ProficiencySnippet.svelte';
	import ExcellenceSnippet from './snippets/ExcellenceSnippet.svelte';

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
