<script type="ts">
	export let heading: string;
</script>

<slot name="graphic" />
<div class="px-4">
	<p class="text-4xl sm:text-5xl font-sans-alternate">{heading}</p>
	<div class="font-mono text-xl">
		<slot />
	</div>
</div>
