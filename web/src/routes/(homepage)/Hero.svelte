<script>
	import TextHighlight from '$lib/components/TextHighlight.svelte';
	import { base } from '$app/paths';
	import Button from '$lib/components/Button.svelte';
	import BodyContentContainer from '$lib/components/BodyContentContainer.svelte';
</script>

<div class="order-first col-span-1 sm:col-span-4 bg-hero bg-no-repeat bg-center py-20">
	<BodyContentContainer>
		<div class="sm:col-span-4">
			<h1 class="text-6xl leading-relaxed text-black max-w-[447px]">
				Building Chicago's <TextHighlight
					class="leading-[1.2]"
					offset_left="0.75"
					offset_right="0.75">Inclusive Tech</TextHighlight
				> Future
			</h1>
			<Button href="{base}/about">Learn more</Button>
		</div>
	</BodyContentContainer>
</div>
