<script type="ts">
	export let href: string | undefined = undefined;
</script>

<li {...$$restProps} class="{$$props.class || ''} inline-block leading-loose">
	{#if href}
		<a class="text-white whitespace-nowrap px-1 sm:px-2" {href}><slot /></a>
	{:else}
		<span class="text-white whitespace-nowrap px-1 sm:px-2"><slot /></span>
	{/if}
</li>
