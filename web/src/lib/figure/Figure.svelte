<script lang="ts">
	import { browser } from '$app/environment';
	import ClientSideFigure from '$lib/figure/ClientSideFigure.svelte';
	import ServerSideFigure from '$lib/figure/ServerSideFigure.svelte';

	export let file: string;
</script>

{#if browser}
	<ClientSideFigure {file} />
{:else}
	<ServerSideFigure {file} />
{/if}
