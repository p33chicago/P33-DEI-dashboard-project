<script type="ts">
	export let image_href: string | undefined;
</script>

<div class="flex-none sm:flex items-center">
	{#if image_href}
		<a href={image_href} target="_blank" class="flex-none">
			<slot name="image" />
		</a>
	{:else}
		<slot name="image" />
	{/if}
	<p class="flex-grow">
		<slot />
	</p>
</div>
