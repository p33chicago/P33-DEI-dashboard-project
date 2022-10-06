<script type="ts">
	import Card from './Card.svelte';
</script>

<Card>
	<slot />
	{#if $$slots.more}
		<slot name="more" />
	{/if}
</Card>
