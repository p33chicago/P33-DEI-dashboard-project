<script type="ts">
	import type { Lifestage } from '$lib/domain/Lifestage';
	import SpaceshipIcon from '$lib/components/icons/SpaceshipIcon.svelte';
	import CertificateIcon from '$lib/components/icons/CertificateIcon.svelte';
	import MortarboardcapIcon from '$lib/components/icons/MortarboardCapIcon.svelte';
	import HandshakeIcon from '$lib/components/icons/HandshakeIcon.svelte';

	export let lifestage: Lifestage;
	export let area: string;
	export let score: number | undefined;
</script>

<div class="flex items-start gap-2">
	<div class="pt-1 h-[22px]">
		{#if lifestage.name === 'K-8'}
			<SpaceshipIcon />
		{:else if lifestage.name === 'High School'}
			<CertificateIcon />
		{:else if lifestage.name === 'College'}
			<MortarboardcapIcon />
		{:else}
			<HandshakeIcon />
		{/if}
	</div>
	<div class="grow">
		<h2 class="font-sans-alternate text-2xl text-black">{lifestage.name}</h2>
		<span
			class="text-sm uppercase font-sans-alternate text-dark-gray"
			data-test-id="scorecard.lifestage-area-{lifestage.route}"
		>
			{area}
		</span>
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
