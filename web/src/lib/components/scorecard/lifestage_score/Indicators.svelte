<script type="ts">
	import type { Scorecard } from '../../../domain/Scorecard';
	import { indicators as domain_indicators } from '../../../domain/Indicator.ts';

	export let indicators: Scorecard[number]['indicators'];

	indicators = domain_indicators.map((domain_indicator) => {
		const scorecard_indicator = indicators.find(
			(scorecard_indicator) => scorecard_indicator.route === domain_indicator.route
		);
		return scorecard_indicator || domain_indicator;
	});
</script>

{#each indicators as indicator}
	{#if typeof indicator.score === 'number'}
		<div>
			<div class="flex mb-3">
				<div class="text-sm grow">
					{indicator.name}
				</div>
				<div data-test-id="scorecard.indicator-score-{indicator.route}" class="text-sm">
					{indicator.score.toPrecision(3)}
				</div>
			</div>
			<div class="h-[4px] bg-light-gray rounded-full">
				{#if indicator.name === 'Access'}
					<div class="bg-blue h-full rounded-l-full" style={`width: ${indicator.score}%`} />
				{:else if indicator.name === 'Proficiency'}
					<div
						class="bg-brand-primary-dark-green h-full rounded-l-full"
						style={`width: ${indicator.score}%`}
					/>
				{:else}
					<div class="bg-warn-orange h-full rounded-l-full" style={`width: ${indicator.score}%`} />
				{/if}
			</div>
		</div>
	{:else}
		<div class="hidden relative -mb-10 sm:block">
			<div class="hidden relative -mb-10 sm:block flex text-sm">&nbsp;</div>
			<div class="h-[4px]" />
		</div>
	{/if}
{/each}
