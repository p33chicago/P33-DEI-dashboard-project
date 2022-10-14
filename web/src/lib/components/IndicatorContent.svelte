<script type="ts">
	import type { Indicator } from '$lib/domain/Indicator';
	import { indicators } from '$lib/domain/Indicator';
	import Card from './cards/Card.svelte';
	import Heading from './Heading.svelte';
	import ConditionalLink from './ConditionalLink.svelte';

	export let active_indicator: Indicator;
</script>

{#each indicators as indicator}
	<ConditionalLink
		active={active_indicator.name !== indicator.name}
		href={indicator.route}
		class="md:hidden"
	>
		<Card>
			<Heading>{indicator.name}</Heading>
			{#if active_indicator.name === indicator.name}
				<slot />
			{/if}
		</Card>
	</ConditionalLink>
{/each}
