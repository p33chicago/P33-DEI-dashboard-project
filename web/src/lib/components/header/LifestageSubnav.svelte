<script lang="ts">
	import { base } from '$app/paths';
	import { indicators } from '$lib/domain/Indicator';
	import Caret from '$lib/components/icons/Caret.svelte';
	import type { Lifestage } from '$lib/domain/Lifestage';

	export let lifestage: Lifestage;

	const dont_hide_nav = () => {
		/* do nothing */
	};
</script>

<details class="open:bg-white">
	<summary
		class="text-brand-primary-dark-green leading-6 select-none"
		on:click|capture|stopPropagation={dont_hide_nav}
	>
		<span class="leading-8">{lifestage.name}</span>
		<Caret />
	</summary>

	<div class="mt-3 text-sm leading-6">
		<ul>
			{#each indicators as indicator}
				<li>
					<a
						href={`${base}/${lifestage.route}/${indicator.route}`}
						class="hover:text-brand-primary-green">{indicator.name}</a
					>
				</li>
			{/each}
		</ul>
	</div>
</details>

<style>
	li {
		padding: 0.25rem 1rem;
	}

	summary {
		list-style: none;
	}

	[open] > summary > :global(svg) {
		transform: rotate(180deg);
	}
</style>
