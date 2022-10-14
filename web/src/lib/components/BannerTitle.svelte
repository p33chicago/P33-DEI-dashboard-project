<script type="ts">
	import BodyContentContainer from './BodyContentContainer.svelte';
	import MapBackground from './MapBackground.svelte';

	export let title: string;
	export let subtitle: string | undefined = undefined;
</script>

<MapBackground>
	<BodyContentContainer>
		<div class="font-sans-alternate col-span-4 py-8 sm:py-12">
			<h1 class="text-white">{title}</h1>
			{#if subtitle}
				<h2 class="uppercase text-heads-up-yellow">{subtitle}</h2>
			{/if}
		</div>
	</BodyContentContainer>
</MapBackground>
