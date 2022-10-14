<script type="ts">
	export let active: boolean;
</script>

{#if active}
	<a {...$$restProps}>
		<slot />
	</a>
{:else}
	<slot />
{/if}
