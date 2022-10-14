<script type="ts">
	import type { Lifestage } from '$lib/domain/Lifestage';
	import type { Indicator } from '$lib/domain/Indicator';
	import { indicators } from '$lib/domain/Indicator';
	import { base } from '$app/paths';

	export let lifestage: Lifestage;
	export let indicator: Indicator;
</script>

{#each indicators as _indicator}
	<a
		class="inline-block leading-9 border-2 rounded-full md:px-6 lg:px-6 uppercase"
		class:bg-brand-primary-dark-green={_indicator.route === indicator.route}
		class:text-white={_indicator.route === indicator.route}
		href={`${base}/${lifestage.route}/${_indicator.route}`}>{_indicator.name}</a
	>
{/each}
