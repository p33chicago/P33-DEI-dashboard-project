<script>
	import Card from './cards/Card.svelte';
	import { base } from '$app/paths';
	import { lifestages } from '$lib/domain/Lifestage';
	import ConditionalLink from '$lib/components/ConditionalLink.svelte';

	export let lifestage;
</script>

<div class="hidden md:grid col-span-1 row-span-2 text-xl auto-rows-min gap-4">
	<Card>
		<ul class="subnav uppercase font-sans-alternate mx-3 text-brand-primary-green">
			{#each lifestages as _lifestage}
				{#if lifestage === _lifestage}
					<li>{_lifestage.name}</li>
				{:else}
					<li>
						<a href="{base}/{_lifestage.route}/access">{_lifestage.name}</a>
					</li>
				{/if}
			{/each}
			<li>
				<ConditionalLink active={lifestage} href="{base}/methodology">Methodology</ConditionalLink>
			</li>
		</ul>
	</Card>
</div>

<style>
	a,
	.subnav :global(a) {
		color: theme('colors.black');
	}
</style>
