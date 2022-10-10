<script type="ts">
	export let heading: string;
</script>

<div class="flex flex-col sm:flex-row py-8">
	<div class="min-w-[100px] sm:min-w-[147px]">
		<slot name="graphic" />
	</div>
	<div class="ml-2">
		<p class="text-4xl sm:text-5xl font-sans-alternate text-black">{heading}</p>
		<div class="font-mono text-black">
			<slot />
		</div>
	</div>
</div>
