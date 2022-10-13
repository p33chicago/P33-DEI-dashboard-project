<script type="ts">
	import type { Scorecard } from '$lib/domain/Scorecard';

	export let indicator: Scorecard[number]['indicators'][number];
	$: has_score = typeof indicator.score === 'number';
</script>

<div>
	<div class="flex mb-3">
		<div class="text-sm grow" class:text-medium-gray={!has_score}>
			{indicator.name}
		</div>
		{#if has_score}
			<div class="text-sm" data-test-id="scorecard.indicator-score-{indicator.route}">
				{indicator.score.toPrecision(3)}
			</div>
		{/if}
	</div>
	<div class="h-[4px] bg-light-gray rounded-full">
		{#if !has_score}
			<!-- don't show a color bar -->
		{:else if indicator.name === 'Access'}
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
