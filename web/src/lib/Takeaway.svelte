<script type="ts">
	export let heading: string;
</script>

<slot name="graphic" />
<div class="px-4">
	<p class="text-4xl sm:text-5xl font-sans-alternate text-black">{heading}</p>
	<div class="font-mono text-black">
		<slot />
	</div>
</div>
