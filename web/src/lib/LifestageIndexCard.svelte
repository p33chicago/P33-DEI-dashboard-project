<script lang="ts">
	import Card from './cards/Card.svelte';
	export let chicago: string;
	export let us: string;
</script>

<Card>
	<p>Chicago: {chicago}</p>
	<p>US: {us}</p>
</Card>
