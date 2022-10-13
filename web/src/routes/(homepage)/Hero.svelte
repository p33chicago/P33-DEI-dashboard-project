<script>
	import TextHighlight from '$lib/components/TextHighlight.svelte';
	import { base } from '$app/paths';
	import Button from '$lib/components/Button.svelte';
</script>

<div
	class="order-first col-span-1 sm:col-span-4 bg-hero bg-no-repeat bg-[length:170vw] bg-[top_right_-190px] sm:bg-contain sm:bg-right-top w-full sm:h-[calc(100vw/2.88)] gap-y-12 md:gap-y-3.5 px-6 lg:px-8"
>
	<div class="max-w-7xl mx-auto sm:col-span-4 space-y-4 flex flex-col justify-center pt-10">
		<h1 class="text-2xl sm:text-3xl lg:text-6xl text-black max-w-[8em]">
			Building Chicago's
			<TextHighlight max_offset_y="0" offset_left="0.75" offset_right="0.75">
				Inclusive Tech
			</TextHighlight>
			Future
		</h1>
		<Button href="{base}/about">Learn more</Button>
	</div>
</div>
