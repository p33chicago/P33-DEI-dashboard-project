<script>
	export let header;
	export let subheader;
</script>

<div class="data-dive grid grid-cols-1 sm:grid-cols-2 gap-4 border-b-[1px] border-light-gray pb-9">
	<div class="col-span-1 sm:col-span-2 pt-9 -order-2 sm:order-none">
		<h3>{header}</h3>
	</div>
	<div class="col-span-1">
		<h4>What does the data tell?</h4>
		<div class="space-y-6">
			<slot name="story" />
		</div>

		<h4 class="mt-6">Takeaways</h4>
		<div class="space-y-6">
			<slot name="takeaways" />
		</div>
	</div>
	<div class="flex flex-col col-span-1 -order-1 sm:order-none">
		<div class="aspect-square min-h-[200px]">
			<slot name="figure" />
		</div>
		<div class="grow">
			<p>{subheader}</p>
		</div>
	</div>
</div>
