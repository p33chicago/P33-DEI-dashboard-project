<script type="ts">
	export let active: boolean;
	export let href: string;
</script>

{#if active}
	<a {href} {...$$restProps}>
		<slot />
	</a>
{:else}
	<slot />
{/if}
