<script type="ts">
	import BodyContentContainer from '$lib/BodyContentContainer.svelte';
	import MapBackground from '$lib/MapBackground.svelte';

	export let title: string;
	export let subtitle: string;
</script>

<MapBackground>
	<BodyContentContainer>
		<div class="font-sans-alternate col-span-4 py-8 sm:py-12">
			<h1 class="text-white">{title}</h1>
			<h2 class="text-heads-up-yellow">{subtitle}</h2>
		</div>
	</BodyContentContainer>
</MapBackground>
