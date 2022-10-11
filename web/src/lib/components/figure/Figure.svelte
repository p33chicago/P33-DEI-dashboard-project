<script lang="ts">
	import { browser } from '$app/environment';
	import ClientSideFigure from './ClientSideFigure.svelte';
	import ServerSideFigure from './ServerSideFigure.svelte';

	export let file: string;
</script>

{#if browser}
	<ClientSideFigure {file} />
{:else}
	<ServerSideFigure {file} />
{/if}
