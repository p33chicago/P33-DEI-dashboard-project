<script lang="ts">
	import Card from './cards/Card.svelte';
	export let access: string;
	export let proficiency: string;
	export let excellence: string;
</script>

<Card>
	<p>Access <span class="text-3xl">{access}</span></p>
	<p>Proficiency <span class="text-3xl">{proficiency}</span></p>
	<p>Excellence <span class="text-3xl">{excellence}</span></p>
</Card>
