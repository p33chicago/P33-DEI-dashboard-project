<script type="ts">
	import type { Lifestage } from '../../../domain/Lifestage';
	import { assets } from '$app/paths';

	export let lifestage: Lifestage;
	export let area: string;
	export let score: number;
</script>

<div class="flex items-start gap-2">
	<div class="pt-1 h-[22px]">
		{#if lifestage.name === 'K-8'}
			<img src={`${assets}/spaceship.svg`} />
		{:else if lifestage.name === 'High School'}
			<img src={`${assets}/certificate.svg`} />
		{:else if lifestage.name === 'College'}
			<img src={`${assets}/mortarboard-cap.svg`} />
		{:else}
			<img src={`${assets}/handshake.svg`} />
		{/if}
	</div>
	<div class="grow">
		<h1 class="text-2xl text-black">{lifestage.name}</h1>
		<h2
			class="text-sm uppercase font-sans-alternate text-dark-gray"
			data-test-id="scorecard.lifestage-area-{lifestage.route}"
		>
			{area}
		</h2>
	</div>
	{#if typeof score === 'number'}
		<div class="text-right relative">
			<span
				data-test-id="scorecard.lifestage-score-{lifestage.route}"
				class="font-sans-alternate block text-5xl text-brand-primary-dark-green"
				>{score.toPrecision(3)}</span
			>
			<span class="block absolute right-0 overflow-hidden bg-medium-gray h-[1px] w-10">/</span>
			<span class="block text-dark-gray">100</span>
			<span class="block text-dark-gray text-xs">Equity Index</span>
		</div>
	{/if}
</div>
