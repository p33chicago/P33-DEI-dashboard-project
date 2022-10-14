<script type="ts">
	import type { Indicator } from '$lib/domain/Indicator';
	import { indicators } from '$lib/domain/Indicator';
	import Heading from './Heading.svelte';
	import ConditionalLink from './ConditionalLink.svelte';
	import Caret from '$lib/components/icons/Caret.svelte';
	import CardWhenSmall from '$lib/components/cards/CardWhenSmall.svelte';

	export let active_indicator: Indicator;

	$: is_active = (indicator: Indicator) => active_indicator.name === indicator.name;
</script>

{#each indicators as indicator}
	<ConditionalLink active={!is_active(indicator)} href={indicator.route} class="md:hidden">
		<CardWhenSmall>
			<details open={is_active(indicator)} class:active={is_active(indicator)}>
				<summary class="list-none">
					<Heading nohr class="flex">
						<span class="grow"> {indicator.name}</span>
						<span class="caret self-center sm:hidden">
							<Caret />
						</span>
					</Heading>
				</summary>
				{#if is_active(indicator)}
					<div class="border-light-gray border-t-[1px]">
						<slot />
					</div>
				{/if}
			</details>
		</CardWhenSmall>
	</ConditionalLink>
{/each}

<style>
	details[open] .caret {
		transform: rotate(180deg);
	}

	/** Prevent the active indicator from closing for non-mobile */
	@media screen(sm) {
		details summary {
			pointer-events: none; /* prevents click events */
			user-select: none; /* prevents text selection */
		}
	}
</style>
