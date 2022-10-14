<script type="ts">
	export let href: string | undefined;
</script>

{#if href}
	<a {href} target="_blank" class="ml-auto mr-auto sm:ml-0 sm:mr-0">
		<img {...$$restProps} />
	</a>
{:else}
	<img {...$$restProps} class="ml-auto mr-auto sm:ml-0 sm:mr-0" />
{/if}
